"""
test_infrastructure.py — Verifies the company_sim.py shared module.
"""

import os
import sys
import json
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for testing
import matplotlib.pyplot as plt
import ipywidgets as widgets

# Ensure local module is importable
sys.path.insert(0, os.path.dirname(__file__))

from company_sim import (
    CompanySimulator, MonteCarloEngine, DiagnosticSuite, AutopsyReport,
    record_trap_response, get_trap_response, check_gate, get_all_responses,
    create_trap_widget, _trap_responses, COLORS,
)


class TestCompanySimulator(unittest.TestCase):

    def setUp(self):
        self.sim = CompanySimulator()

    def test_generate_shape_and_columns(self):
        df = self.sim.generate(n=200, seed=0)
        self.assertEqual(df.shape[0], 200)
        self.assertListEqual(
            sorted(df.columns.tolist()),
            sorted(['revenue', 'ad_spend', 'staff_count', 'satisfaction']),
        )

    def test_ad_spend_always_positive(self):
        for seed in range(10):
            df = self.sim.generate(n=1000, seed=seed)
            self.assertTrue((df['ad_spend'] > 0).all(),
                            f"Negative ad_spend found with seed={seed}")

    def test_truth_returns_demand_U(self):
        df, params = self.sim.truth(n=100, seed=42)
        self.assertIn('demand_U', df.columns)
        self.assertEqual(df.shape[1], 5)
        self.assertIn('beta_0', params)
        self.assertIn('beta_1', params)
        self.assertIn('beta_U', params)

    def test_truth_params_match_defaults(self):
        _, params = self.sim.truth()
        self.assertEqual(params['beta_0'], 50)
        self.assertEqual(params['beta_1'], 8)
        self.assertEqual(params['beta_2'], 3)
        self.assertEqual(params['beta_U'], 2)

    def test_set_methods(self):
        self.sim.set_heteroscedasticity(1.0)
        self.assertEqual(self.sim.heteroscedasticity_strength, 1.0)
        self.sim.set_endogeneity(10)
        self.assertEqual(self.sim.endogeneity_strength, 10)
        self.sim.set_nonlinearity(False)
        self.assertFalse(self.sim.nonlinearity)

    def test_dgp_summary_is_string(self):
        s = self.sim.dgp_summary()
        self.assertIsInstance(s, str)
        self.assertIn('Y', s)

    def test_reproducibility(self):
        df1 = self.sim.generate(n=100, seed=7)
        df2 = self.sim.generate(n=100, seed=7)
        pd.testing.assert_frame_equal(df1, df2)


class TestOVBFormula(unittest.TestCase):
    """
    Critical test: OVB prediction matches simulation mean.

    With linear DGP (nonlinearity=False):
    Y = beta_0 + beta_1 * X1 + beta_2 * X2 + beta_U * U + eps

    Short regression: Y ~ X1 (omitting X2 and U)
    E[beta_hat_1] = beta_1 + beta_U * delta_U + beta_2 * delta_2

    where delta_U = Cov(X1, U) / Var(X1)
          delta_2 = Cov(X1, X2) / Var(X1)
    """

    def test_ovb_prediction_matches_simulation(self):
        sim = CompanySimulator(
            endogeneity_strength=20,
            heteroscedasticity_strength=0.0,  # Remove heteroscedasticity for clean OVB test
            nonlinearity=False,  # Linear for exact OVB formula
            noise_sigma=1.0,
        )

        n_reps = 5000
        n_obs = 500
        beta1_hats = np.empty(n_reps)

        for r in range(n_reps):
            data = sim.generate(n=n_obs, seed=r)
            X = sm.add_constant(data['ad_spend'])
            model = sm.OLS(data['revenue'], X).fit()
            beta1_hats[r] = model.params['ad_spend']

        sim_mean = beta1_hats.mean()

        # Compute theoretical OVB using population moments
        # X1 = endo * U + eta1, X2 = 5 * U + eta2, U ~ N(0,1), eta ~ N(0, sigma^2)
        endo = sim.endogeneity_strength  # 20
        staff = sim.staff_loading         # 5
        sigma2 = sim.noise_sigma ** 2     # 1

        # Var(X1) = endo^2 * Var(U) + Var(eta1) = endo^2 + sigma^2
        var_X1 = endo**2 + sigma2

        # Cov(X1, U) = endo * Var(U) = endo
        cov_X1_U = endo

        # Cov(X1, X2) = endo * staff * Var(U) = endo * staff
        cov_X1_X2 = endo * staff

        delta_U = cov_X1_U / var_X1
        delta_2 = cov_X1_X2 / var_X1

        theoretical = sim.beta_1 + sim.beta_U * delta_U + sim.beta_2 * delta_2

        print(f"\n  OVB Test Results:")
        print(f"    Simulation mean(beta_hat_1) = {sim_mean:.4f}")
        print(f"    Theoretical E[beta_hat_1]   = {theoretical:.4f}")
        print(f"    Difference                  = {abs(sim_mean - theoretical):.4f}")

        self.assertAlmostEqual(sim_mean, theoretical, places=2,
            msg=f"Sim mean {sim_mean:.4f} != theoretical {theoretical:.4f}")


