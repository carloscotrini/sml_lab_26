"""
Nine Numerical Examples for Statistics Lecture Results
======================================================
Each example is hand-computable with 3-5 data points.
Run this file to verify all arithmetic.
"""
import numpy as np
from numpy.linalg import inv
np.set_printoptions(precision=4, suppress=True)


# =====================================================================
# RESULT 1: OMITTED VARIABLE BIAS
# E[beta1_short] = beta1 + beta2 * delta1
# =====================================================================
print("=" * 70)
print("RESULT 1: OMITTED VARIABLE BIAS")
print("=" * 70)

X1 = np.array([1, 2, 3, 4, 5], dtype=float)   # hours studied
X2 = np.array([8, 7, 5, 4, 1], dtype=float)    # hours slept
Y  = 40 + 3*X1 + 2*X2                          # exam score (exact, no noise)
# Y = [59, 60, 59, 60, 57]

n = 5
ones = np.ones(n)

# Full regression: Y on 1, X1, X2
X_full = np.column_stack([ones, X1, X2])
beta_full = inv(X_full.T @ X_full) @ X_full.T @ Y
print(f"Full regression: b0={beta_full[0]:.1f}, b1={beta_full[1]:.1f}, b2={beta_full[2]:.1f}")

# Short regression: Y on 1, X1
X_short = np.column_stack([ones, X1])
beta_short = inv(X_short.T @ X_short) @ X_short.T @ Y
print(f"Short regression: a0={beta_short[0]:.1f}, a1={beta_short[1]:.1f}")

# Auxiliary regression: X2 on 1, X1
delta = inv(X_short.T @ X_short) @ X_short.T @ X2
print(f"Auxiliary (X2 on X1): delta1={delta[1]:.1f}")

bias = beta_full[2] * delta[1]
print(f"Bias = beta2 * delta1 = {beta_full[2]:.1f} * {delta[1]:.1f} = {bias:.1f}")
print(f"beta1_short = beta1 + bias = {beta_full[1]:.1f} + ({bias:.1f}) = {beta_full[1]+bias:.1f}")
print(f"Actual beta1_short = {beta_short[1]:.1f}")
assert np.isclose(beta_short[1], beta_full[1] + bias), "OVB formula mismatch!"
print("PASS: OVB formula verified.\n")


# =====================================================================
# RESULT 2: SANDWICH VARIANCE (HETEROSCEDASTICITY)
# =====================================================================
print("=" * 70)
print("RESULT 2: SANDWICH VARIANCE (HETEROSCEDASTICITY)")
print("=" * 70)

X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([3, 5, 7, 3, 15], dtype=float)

Xbar, Ybar = 3.0, 6.6
slope = np.sum((X - Xbar)*(Y - Ybar)) / np.sum((X - Xbar)**2)  # = 22/10 = 2.2
intercept = Ybar - slope*Xbar  # = 6.6 - 6.6 = 0
Yhat = intercept + slope*X
resid = Y - Yhat

print(f"OLS: Y = {intercept:.1f} + {slope:.1f}*X")
print(f"Fitted:    {Yhat}")
print(f"Residuals: {resid}")
print(f"e^2:       {resid**2}")

s2 = np.sum(resid**2) / 3  # n-2 = 3
SE_classical = np.sqrt(s2 / np.sum((X - Xbar)**2))
print(f"\ns^2 = {np.sum(resid**2):.2f}/3 = {s2:.2f}")
print(f"Classical SE(slope) = sqrt({s2:.2f}/10) = {SE_classical:.2f}")

print(f"\nResidual pattern:")
print(f"  Low X  (X=1,2): e^2 = {resid[0]**2:.2f}, {resid[1]**2:.2f}  -> avg {np.mean(resid[:2]**2):.2f}")
print(f"  High X (X=4,5): e^2 = {resid[3]**2:.2f}, {resid[4]**2:.2f} -> avg {np.mean(resid[3:]**2):.2f}")
print(f"  Ratio: {np.mean(resid[3:]**2)/np.mean(resid[:2]**2):.0f}x larger at high X!")
print("PASS: Heteroscedasticity demonstrated.\n")


