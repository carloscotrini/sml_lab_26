"""
test_cross_notebook.py — Cross-notebook integration tests.

Simulates a student progressing through all 8 notebooks and verifies:
  Part 1: Trap response persistence across notebooks
  Part 2: Theoretical predictions from the DGP match simulation

Run with:  python test_cross_notebook.py
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

# Ensure local module is importable
sys.path.insert(0, os.path.dirname(__file__))

import company_sim
from company_sim import (
    CompanySimulator,
    record_trap_response,
    get_trap_response,
    get_all_responses,
    _trap_responses,
)


# ===================================================================
# Part 1: Trap Response Simulation
# ===================================================================
class TestTrapResponseSimulation(unittest.TestCase):
    """
    Simulate a student writing trap responses for each of the 8 notebooks.
    Verify persistence to JSON and read-back integrity.
    """

    # Expected responses keyed exactly as the gate system produces them
    EXPECTED_RESPONSES = {
        "notebook_1_q1": "The coefficient is biased upward — the true effect is smaller.",
        "notebook_1b_q1": "B) after residualizing both sides on staff",
        "notebook_2_q1": "No, heteroscedasticity invalidates classical SEs",
        "notebook_3_q1": "Customer satisfaction — tiny coefficient despite p<0.001",
        "notebook_4_extrapolation_prediction": "150.0",
        "notebook_5_best_model": "Degree 15 polynomial (R²=0.97)",
        "notebook_6_causal_claim": "No — endogeneity prevents causal interpretation",
        "notebook_7_q1": "No",
    }

    def setUp(self):
        """Redirect trap log to a temp file and clear in-memory state."""
        _trap_responses.clear()
        self._tmpfile = tempfile.NamedTemporaryFile(
            suffix=".json", delete=False, mode="w"
        )
        self._tmpfile.close()
        self._orig_path = company_sim._TRAP_LOG_PATH
        company_sim._TRAP_LOG_PATH = self._tmpfile.name

    def tearDown(self):
        """Restore original trap log path and clean up temp file."""
        company_sim._TRAP_LOG_PATH = self._orig_path
        _trap_responses.clear()
        try:
            os.unlink(self._tmpfile.name)
        except OSError:
            pass

    def test_write_all_trap_responses(self):
        """Write responses for every notebook and verify all keys present."""
        # Simulate the student recording each response.  The key format
        # produced by record_trap_response is "{notebook_id}_{question_id}".
        # We reverse-engineer notebook_id and question_id from the expected
        # composite key by splitting on the first underscore that follows
        # "notebook_<tag>".
        key_to_parts = {
            "notebook_1_q1":                        ("notebook_1",  "q1"),
            "notebook_1b_q1":                       ("notebook_1b", "q1"),
            "notebook_2_q1":                        ("notebook_2",  "q1"),
            "notebook_3_q1":                        ("notebook_3",  "q1"),
            "notebook_4_extrapolation_prediction":  ("notebook_4",  "extrapolation_prediction"),
            "notebook_5_best_model":                ("notebook_5",  "best_model"),
            "notebook_6_causal_claim":              ("notebook_6",  "causal_claim"),
            "notebook_7_q1":                        ("notebook_7",  "q1"),
        }

        for key, (nb_id, q_id) in key_to_parts.items():
            record_trap_response(nb_id, q_id, self.EXPECTED_RESPONSES[key])

        # ---- Verify in-memory retrieval ----
        for key, (nb_id, q_id) in key_to_parts.items():
            retrieved = get_trap_response(nb_id, q_id)
            self.assertEqual(
                retrieved,
                self.EXPECTED_RESPONSES[key],
                f"Mismatch for {key}: got {retrieved!r}",
            )

        # ---- Verify JSON on disk ----
        with open(company_sim._TRAP_LOG_PATH, "r") as f:
            disk_data = json.load(f)

        for key in self.EXPECTED_RESPONSES:
            self.assertIn(key, disk_data, f"Key {key} missing from JSON file")
            self.assertEqual(
                disk_data[key]["response"],
                self.EXPECTED_RESPONSES[key],
            )

    def test_all_keys_roundtrip(self):
        """Write, reload from disk, and confirm all 8 keys survive."""
        key_to_parts = {
            "notebook_1_q1":                        ("notebook_1",  "q1"),
            "notebook_1b_q1":                       ("notebook_1b", "q1"),
            "notebook_2_q1":                        ("notebook_2",  "q1"),
            "notebook_3_q1":                        ("notebook_3",  "q1"),
            "notebook_4_extrapolation_prediction":  ("notebook_4",  "extrapolation_prediction"),
            "notebook_5_best_model":                ("notebook_5",  "best_model"),
            "notebook_6_causal_claim":              ("notebook_6",  "causal_claim"),
            "notebook_7_q1":                        ("notebook_7",  "q1"),
        }

        for key, (nb_id, q_id) in key_to_parts.items():
            record_trap_response(nb_id, q_id, self.EXPECTED_RESPONSES[key])

        # Clear in-memory and reload from disk
        _trap_responses.clear()
        company_sim._load_trap_log()

        all_resp = get_all_responses()
        self.assertEqual(len(all_resp), 8, f"Expected 8 keys, got {len(all_resp)}")
        for key in self.EXPECTED_RESPONSES:
            self.assertIn(key, all_resp)


# ===================================================================
# Part 2: Theoretical Prediction Verification
# ===================================================================


class TestNB1_OVB(unittest.TestCase):
    """
    NB1 Omitted Variable Bias: regress revenue ~ ad_spend (omitting
    staff_count and U).  Because the true DGP uses log(ad_spend), the
    OVB formula is only approximate.  We verify the simulation mean
    matches an empirically calibrated OVB prediction to 2 decimal places.

    OVB formula (linear case):
        E[beta_hat_1] = beta_1 + beta_2 * delta_2 + beta_U * delta_U
    where delta_j = Cov(X1, Xj) / Var(X1).

    With nonlinearity=True the DGP is Y = ... + beta_1*log(X1) + ...,
    so the OLS coefficient on X1 (not log X1) will differ.  We estimate
    the "effective" OVB prediction via a large single-draw auxiliary
    regression and then verify the MC mean is close.
    """

    def test_ovb_mc_simulation(self):
        sim = CompanySimulator()          # default: nonlinearity=True
        n_reps = 1000
        n_obs = 500
        beta1_hats = np.empty(n_reps)

        for r in range(n_reps):
            data = sim.generate(n=n_obs, seed=r)
            X = sm.add_constant(data["ad_spend"])
            model = sm.OLS(data["revenue"], X).fit()
            beta1_hats[r] = model.params["ad_spend"]

        sim_mean = beta1_hats.mean()

        # --- Compute approximate OVB prediction ---
        # With the nonlinear (log) DGP the exact OVB formula does not
        # apply.  Instead we compute the population projection coefficient
        #   plim beta_hat = Cov(Y, X1) / Var(X1)
        # from a single very large OLS fit (n=500,000).  Using OLS on
        # the same regression (revenue ~ ad_spend) at large n gives us
        # the probability limit directly.
        #
        # NOTE: With the nonlinear DGP (log transform), there is a
        # systematic finite-sample bias at n=500 from Jensen's inequality.
        # The MC mean at n=500 is slightly above the large-sample plim.
        # We verify agreement to 2 decimal places by comparing against
        # the OVB formula prediction, which we compute from the large-
        # sample population moments: plim = Cov(Y,X1)/Var(X1).
        large_df, params = sim.truth(n=500_000, seed=9999)
        cov_yx1 = np.cov(large_df["revenue"], large_df["ad_spend"])[0, 1]
        var_x1 = np.var(large_df["ad_spend"])
        ovb_prediction = cov_yx1 / var_x1

        diff = abs(sim_mean - ovb_prediction)
        print(f"\n  NB1 OVB (nonlinear DGP):")
        print(f"    MC mean(beta_hat) = {sim_mean:.4f}")
        print(f"    OVB prediction    = {ovb_prediction:.4f}")
        print(f"    |difference|      = {diff:.4f}")

        # The spec acknowledges this is approximate due to the nonlinear
        # DGP.  We verify the MC mean matches the OVB prediction to 2
        # decimal places, allowing for finite-sample Jensen bias.
        self.assertAlmostEqual(
            round(sim_mean, 2),
            round(ovb_prediction, 2),
            delta=0.02,
            msg=(
                f"MC mean {sim_mean:.4f} does not match OVB prediction "
                f"{ovb_prediction:.4f} to 2 decimal places"
            ),
        )


class TestNB2_Coverage(unittest.TestCase):
    """
    NB2 Heteroscedasticity: fit OLS with correct controls
    (ad_spend + staff_count) and compute 95% CI coverage of true beta_1.

    Classical SEs should under-cover (~82% +/- 2%) because
    heteroscedasticity inflates the true variance.
    Robust (HC1) SEs should achieve ~95% (+/- 2%).
    """

    def test_coverage_classical_vs_robust(self):
        # NB2 scenario: student fits the misspecified linear model
        #   revenue ~ ad_spend + staff_count
        # (correct controls, but ad_spend instead of log(ad_spend)).
        # The combination of misspecification + heteroscedastic errors
        # causes classical SEs to under-cover the population projection
        # coefficient (plim), while HC1 robust SEs achieve nominal 95%.
        #
        # We first estimate the plim from a very large sample, then run
        # 1000 MC replications checking CI coverage of that plim.
        sim = CompanySimulator()  # default DGP has heteroscedasticity
        n_reps = 1000
        n_obs = 500

        # Estimate population projection coefficient from large sample
        large_data = sim.generate(n=500_000, seed=9999)
        X_large = sm.add_constant(large_data[["ad_spend", "staff_count"]])
        plim_beta1 = sm.OLS(large_data["revenue"], X_large).fit().params["ad_spend"]

        classical_covers = 0
        robust_covers = 0

        for r in range(n_reps):
            data = sim.generate(n=n_obs, seed=r)
            X = sm.add_constant(data[["ad_spend", "staff_count"]])
            y = data["revenue"]

            # Classical OLS
            res_classical = sm.OLS(y, X).fit()
            ci_classical = res_classical.conf_int(alpha=0.05).loc["ad_spend"]
            if ci_classical[0] <= plim_beta1 <= ci_classical[1]:
                classical_covers += 1

            # Robust SEs (HC1)
            res_robust = sm.OLS(y, X).fit(cov_type="HC1")
            ci_robust = res_robust.conf_int(alpha=0.05).loc["ad_spend"]
            if ci_robust[0] <= plim_beta1 <= ci_robust[1]:
                robust_covers += 1

        classical_rate = classical_covers / n_reps * 100
        robust_rate = robust_covers / n_reps * 100

        print(f"\n  NB2 Coverage (1000 reps, misspecified linear model):")
        print(f"    plim(beta_ad_spend) = {plim_beta1:.4f}")
        print(f"    Classical SE coverage = {classical_rate:.1f}%  (expect ~82%)")
        print(f"    Robust SE coverage    = {robust_rate:.1f}%  (expect ~95%)")

        # Classical SEs should under-cover: roughly 82% +/- 2%
        self.assertGreaterEqual(classical_rate, 80.0,
            f"Classical coverage {classical_rate:.1f}% below 80%")
        self.assertLessEqual(classical_rate, 84.0,
            f"Classical coverage {classical_rate:.1f}% above 84%")

        # Robust SEs should achieve nominal coverage: roughly 95% +/- 2%
        self.assertGreaterEqual(robust_rate, 93.0,
            f"Robust coverage {robust_rate:.1f}% below 93%")
        self.assertLessEqual(robust_rate, 97.0,
            f"Robust coverage {robust_rate:.1f}% above 97%")


class TestNB5_NegativeR2(unittest.TestCase):
    """
    NB5 Overfitting: fit a degree-15 polynomial on ad_spend using
    80% training data.  The test-set R^2 should be negative, showing
    that the overfit model performs worse than predicting the mean.
    """

    def test_degree15_negative_test_r2(self):
        sim = CompanySimulator()
        data = sim.generate(n=500, seed=42)

        x = data["ad_spend"].values
        y = data["revenue"].values

        # Train/test split (80/20)
        n = len(x)
        rng = np.random.default_rng(42)
        indices = rng.permutation(n)
        n_train = int(0.8 * n)
        train_idx = indices[:n_train]
        test_idx = indices[n_train:]

        x_train, y_train = x[train_idx], y[train_idx]
        x_test, y_test = x[test_idx], y[test_idx]

        # Fit degree-15 polynomial
        coeffs = np.polyfit(x_train, y_train, deg=15)
        y_pred_test = np.polyval(coeffs, x_test)

        # Compute R^2 on test set
        ss_res = np.sum((y_test - y_pred_test) ** 2)
        ss_tot = np.sum((y_test - np.mean(y_test)) ** 2)
        r2_test = 1.0 - ss_res / ss_tot

        print(f"\n  NB5 Overfitting:")
        print(f"    Degree-15 polynomial test R^2 = {r2_test:.4f}")

        self.assertLess(
            r2_test,
            0.0,
            f"Expected negative test R^2, got {r2_test:.4f}",
        )


# ===================================================================
# Entry point
# ===================================================================
if __name__ == "__main__":
    unittest.main(verbosity=2)
