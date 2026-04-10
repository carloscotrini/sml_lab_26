/**
 * company_sim.js — Shared DGP simulation module for Regression Autopsy
 *
 * DGP: Y = 50 + 8*log(X1) + 3*X2 + 2*U + eps
 *   U  ~ N(0,1)                     — unobserved neighborhood desirability
 *   X1 = 2.0 + 0.5*U + eta1         — living area (thousands of sqft)
 *   X2 = 3   + 0.5*U + eta2          — bedroom count
 *   X3 = 0.9*Y + eta3                — Zestimate (post-treatment)
 *   eps ~ N(0, 0.5*X1)               — heteroscedastic noise
 *   eta_i ~ N(0, sigma^2)            — independent noise
 */

// ============================================================
// Seeded PRNG — xorshift128
// ============================================================

export function seededRandom(seed) {
  let s = [seed | 0, (seed * 2654435761) | 0, (seed * 340573321) | 0, (seed * 1013904223) | 0];
  // Ensure non-zero state
  if (s[0] === 0 && s[1] === 0 && s[2] === 0 && s[3] === 0) s[0] = 1;

  function next() {
    let t = s[3];
    t ^= t << 11;
    t ^= t >>> 8;
    s[3] = s[2];
    s[2] = s[1];
    s[1] = s[0];
    t ^= s[0];
    t ^= s[0] >>> 19;
    s[0] = t;
    return (t >>> 0) / 4294967296;
  }

  // Warm up
  for (let i = 0; i < 20; i++) next();

  return next;
}

// ============================================================
// Box-Muller normal variate
// ============================================================

export function randn(rng) {
  let u1, u2;
  do { u1 = rng(); } while (u1 === 0);
  u2 = rng();
  return Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
}

// ============================================================
// Matrix utilities (for small matrices needed by OLS)
// ============================================================

function matTranspose(A, rows, cols) {
  const T = new Float64Array(cols * rows);
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      T[j * rows + i] = A[i * cols + j];
    }
  }
  return T;
}

function matMul(A, B, m, n, p) {
  // A is m x n, B is n x p, result is m x p
  const C = new Float64Array(m * p);
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < p; j++) {
      let sum = 0;
      for (let k = 0; k < n; k++) {
        sum += A[i * n + k] * B[k * p + j];
      }
      C[i * p + j] = sum;
    }
  }
  return C;
}

function matVecMul(A, x, m, n) {
  const y = new Float64Array(m);
  for (let i = 0; i < m; i++) {
    let sum = 0;
    for (let j = 0; j < n; j++) {
      sum += A[i * n + j] * x[j];
    }
    y[i] = sum;
  }
  return y;
}

/**
 * Invert a small square matrix using Gauss-Jordan elimination.
 * Returns null if singular.
 */
function matInvert(M, n) {
  // Build augmented matrix [M | I]
  const aug = new Float64Array(n * 2 * n);
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      aug[i * 2 * n + j] = M[i * n + j];
    }
    aug[i * 2 * n + n + i] = 1;
  }

  for (let col = 0; col < n; col++) {
    // Partial pivoting
    let maxVal = Math.abs(aug[col * 2 * n + col]);
    let maxRow = col;
    for (let row = col + 1; row < n; row++) {
      const v = Math.abs(aug[row * 2 * n + col]);
      if (v > maxVal) { maxVal = v; maxRow = row; }
    }
    if (maxVal < 1e-14) return null; // singular

    // Swap rows
    if (maxRow !== col) {
      for (let j = 0; j < 2 * n; j++) {
        const tmp = aug[col * 2 * n + j];
        aug[col * 2 * n + j] = aug[maxRow * 2 * n + j];
        aug[maxRow * 2 * n + j] = tmp;
      }
    }

    // Scale pivot row
    const pivot = aug[col * 2 * n + col];
    for (let j = 0; j < 2 * n; j++) {
      aug[col * 2 * n + j] /= pivot;
    }

    // Eliminate column
    for (let row = 0; row < n; row++) {
      if (row === col) continue;
      const factor = aug[row * 2 * n + col];
      for (let j = 0; j < 2 * n; j++) {
        aug[row * 2 * n + j] -= factor * aug[col * 2 * n + j];
      }
    }
  }

  // Extract inverse
  const inv = new Float64Array(n * n);
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      inv[i * n + j] = aug[i * 2 * n + n + j];
    }
  }
  return inv;
}

