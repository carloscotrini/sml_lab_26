import numpy as np
np.set_printoptions(precision=6, suppress=True)

print("=" * 70)
print("RESULT 1: OMITTED VARIABLE BIAS")
print("=" * 70)
# Context: Hours studied (X1), Hours slept (X2), Exam score (Y)
# X1 and X2 are correlated (students who study more sleep less)
# True model: Y = 60 + 5*X1 + 3*X2 + noise

# Design data where X1 and X2 are negatively correlated
# Let's pick simple values
X1 = np.array([1, 2, 3, 4, 5], dtype=float)  # hours studied
X2 = np.array([8, 7, 6, 5, 4], dtype=float)  # hours slept
# Y = 60 + 5*X1 + 3*X2 with small/no noise to keep it clean
# Let's use exact values for clarity
Y = 60 + 5*X1 + 3*X2  # no noise for clean demo
# Y = 60 + 5(1)+3(8), 60+10+21, 60+15+18, 60+20+15, 60+25+12
# Y = 89, 91, 93, 95, 97
print(f"X1 (hours studied): {X1}")
print(f"X2 (hours slept):   {X2}")
print(f"Y  (exam score):    {Y}")

# Full regression: Y on X1 and X2
n = len(X1)
X_full = np.column_stack([np.ones(n), X1, X2])
beta_full = np.linalg.lstsq(X_full, Y, rcond=None)[0]
print(f"\nFull regression Y = b0 + b1*X1 + b2*X2:")
print(f"  b0 = {beta_full[0]:.4f}, b1 = {beta_full[1]:.4f}, b2 = {beta_full[2]:.4f}")

# Short regression: Y on X1 only
X_short = np.column_stack([np.ones(n), X1])
beta_short = np.linalg.lstsq(X_short, Y, rcond=None)[0]
print(f"\nShort regression Y = a0 + a1*X1:")
print(f"  a0 = {beta_short[0]:.4f}, a1 = {beta_short[1]:.4f}")

# Auxiliary regression: X2 on X1
X_aux = np.column_stack([np.ones(n), X1])
delta = np.linalg.lstsq(X_aux, X2, rcond=None)[0]
print(f"\nAuxiliary regression X2 = d0 + d1*X1:")
print(f"  d0 = {delta[0]:.4f}, d1 = {delta[1]:.4f}")

print(f"\nBias formula: b1_short = b1_true + b2_true * d1")
print(f"  {beta_full[1]:.4f} + {beta_full[2]:.4f} * {delta[1]:.4f} = {beta_full[1] + beta_full[2]*delta[1]:.4f}")
print(f"  Actual b1_short = {beta_short[1]:.4f}")

# Hmm, with perfectly linear X1,X2 relationship this is exact but the numbers
# Y = 89,91,93,95,97 is just a linear function of X1 with slope 2.
# That's not ideal. Let me add some noise to make it more interesting.
print("\n--- Let me redesign with noise for a more interesting example ---")

X1 = np.array([1, 2, 3, 4, 5], dtype=float)
X2 = np.array([8, 7, 6, 5, 4], dtype=float)
# Add noise to Y
Y = np.array([89, 90, 94, 96, 97], dtype=float)  # close to 60+5X1+3X2

X_full = np.column_stack([np.ones(n), X1, X2])
beta_full = np.linalg.lstsq(X_full, Y, rcond=None)[0]
print(f"X1: {X1}, X2: {X2}, Y: {Y}")
print(f"Full: b0={beta_full[0]:.4f}, b1={beta_full[1]:.4f}, b2={beta_full[2]:.4f}")

X_short = np.column_stack([np.ones(n), X1])
beta_short = np.linalg.lstsq(X_short, Y, rcond=None)[0]
print(f"Short: a0={beta_short[0]:.4f}, a1={beta_short[1]:.4f}")

