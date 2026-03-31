"""
company_sim.py — Shared infrastructure for the Regression Autopsy course.
Embedded in every notebook's setup cell. Self-contained, no external deps
beyond numpy, pandas, matplotlib, statsmodels, ipywidgets.
"""

import json
import os
from datetime import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.stattools import durbin_watson, jarque_bera
from statsmodels.stats.outliers_influence import variance_inflation_factor, OLSInfluence

import ipywidgets as widgets

# ---------------------------------------------------------------------------
# Color constants — consistent across all notebooks
# ---------------------------------------------------------------------------
COLORS = {
    'ols': '#2E5EA8',       # Blue — OLS estimator
    'truth': '#D4A017',     # Gold — true parameter
    'bias': '#C0392B',      # Red — bias/violation/error
    'repair': '#27AE60',    # Green — repair working
    'alt': '#7F8C8D',       # Gray — alternative estimators
}

# ---------------------------------------------------------------------------
# Gate System — module-level trap response storage
# ---------------------------------------------------------------------------
_trap_responses = {}
_TRAP_LOG_PATH = '/content/trap_log.json'


def _load_trap_log():
    """Load existing trap log from disk into memory."""
    global _trap_responses
    if os.path.exists(_TRAP_LOG_PATH):
        try:
            with open(_TRAP_LOG_PATH, 'r') as f:
                _trap_responses = json.load(f)
        except (json.JSONDecodeError, IOError):
            _trap_responses = {}


def _save_trap_log():
    """Persist in-memory trap responses to disk."""
    try:
        os.makedirs(os.path.dirname(_TRAP_LOG_PATH), exist_ok=True)
        with open(_TRAP_LOG_PATH, 'w') as f:
            json.dump(_trap_responses, f, indent=2)
    except IOError:
        pass  # Silently fail if /content not available (local dev)


def record_trap_response(notebook_id, question_id, response):
    """Save a trap response to the log."""
    key = f"{notebook_id}_{question_id}"
    _trap_responses[key] = {
        "response": response,
        "timestamp": datetime.now().isoformat(),
    }
    _save_trap_log()


def get_trap_response(notebook_id, question_id):
    """Retrieve a previously recorded trap response, or None."""
    key = f"{notebook_id}_{question_id}"
    entry = _trap_responses.get(key)
    return entry["response"] if entry else None


def check_gate(notebook_id, question_id):
    """Return True if a response has been recorded for this gate."""
    key = f"{notebook_id}_{question_id}"
    return key in _trap_responses


def get_all_responses():
    """Return all recorded trap responses."""
    return dict(_trap_responses)


def create_trap_widget(notebook_id, question_id, question_text, options):
    """Create a radio-button trap widget with submit button and gate logic."""
    label = widgets.HTML(f"<b>{question_text}</b>")
    radio = widgets.RadioButtons(
        options=options,
        value=None,
        layout=widgets.Layout(width='auto'),
    )
    submit = widgets.Button(description="Submit", button_style='primary')
    output = widgets.Output()

    def on_submit(btn):
        with output:
            output.clear_output()
            if radio.value is None:
                print("Please select an option before submitting.")
                return
            record_trap_response(notebook_id, question_id, radio.value)
            print(f"Response recorded: {radio.value}")
            submit.disabled = True
            radio.disabled = True

    submit.on_click(on_submit)

    # Pre-fill if already answered
    existing = get_trap_response(notebook_id, question_id)
    if existing is not None:
        try:
            radio.value = existing
            radio.disabled = True
            submit.disabled = True
        except Exception:
            pass

    return widgets.VBox([label, radio, submit, output])


# Load any existing responses at import time
_load_trap_log()