// ============================================================
// OLS — Ordinary Least Squares
// ============================================================

/**
 * Fit OLS: y = X * beta + residuals.
 * @param {Float64Array|number[]} y  — response vector (length n)
 * @param {Float64Array|number[]} X  — design matrix, FLAT row-major (n x p)
 *        Caller must include an intercept column if desired.
 * @param {number} [p]              — number of columns in X (auto-detected if X is 2D array)
 * @returns {{ coefficients, se, tStats, pValues, r2, residuals }}
 */
export function ols(y, X, p) {
  const n = y.length;
  if (!p) {
    // If X is an array of arrays, flatten
    if (Array.isArray(X) && Array.isArray(X[0])) {
      p = X[0].length;
      const flat = new Float64Array(n * p);
      for (let i = 0; i < n; i++) {
        for (let j = 0; j < p; j++) flat[i * p + j] = X[i][j];
      }
      X = flat;
    } else {
      p = X.length / n;
    }
  }
  const Xf = (X instanceof Float64Array) ? X : new Float64Array(X);
  const yf = (y instanceof Float64Array) ? y : new Float64Array(y);

  // X'X
  const Xt = matTranspose(Xf, n, p);
  const XtX = matMul(Xt, Xf, p, n, p);

  // (X'X)^{-1}
  const XtXinv = matInvert(XtX, p);
  if (!XtXinv) {
    throw new Error("OLS: X'X is singular — check for perfect collinearity.");
  }

  // X'y
  const Xty = matVecMul(Xt, yf, p, n);

  // beta = (X'X)^{-1} X'y
  const beta = matVecMul(XtXinv, Xty, p, p);

  // residuals
  const yhat = matVecMul(Xf, beta, n, p);
  const residuals = new Float64Array(n);
  let ssr = 0;
  for (let i = 0; i < n; i++) {
    residuals[i] = yf[i] - yhat[i];
    ssr += residuals[i] * residuals[i];
  }

  // sigma^2 = SSR / (n - p)
  const sigma2 = ssr / (n - p);

  // SE = sqrt(diag(sigma^2 * (X'X)^{-1}))
  const se = new Float64Array(p);
  for (let j = 0; j < p; j++) {
    se[j] = Math.sqrt(sigma2 * XtXinv[j * p + j]);
  }

  // t-stats & p-values (two-sided, using normal approx for large n)
  const tStats = new Float64Array(p);
  const pValues = new Float64Array(p);
  for (let j = 0; j < p; j++) {
    tStats[j] = beta[j] / se[j];
    // Normal CDF approximation for |t| (good for n > 30)
    pValues[j] = 2 * (1 - normalCDF(Math.abs(tStats[j])));
  }

  // R-squared
  let yMean = 0;
  for (let i = 0; i < n; i++) yMean += yf[i];
  yMean /= n;
  let sst = 0;
  for (let i = 0; i < n; i++) sst += (yf[i] - yMean) ** 2;
  const r2 = 1 - ssr / sst;

  return {
    coefficients: Array.from(beta),
    se: Array.from(se),
    tStats: Array.from(tStats),
    pValues: Array.from(pValues),
    r2,
    residuals: Array.from(residuals),
  };
}

/** Standard normal CDF approximation (Abramowitz & Stegun) */
function normalCDF(x) {
  const a1 = 0.254829592, a2 = -0.284496736, a3 = 1.421413741;
  const a4 = -1.453152027, a5 = 1.061405429, p = 0.3275911;
  const sign = x < 0 ? -1 : 1;
  x = Math.abs(x) / Math.SQRT2;
  const t = 1 / (1 + p * x);
  const y = 1 - ((((a5 * t + a4) * t + a3) * t + a2) * t + a1) * t * Math.exp(-x * x);
  return 0.5 * (1 + sign * y);
}

// ============================================================
// CompanySimulator — Data Generating Process
// ============================================================