delta = np.linalg.lstsq(X_aux, X2, rcond=None)[0]
print(f"Aux: d0={delta[0]:.4f}, d1={delta[1]:.4f}")
print(f"Bias check: {beta_full[1]:.4f} + {beta_full[2]:.4f}*{delta[1]:.4f} = {beta_full[1]+beta_full[2]*delta[1]:.4f}")
print(f"Actual short b1 = {beta_short[1]:.4f}")

# The issue: with X1 and X2 perfectly correlated (X2 = 9-X1), we can't
# separately identify b1 and b2. Let me break the perfect correlation.
print("\n--- Breaking perfect correlation ---")
X1 = np.array([1, 2, 3, 4, 5], dtype=float)
X2 = np.array([8, 6, 7, 4, 5], dtype=float)  # correlated but not perfectly
Y_true = 60 + 5*X1 + 3*X2
print(f"X1: {X1}")
print(f"X2: {X2}")
print(f"Y (true, no noise): {Y_true}")

X_full = np.column_stack([np.ones(n), X1, X2])
beta_full = np.linalg.lstsq(X_full, Y_true, rcond=None)[0]
print(f"Full: b0={beta_full[0]:.6f}, b1={beta_full[1]:.6f}, b2={beta_full[2]:.6f}")

X_short = np.column_stack([np.ones(n), X1])
beta_short = np.linalg.lstsq(X_short, Y_true, rcond=None)[0]
print(f"Short: a0={beta_short[0]:.6f}, a1={beta_short[1]:.6f}")

X_aux = np.column_stack([np.ones(n), X1])
delta = np.linalg.lstsq(X_aux, X2, rcond=None)[0]
print(f"Aux (X2 on X1): d0={delta[0]:.6f}, d1={delta[1]:.6f}")
print(f"Bias = b2*d1 = {beta_full[2]:.6f} * {delta[1]:.6f} = {beta_full[2]*delta[1]:.6f}")
print(f"b1_true + bias = {beta_full[1]:.6f} + {beta_full[2]*delta[1]:.6f} = {beta_full[1]+beta_full[2]*delta[1]:.6f}")
print(f"b1_short = {beta_short[1]:.6f}")

print(f"\nCorrelation X1,X2: {np.corrcoef(X1,X2)[0,1]:.4f}")

# Let me try yet another design that gives cleaner numbers
print("\n--- Design with cleaner numbers ---")
X1 = np.array([1, 2, 3, 4, 5], dtype=float)
X2 = np.array([10, 8, 6, 4, 2], dtype=float)  # X2 = 12 - 2*X1
# This is perfectly correlated again. Let me try:
X2 = np.array([10, 8, 8, 4, 0], dtype=float)
Y_true = 50 + 3*X1 + 2*X2
print(f"X1: {X1}")
print(f"X2: {X2}")
print(f"Y = 50 + 3*X1 + 2*X2: {Y_true}")

X_full = np.column_stack([np.ones(n), X1, X2])
beta_full = np.linalg.lstsq(X_full, Y_true, rcond=None)[0]
print(f"Full: b0={beta_full[0]:.6f}, b1={beta_full[1]:.6f}, b2={beta_full[2]:.6f}")

X_short = np.column_stack([np.ones(n), X1])
beta_short = np.linalg.lstsq(X_short, Y_true, rcond=None)[0]
print(f"Short: a0={beta_short[0]:.6f}, a1={beta_short[1]:.6f}")

X_aux = np.column_stack([np.ones(n), X1])
delta = np.linalg.lstsq(X_aux, X2, rcond=None)[0]
print(f"Aux (X2 on X1): d0={delta[0]:.6f}, d1={delta[1]:.6f}")
print(f"Bias = b2*d1 = {beta_full[2]:.6f} * {delta[1]:.6f} = {beta_full[2]*delta[1]:.6f}")
print(f"b1_true + bias = {beta_full[1]+beta_full[2]*delta[1]:.6f}")
print(f"b1_short = {beta_short[1]:.6f}")
print(f"Corr(X1,X2) = {np.corrcoef(X1,X2)[0,1]:.4f}")