# ---------------------------------------------------------------------------
# CompanySimulator — NovaMart data generating process
# ---------------------------------------------------------------------------
class CompanySimulator:
    """
    Generates simulated NovaMart data with controllable pathologies:
    omitted variable bias, heteroscedasticity, nonlinearity, bad controls.
    """

    def __init__(
        self,
        endogeneity_strength=20,
        heteroscedasticity_strength=0.5,
        nonlinearity=True,
        bad_control_strength=0.1,
        noise_sigma=1.0,
    ):
        self.endogeneity_strength = endogeneity_strength
        self.heteroscedasticity_strength = heteroscedasticity_strength
        self.nonlinearity = nonlinearity
        self.bad_control_strength = bad_control_strength
        self.noise_sigma = noise_sigma

        # True DGP parameters
        self.beta_0 = 50
        self.beta_1 = 8      # coefficient on log(X1) or X1
        self.beta_2 = 3      # coefficient on X2
        self.beta_U = 2      # coefficient on U
        self.staff_loading = 5  # U -> X2 coefficient

    def generate(self, n=500, seed=42):
        """Generate observed data: revenue, ad_spend, staff_count, satisfaction."""
        rng = np.random.default_rng(seed)

        # Step 1: Generate U, noise terms, epsilon base
        U = rng.standard_normal(n)
        eta1 = rng.normal(0, self.noise_sigma, n)
        eta2 = rng.normal(0, self.noise_sigma, n)
        eta3 = rng.normal(0, self.noise_sigma, n)

        # Step 2: X1, X2 from U
        X1 = self.endogeneity_strength * U + eta1
        if self.nonlinearity:
            X1 = np.abs(X1) + 0.01  # Ensure positive for log
        X2 = self.staff_loading * U + eta2

        # Step 3: Compute Y
        # Heteroscedastic errors: eps ~ N(0, h * X1)
        eps_std = np.sqrt(np.abs(self.heteroscedasticity_strength * X1))
        eps = rng.normal(0, eps_std)

        if self.nonlinearity:
            Y = self.beta_0 + self.beta_1 * np.log(X1) + self.beta_2 * X2 + self.beta_U * U + eps
        else:
            Y = self.beta_0 + self.beta_1 * X1 + self.beta_2 * X2 + self.beta_U * U + eps

        # Step 4: X3 from Y (post-treatment / bad control)
        X3 = self.bad_control_strength * Y + eta3

        return pd.DataFrame({
            'revenue': Y,
            'ad_spend': X1,
            'staff_count': X2,
            'satisfaction': X3,
        })

    def truth(self, n=500, seed=42):
        """Generate data including hidden demand_U + return true parameter dict."""
        rng = np.random.default_rng(seed)

        U = rng.standard_normal(n)
        eta1 = rng.normal(0, self.noise_sigma, n)
        eta2 = rng.normal(0, self.noise_sigma, n)
        eta3 = rng.normal(0, self.noise_sigma, n)

        X1 = self.endogeneity_strength * U + eta1
        if self.nonlinearity:
            X1 = np.abs(X1) + 0.01
        X2 = self.staff_loading * U + eta2

        eps_std = np.sqrt(np.abs(self.heteroscedasticity_strength * X1))
        eps = rng.normal(0, eps_std)

        if self.nonlinearity:
            Y = self.beta_0 + self.beta_1 * np.log(X1) + self.beta_2 * X2 + self.beta_U * U + eps
        else:
            Y = self.beta_0 + self.beta_1 * X1 + self.beta_2 * X2 + self.beta_U * U + eps

        X3 = self.bad_control_strength * Y + eta3

        df = pd.DataFrame({
            'revenue': Y,
            'ad_spend': X1,
            'staff_count': X2,
            'satisfaction': X3,
            'demand_U': U,
        })

        params = {
            'beta_0': self.beta_0,
            'beta_1': self.beta_1,
            'beta_2': self.beta_2,
            'beta_U': self.beta_U,
            'sigma_epsilon': self.heteroscedasticity_strength,
        }

        return df, params

    def dgp_summary(self):
        """Return LaTeX specification string."""
        func = r"\log(X_1)" if self.nonlinearity else r"X_1"
        return (
            rf"$Y = {self.beta_0} + {self.beta_1} \cdot {func} "
            rf"+ {self.beta_2} \cdot X_2 + {self.beta_U} \cdot U + \varepsilon$"
            "\n\nWhere:\n"
            rf"- $U \sim N(0, 1)$ (unobserved market demand)"
            "\n"
            rf"- $X_1 = {self.endogeneity_strength} \cdot U + \eta_1$ (ad spend)"
            "\n"
            rf"- $X_2 = {self.staff_loading} \cdot U + \eta_2$ (staff count)"
            "\n"
            rf"- $X_3 = {self.bad_control_strength} \cdot Y + \eta_3$ (satisfaction, post-treatment)"
            "\n"
            rf"- $\varepsilon \sim N(0, {self.heteroscedasticity_strength} \cdot X_1)$"
            "\n"
            rf"- $\eta_i \sim N(0, {self.noise_sigma}^2)$"
        )

    def set_heteroscedasticity(self, strength):
        """Update heteroscedasticity strength."""
        self.heteroscedasticity_strength = strength

    def set_endogeneity(self, strength):
        """Update endogeneity strength (U -> X1 coefficient)."""
        self.endogeneity_strength = strength

    def set_nonlinearity(self, curvature):
        """Toggle or adjust nonlinearity. Pass bool or truthy value."""
        self.nonlinearity = bool(curvature)