export class CompanySimulator {
  /**
   * @param {Object} opts — pathology strength parameters
   * @param {number} opts.sigma_eta — std dev of independent noise terms (default 0.5)
   * @param {number} opts.confound_strength — coefficient on U in X1, X2 equations (default 0.5)
   * @param {number} opts.hetero_scale — scale of heteroscedastic noise (default 0.5)
   * @param {number} opts.post_treatment_weight — weight of Y in Zestimate (default 0.9)
   */
  constructor(opts = {}) {
    this.sigma_eta = opts.sigma_eta ?? 0.5;
    this.confound_strength = opts.confound_strength ?? 0.5;
    this.hetero_scale = opts.hetero_scale ?? 0.5;
    this.post_treatment_weight = opts.post_treatment_weight ?? 0.9;
  }

  /**
   * Generate n observations from the DGP.
   * @param {number} n    — sample size
   * @param {number} seed — PRNG seed for reproducibility
   * @returns {Array<{sale_price: number, living_area: number, bedrooms: number, zestimate: number, desirability_U: number}>}
   */
  generate(n = 500, seed = 42) {
    const rng = seededRandom(seed);
    const data = [];

    for (let i = 0; i < n; i++) {
      // Unobserved confounder
      const U = randn(rng);

      // Observed covariates
      const eta1 = this.sigma_eta * randn(rng);
      const eta2 = this.sigma_eta * randn(rng);
      const X1 = 2.0 + this.confound_strength * U + eta1; // living area
      const X2 = 3 + this.confound_strength * U + eta2;   // bedrooms

      // Heteroscedastic error
      const eps = this.hetero_scale * Math.abs(X1) * randn(rng);

      // Outcome
      const Y = 50 + 8 * Math.log(Math.max(X1, 0.01)) + 3 * X2 + 2 * U + eps;

      // Post-treatment variable
      const eta3 = this.sigma_eta * randn(rng);
      const X3 = this.post_treatment_weight * Y + eta3; // Zestimate

      data.push({
        sale_price: Y,
        living_area: X1,
        bedrooms: X2,
        zestimate: X3,
        desirability_U: U,
      });
    }

    return data;
  }

  /**
   * Returns the true DGP parameters.
   */
  truth() {
    return {
      beta_log_x1: 8,
      beta_x2: 3,
      beta_u: 2,
      intercept: 50,
    };
  }
}

// ============================================================
// MonteCarloEngine
// ============================================================

export class MonteCarloEngine {
  /**
   * Run Monte Carlo replications of an estimator across parameter settings.
   *
   * @param {Function} estimatorFn — function(data, params) => {estimate: number, ...}
   *        where data comes from CompanySimulator.generate()
   * @param {Array<Object>} paramGrid — array of parameter setting objects,
   *        each passed to estimatorFn and used to configure CompanySimulator
   * @param {number} nReps — number of Monte Carlo replications per setting
   * @returns {Array<{params: Object, results: Array, summary: {mean, std, bias, mse, ci95}}>}
   */
  run(estimatorFn, paramGrid, nReps = 2000) {
    const output = [];

    for (const params of paramGrid) {
      const sim = new CompanySimulator(params.simOpts || {});
      const estimates = [];

      for (let rep = 0; rep < nReps; rep++) {
        const data = sim.generate(params.n || 500, rep + 1);
        try {
          const result = estimatorFn(data, params);
          estimates.push(result.estimate);
        } catch {
          // Skip failed replications
        }
      }

      // Summary statistics
      const m = estimates.length;
      if (m === 0) {
        output.push({ params, results: [], summary: null });
        continue;
      }

      const mean = estimates.reduce((a, b) => a + b, 0) / m;
      const variance = estimates.reduce((a, b) => a + (b - mean) ** 2, 0) / (m - 1);
      const std = Math.sqrt(variance);

      const trueValue = params.trueValue ?? 0;
      const bias = mean - trueValue;
      const mse = estimates.reduce((a, b) => a + (b - trueValue) ** 2, 0) / m;

      // 95% CI from empirical quantiles
      const sorted = [...estimates].sort((a, b) => a - b);
      const ci95 = [
        sorted[Math.floor(0.025 * m)],
        sorted[Math.floor(0.975 * m)],
      ];

      output.push({
        params,
        results: estimates,
        summary: { mean, std, bias, mse, ci95 },
      });
    }

    return output;
  }
}