class TestMonteCarloEngine(unittest.TestCase):

    def test_run_shape(self):
        sim = CompanySimulator(nonlinearity=False, heteroscedasticity_strength=0)
        engine = MonteCarloEngine()

        def simple_estimator(data):
            X = sm.add_constant(data['ad_spend'])
            return sm.OLS(data['revenue'], X).fit().params['ad_spend']

        grid = [5.0, 10.0, 20.0]
        # Use small n_reps for speed
        results = engine.run(simple_estimator, 'endogeneity', grid, sim,
                             n_reps=10, n_obs=100)
        self.assertEqual(results.shape, (3, 10))

    def test_quick_run_shape(self):
        sim = CompanySimulator(nonlinearity=False, heteroscedasticity_strength=0)
        engine = MonteCarloEngine()

        def simple_estimator(data):
            X = sm.add_constant(data['ad_spend'])
            return sm.OLS(data['revenue'], X).fit().params['ad_spend']

        results = engine.quick_run(
            simple_estimator,
            lambda seed, n: sim.generate(n=n, seed=seed),
            n_reps=20, n_obs=100,
        )
        self.assertEqual(results.shape, (20,))


class TestDiagnosticSuite(unittest.TestCase):

    def test_run_diagnostics_4_subplots(self):
        sim = CompanySimulator()
        data = sim.generate(n=200, seed=0)
        X = sm.add_constant(data[['ad_spend', 'staff_count']])
        model = sm.OLS(data['revenue'], X).fit()

        diag = DiagnosticSuite()
        fig = diag.run_diagnostics(model)
        axes = fig.get_axes()
        self.assertEqual(len(axes), 4)
        plt.close(fig)

    def test_summary_tests_keys(self):
        sim = CompanySimulator()
        data = sim.generate(n=200, seed=0)
        X = sm.add_constant(data[['ad_spend', 'staff_count']])
        model = sm.OLS(data['revenue'], X).fit()

        diag = DiagnosticSuite()
        tests = diag.summary_tests(model)
        self.assertIn('vif', tests)
        self.assertIn('breusch_pagan', tests)
        self.assertIn('durbin_watson', tests)
        self.assertIn('jarque_bera', tests)
        self.assertEqual(len(tests['breusch_pagan']), 2)
        self.assertEqual(len(tests['jarque_bera']), 2)


class TestGateSystem(unittest.TestCase):

    def setUp(self):
        _trap_responses.clear()

    def test_record_and_retrieve(self):
        # Use a temp file to avoid writing to /content
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
            tmp_path = f.name
        import company_sim
        original_path = company_sim._TRAP_LOG_PATH
        company_sim._TRAP_LOG_PATH = tmp_path
        try:
            record_trap_response('notebook_1', 'q1', 'A')
            self.assertEqual(get_trap_response('notebook_1', 'q1'), 'A')
            self.assertTrue(check_gate('notebook_1', 'q1'))
            self.assertFalse(check_gate('notebook_1', 'q2'))
            self.assertIsNone(get_trap_response('notebook_1', 'q2'))

            # Verify JSON file was written
            with open(tmp_path) as f:
                data = json.load(f)
            self.assertIn('notebook_1_q1', data)
        finally:
            company_sim._TRAP_LOG_PATH = original_path
            os.unlink(tmp_path)

    def test_get_all_responses(self):
        record_trap_response('nb1', 'q1', 'A')
        record_trap_response('nb2', 'q1', 'C')
        all_resp = get_all_responses()
        self.assertEqual(len(all_resp), 2)


class TestAutopsyReport(unittest.TestCase):

    def test_lightweight_renders(self):
        report = AutopsyReport()
        w = report.lightweight(1)
        self.assertIsInstance(w, widgets.VBox)

    def test_full_renders(self):
        report = AutopsyReport()
        w = report.full(7, available_sidebars=['HRT', 'Google Flu Trends'])
        self.assertIsInstance(w, widgets.VBox)

    def test_full_without_sidebars(self):
        report = AutopsyReport()
        w = report.full(8)
        self.assertIsInstance(w, widgets.VBox)


class TestColors(unittest.TestCase):

    def test_color_keys(self):
        expected = {'ols', 'truth', 'bias', 'repair', 'alt'}
        self.assertEqual(set(COLORS.keys()), expected)


class TestTrapWidget(unittest.TestCase):

    def test_create_trap_widget(self):
        _trap_responses.clear()
        w = create_trap_widget('nb1', 'q1', 'Pick one:', ['A', 'B', 'C'])
        self.assertIsInstance(w, widgets.VBox)


if __name__ == '__main__':
    unittest.main(verbosity=2)