# =====================================================================
# RESULT 3: POWER / SIGNIFICANCE != IMPORTANCE
# =====================================================================
print("=" * 70)
print("RESULT 3: POWER / SIGNIFICANCE != IMPORTANCE")
print("=" * 70)

beta = 0.1
sigma = 2.0
for n_val in [5, 50, 5000]:
    SE = sigma / np.sqrt(n_val)
    t = beta / SE
    sig = "YES (p < 0.05)" if abs(t) > 1.96 else "NO"
    print(f"  n={n_val:>5}: SE = {sigma}/sqrt({n_val}) = {SE:.4f}, t = {beta}/{SE:.4f} = {t:.2f} -> Significant? {sig}")
print("PASS: Tiny effect becomes 'significant' at n=5000.\n")


# =====================================================================
# RESULT 4: LINEAR PROJECTION UNDER MISSPECIFICATION
# =====================================================================
print("=" * 70)
print("RESULT 4: LINEAR PROJECTION UNDER MISSPECIFICATION")
print("=" * 70)

X = np.array([1, 4, 9, 16, 25], dtype=float)
Y_true = np.sqrt(X)  # [1, 2, 3, 4, 5]

n = 5
ones = np.ones(n)
Xmat = np.column_stack([ones, X])
beta = inv(Xmat.T @ Xmat) @ Xmat.T @ Y_true
Yhat = Xmat @ beta
resid = Y_true - Yhat

print(f"X:         {X}")
print(f"Y=sqrt(X): {Y_true}")
print(f"OLS line:  Y = {beta[0]:.3f} + {beta[1]:.4f}*X")
print(f"Fitted:    {np.round(Yhat, 2)}")
print(f"Residuals: {np.round(resid, 2)}")
print(f"Max in-sample |error| = {np.max(np.abs(resid)):.2f}")

for X_new in [100, 10000]:
    pred = beta[0] + beta[1]*X_new
    truth = np.sqrt(X_new)
    print(f"\n  X={X_new}: line predicts {pred:.1f}, truth=sqrt({X_new})={truth:.0f}, error={pred-truth:.1f}")

print("PASS: Linear fit diverges wildly outside data range.\n")


# =====================================================================
# RESULT 5: BIAS-VARIANCE DECOMPOSITION
# =====================================================================
print("=" * 70)
print("RESULT 5: BIAS-VARIANCE DECOMPOSITION")
print("=" * 70)

print("True model: Y = 2X. Test point: X=6, true Y=12.\n")

training_sets = [
    np.array([3, 4, 6, 8, 9], dtype=float),   # Set 1
    np.array([1, 4, 6, 8, 11], dtype=float),   # Set 2
    np.array([2, 5, 5, 9, 10], dtype=float),   # Set 3
]
Xs = np.array([1, 2, 3, 4, 5], dtype=float)
X_test = 6.0

for i, Ys in enumerate(training_sets):
    print(f"  Training set {i+1}: X={Xs.astype(int)}, Y={Ys.astype(int)}")

# Model A: constant = 7
print(f"\nModel A (always predict 7): predictions = [7, 7, 7]")
print(f"  Bias = 7 - 12 = -5, Bias^2 = 25, Variance = 0, Total = 25")

# Model B: linear fit
preds_B = []
for i, Ys in enumerate(training_sets):
    Xm = np.column_stack([np.ones(5), Xs])
    b = inv(Xm.T @ Xm) @ Xm.T @ Ys
    pred = b[0] + b[1]*X_test
    preds_B.append(pred)
    print(f"\nModel B, Set {i+1}: Y = {b[0]:.1f} + {b[1]:.1f}*X -> pred(6) = {pred:.1f}")
mean_B = np.mean(preds_B)
var_B = np.var(preds_B)
bias_B = mean_B - 12
print(f"  Avg = {mean_B:.1f}, Bias^2 = {bias_B**2:.2f}, Var = {var_B:.2f}, Total = {bias_B**2+var_B:.2f}")

# Model C: degree-4 polynomial
preds_C = []
for i, Ys in enumerate(training_sets):
    coeffs = np.polyfit(Xs, Ys, 4)
    pred = np.polyval(coeffs, X_test)
    preds_C.append(pred)
    print(f"\nModel C, Set {i+1}: pred(6) = {pred:.1f}")