# ---------------------------------------------------------------------------
# MonteCarloEngine — precompute simulation results for interactive sliders
# ---------------------------------------------------------------------------
class MonteCarloEngine:
    """Precomputes Monte Carlo draws across a parameter grid."""

    def run(self, estimator_fn, param_name, param_grid, simulator,
            n_reps=5000, n_obs=500):
        """
        For each value in param_grid, set param on simulator, run n_reps
        replications, collect estimator_fn output.

        Returns numpy array of shape (len(param_grid), n_reps).
        """
        results = np.empty((len(param_grid), n_reps))

        # Progress bar
        try:
            progress = widgets.IntProgress(
                value=0, min=0, max=len(param_grid),
                description='Simulating:', style={'description_width': 'initial'},
            )
            from IPython.display import display
            display(progress)
            use_widget = True
        except Exception:
            use_widget = False

        setter = getattr(simulator, f'set_{param_name}', None)

        for i, val in enumerate(param_grid):
            if setter is not None:
                setter(val)
            for r in range(n_reps):
                data = simulator.generate(n=n_obs, seed=r)
                results[i, r] = estimator_fn(data)
            if use_widget:
                progress.value = i + 1
            else:
                print(f"  [{i+1}/{len(param_grid)}] {param_name}={val:.3f}")

        if use_widget:
            progress.bar_style = 'success'

        return results

    def quick_run(self, estimator_fn, dgp_fn, n_reps=1000, n_obs=500):
        """
        Single-configuration simulation for sidebar mini-sims.
        dgp_fn(seed, n) -> DataFrame. No caching.
        """
        results = np.empty(n_reps)
        for r in range(n_reps):
            data = dgp_fn(seed=r, n=n_obs)
            results[r] = estimator_fn(data)
        return results


# ---------------------------------------------------------------------------
# DiagnosticSuite — standardized diagnostic visualizations
# ---------------------------------------------------------------------------
class DiagnosticSuite:
    """Produces four-panel residual diagnostics and summary test statistics."""

    @staticmethod
    def run_diagnostics(model_result):
        """
        2x2 diagnostic plot grid from a statsmodels OLS results object.
        Returns the matplotlib Figure.
        """
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))

        influence = OLSInfluence(model_result)
        fitted = model_result.fittedvalues
        resid = model_result.resid
        std_resid = influence.resid_studentized_internal

        # Top-left: Residuals vs Fitted
        ax = axes[0, 0]
        ax.scatter(fitted, resid, alpha=0.4, s=15, color=COLORS['ols'])
        ax.axhline(0, color=COLORS['truth'], linewidth=1.5)
        ax.set_xlabel('Fitted values')
        ax.set_ylabel('Residuals')
        ax.set_title('Residuals vs Fitted')

        # Top-right: QQ plot
        ax = axes[0, 1]
        stats.probplot(resid, dist="norm", plot=ax)
        ax.set_title('Normal Q-Q')
        ax.get_lines()[0].set_color(COLORS['ols'])
        ax.get_lines()[1].set_color(COLORS['bias'])

        # Bottom-left: Scale-Location
        ax = axes[1, 0]
        sqrt_abs_std = np.sqrt(np.abs(std_resid))
        ax.scatter(fitted, sqrt_abs_std, alpha=0.4, s=15, color=COLORS['ols'])
        ax.set_xlabel('Fitted values')
        ax.set_ylabel(r'$\sqrt{|Standardized\ Residuals|}$')
        ax.set_title('Scale-Location')

        # Bottom-right: Residuals vs Leverage
        ax = axes[1, 1]
        leverage = influence.hat_matrix_diag
        cooks_d = influence.cooks_distance[0]
        ax.scatter(leverage, std_resid, alpha=0.4, s=15, color=COLORS['ols'])
        ax.axhline(0, color=COLORS['truth'], linewidth=1)
        ax.set_xlabel('Leverage')
        ax.set_ylabel('Standardized Residuals')
        ax.set_title("Residuals vs Leverage")

        # Cook's distance contours
        x_range = np.linspace(0.001, ax.get_xlim()[1], 100)
        for cook_val in [0.5, 1.0]:
            for sign in [1, -1]:
                p = model_result.df_model + 1
                y_val = sign * np.sqrt(cook_val * p * (1 - x_range) / x_range)
                ax.plot(x_range, y_val, '--', color=COLORS['bias'],
                        alpha=0.5, label=f"Cook's d={cook_val}" if sign == 1 else None)
        ax.legend(fontsize=8)

        fig.tight_layout()
        return fig

    @staticmethod
    def summary_tests(model_result):
        """
        Return dict of diagnostic test results:
        vif, breusch_pagan, durbin_watson, jarque_bera.
        """
        results = {}

        # VIF — requires exog with constant
        exog = model_result.model.exog
        exog_names = model_result.model.exog_names
        vif_dict = {}
        for i, name in enumerate(exog_names):
            if name == 'const':
                continue
            vif_dict[name] = variance_inflation_factor(exog, i)
        results['vif'] = vif_dict

        # Breusch-Pagan
        bp_stat, bp_pval, _, _ = het_breuschpagan(
            model_result.resid, model_result.model.exog
        )
        results['breusch_pagan'] = (bp_stat, bp_pval)

        # Durbin-Watson
        results['durbin_watson'] = durbin_watson(model_result.resid)

        # Jarque-Bera
        jb_stat, jb_pval, _, _ = jarque_bera(model_result.resid)
        results['jarque_bera'] = (jb_stat, jb_pval)

        return results