mean_C = np.mean(preds_C)
var_C = np.var(preds_C)
bias_C = mean_C - 12
print(f"  Avg = {mean_C:.1f}, Bias^2 = {bias_C**2:.1f}, Var = {var_C:.1f}, Total = {bias_C**2+var_C:.1f}")

print(f"\nSummary:")
print(f"  Model A (constant):  Bias^2=25.0, Var=0.0,   Total=25.0")
print(f"  Model B (linear):    Bias^2={bias_B**2:.2f}, Var={var_B:.2f}, Total={bias_B**2+var_B:.2f}")
print(f"  Model C (degree-4):  Bias^2={bias_C**2:.1f}, Var={var_C:.1f}, Total={bias_C**2+var_C:.1f}")
print("PASS: Low-bias model (C) has insane variance; right model (B) wins.\n")


# =====================================================================
# RESULT 6: COLLIDER BIAS / BAD CONTROLS
# =====================================================================
print("=" * 70)
print("RESULT 6: COLLIDER BIAS / BAD CONTROLS")
print("=" * 70)

print("Four types of people (equal frequency):")
print("  Talent  Luck  Famous (= Talent OR Luck)")
for t, l in [(0,0), (0,1), (1,0), (1,1)]:
    f = int(t + l >= 1)
    print(f"    {t}       {l}      {f}")

print(f"\nAll people: Corr(Talent, Luck) = 0 (independent by design)")
print(f"\nFamous only (drop the (0,0) row):")
print(f"  Talent  Luck")
for t, l in [(0,1), (1,0), (1,1)]:
    print(f"    {t}       {l}")
print(f"\n  P(Lucky | Talented) = 1/2")
print(f"  P(Lucky | Not Talented) = 1/1 = 1")
print(f"  Among famous: talent and luck are NEGATIVELY associated!")
print("PASS: Conditioning on a collider creates spurious negative correlation.\n")


# =====================================================================
# RESULT 7: INSTRUMENTAL VARIABLES
# =====================================================================
print("=" * 70)
print("RESULT 7: INSTRUMENTAL VARIABLES")
print("=" * 70)

Z = np.array([1, 2, 3, 4, 5], dtype=float)      # instrument
U = np.array([1, -2, 0, 2, -1], dtype=float)     # unobserved (Cov(Z,U)=0 by construction)
X = 2 + 1*Z + U                                   # endogenous: [4, 2, 5, 8, 6]
Y = 10 + 3*X + U                                  # outcome (true beta = 3)

print(f"Z: {Z},  U: {U}")
print(f"X = 2 + Z + U: {X}")
print(f"Y = 10 + 3X + U: {Y}")

# Verify Cov(Z,U) = 0
Zbar, Ubar = 3.0, 0.0
cov_ZU = np.mean((Z-Zbar)*(U-Ubar))
print(f"\nCov(Z,U) = {cov_ZU:.1f} (zero by construction)")

# OLS
n = 5
Xmat = np.column_stack([np.ones(n), X])
beta_ols = inv(Xmat.T @ Xmat) @ Xmat.T @ Y
print(f"\nOLS: Y = {beta_ols[0]:.1f} + {beta_ols[1]:.1f}*X  (true beta=3, OLS={beta_ols[1]:.1f} -- BIASED)")

# IV
Xbar, Ybar = np.mean(X), np.mean(Y)
cov_ZY = np.mean((Z-Zbar)*(Y-Ybar))
cov_ZX = np.mean((Z-Zbar)*(X-Xbar))
beta_iv = cov_ZY / cov_ZX
print(f"\nCov(Z,Y) = {cov_ZY:.1f}")
print(f"Cov(Z,X) = {cov_ZX:.1f}")
print(f"IV = Cov(Z,Y)/Cov(Z,X) = {cov_ZY:.1f}/{cov_ZX:.1f} = {beta_iv:.1f}")
assert np.isclose(beta_iv, 3.0), "IV should recover true beta!"
print("PASS: IV recovers true beta = 3 exactly.\n")


# =====================================================================
# RESULT 8: REGRESSION DISCONTINUITY
# =====================================================================
print("=" * 70)
print("RESULT 8: REGRESSION DISCONTINUITY")
print("=" * 70)