# ---------------------------------------------------------------------------
# AutopsyReport — widget factory for structured reflection
# ---------------------------------------------------------------------------
class AutopsyReport:
    """Creates reflection widgets for notebook wrap-up cells."""

    @staticmethod
    def lightweight(notebook_number):
        """Two-question mini autopsy for Notebooks 3-6."""
        threat = widgets.Text(
            description='Biggest threat:',
            placeholder='What is the biggest threat to this estimate?',
            layout=widgets.Layout(width='90%'),
            style={'description_width': '120px'},
        )
        check = widgets.Text(
            description='How to check:',
            placeholder='How would you check if that threat is real?',
            layout=widgets.Layout(width='90%'),
            style={'description_width': '120px'},
        )
        submit = widgets.Button(description='Save Autopsy', button_style='primary')
        output = widgets.Output()

        def on_submit(btn):
            with output:
                output.clear_output()
                nb_id = f"notebook_{notebook_number}"
                record_trap_response(nb_id, "threat", threat.value)
                record_trap_response(nb_id, "check", check.value)
                print("Autopsy responses saved.")
                submit.disabled = True

        submit.on_click(on_submit)
        return widgets.VBox([
            widgets.HTML(f"<h3>Mini Autopsy — Notebook {notebook_number}</h3>"),
            threat, check, submit, output
        ])

    @staticmethod
    def full(notebook_number, available_sidebars=None):
        """Full sensitivity-analysis autopsy for Notebooks 7-8."""
        fields = {
            'point_estimate': widgets.Text(
                description='Point estimate:',
                placeholder='My point estimate is:',
                layout=widgets.Layout(width='90%'),
                style={'description_width': '150px'},
            ),
            'robustness': widgets.Text(
                description='Robustness value:',
                placeholder='The robustness value is:',
                layout=widgets.Layout(width='90%'),
                style={'description_width': '150px'},
            ),
            'partial_r2': widgets.Text(
                description='Strongest partial R²:',
                placeholder='The strongest observed covariate has partial R² of:',
                layout=widgets.Layout(width='90%'),
                style={'description_width': '150px'},
            ),
            'plain_language': widgets.Text(
                description='Plain language:',
                placeholder='An omitted variable would need to be ___ times as important as ___ to explain away this result',
                layout=widgets.Layout(width='90%'),
                style={'description_width': '150px'},
            ),
        }

        children = [
            widgets.HTML(f"<h3>Full Autopsy Report — Notebook {notebook_number}</h3>"),
        ]
        children.extend(fields.values())

        if available_sidebars:
            sidebar_dropdown = widgets.Dropdown(
                options=['(select)'] + list(available_sidebars),
                description='Most analogous disaster:',
                layout=widgets.Layout(width='90%'),
                style={'description_width': '180px'},
            )
            children.append(sidebar_dropdown)
            fields['analogous_disaster'] = sidebar_dropdown

        submit = widgets.Button(description='Save Autopsy', button_style='primary')
        output = widgets.Output()

        def on_submit(btn):
            with output:
                output.clear_output()
                nb_id = f"notebook_{notebook_number}"
                for key, w in fields.items():
                    record_trap_response(nb_id, key, w.value)
                print("Full autopsy report saved.")
                submit.disabled = True

        submit.on_click(on_submit)
        children.extend([submit, output])
        return widgets.VBox(children)