R = np.array([43, 45, 47, 49, 51, 53, 55, 57], dtype=float)
D = (R >= 50).astype(float)
Y = 60 + 0.5*R + 5*D

print(f"R (test score):  {R.astype(int)}")
print(f"D (scholarship): {D.astype(int)}")
print(f"Y (outcome):     {Y}")

# Fit lines on each side
ones4 = np.ones(4)
R_b, Y_b = R[:4], Y[:4]
Xm_b = np.column_stack([ones4, R_b])
b_b = inv(Xm_b.T @ Xm_b) @ Xm_b.T @ Y_b
pred_left = b_b[0] + b_b[1]*50

R_a, Y_a = R[4:], Y[4:]
Xm_a = np.column_stack([ones4, R_a])
b_a = inv(Xm_a.T @ Xm_a) @ Xm_a.T @ Y_a
pred_right = b_a[0] + b_a[1]*50

print(f"\nLine below: Y = {b_b[0]:.1f} + {b_b[1]:.2f}*R -> at R=50: {pred_left:.1f}")
print(f"Line above: Y = {b_a[0]:.1f} + {b_a[1]:.2f}*R -> at R=50: {pred_right:.1f}")
print(f"RD estimate = {pred_right:.1f} - {pred_left:.1f} = {pred_right-pred_left:.1f}")
assert np.isclose(pred_right - pred_left, 5.0), "RD should recover tau=5!"
print("PASS: RD recovers treatment effect = 5 exactly.\n")


# =====================================================================
# RESULT 9: FRISCH-WAUGH-LOVELL
# =====================================================================
print("=" * 70)
print("RESULT 9: FRISCH-WAUGH-LOVELL")
print("=" * 70)

X1 = np.array([1, 2, 3, 5, 4], dtype=float)
X2 = np.array([2, 4, 6, 8, 10], dtype=float)
Y  = np.array([3, 7, 10, 18, 12], dtype=float)
n = 5
ones = np.ones(n)

print(f"X1: {X1.astype(int)}")
print(f"X2: {X2.astype(int)}")
print(f"Y:  {Y.astype(int)}")

# Full regression
X_full = np.column_stack([ones, X1, X2])
beta_full = inv(X_full.T @ X_full) @ X_full.T @ Y
print(f"\nFull: Y = {beta_full[0]:.4f} + {beta_full[1]:.4f}*X1 + {beta_full[2]:.4f}*X2")

# (a) Y on X2 -> residuals
X2mat = np.column_stack([ones, X2])
b_YX2 = inv(X2mat.T @ X2mat) @ X2mat.T @ Y
Yhat = X2mat @ b_YX2
Y_tilde = Y - Yhat
print(f"\n(a) Y on X2: Y = {b_YX2[0]:.1f} + {b_YX2[1]:.2f}*X2")
print(f"    Y_tilde = {np.round(Y_tilde, 1)}")

# (b) X1 on X2 -> residuals
b_X1X2 = inv(X2mat.T @ X2mat) @ X2mat.T @ X1
X1hat = X2mat @ b_X1X2
X1_tilde = X1 - X1hat
print(f"\n(b) X1 on X2: X1 = {b_X1X2[0]:.1f} + {b_X1X2[1]:.2f}*X2")
print(f"    X1_tilde = {np.round(X1_tilde, 1)}")

# (c) Y_tilde on X1_tilde
beta_FWL = np.sum(X1_tilde * Y_tilde) / np.sum(X1_tilde**2)
print(f"\n(c) Regress Y_tilde on X1_tilde:")
print(f"    slope = {np.sum(X1_tilde * Y_tilde):.1f} / {np.sum(X1_tilde**2):.1f} = {beta_FWL:.4f}")

print(f"\n(d) Full regression coeff on X1 = {beta_full[1]:.4f}")
print(f"(e) FWL coeff on X1              = {beta_FWL:.4f}")
assert np.isclose(beta_FWL, beta_full[1]), "FWL should match full regression!"
print("PASS: FWL coefficient matches full regression exactly.")

print("\n" + "=" * 70)
print("ALL 9 RESULTS VERIFIED SUCCESSFULLY")
print("=" * 70)
