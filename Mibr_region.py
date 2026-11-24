import numpy as np

P0 = np.array([
    [0.57584314,    5.1692157,    4.9019608, 0,        0],
    [0.08,       1.82266667, 9.3647059, 0,        0],
    [0,          0.57584314, 5.1692157, 4.9019608, 0],
    [0,          0.08,       1.8226667, 9.3647059, 0],
    [0,          0,          0.57584314, 5.1692157, 4.9019608]
])

P1 = np.array([
    [0.808, 212.63, 250,    0,      0],
    [0,     26.656, 477.6,  0,      0],
    [0,     0.808,  212.63, 250,    0],
    [0,     0,      26.656, 477.6,  0],
    [0,     0,      0.808,  212.63, 250]
])




Mhat_ibr = 6
Mg = 45


A = -np.linalg.inv(P0) @ P1


eigvals = np.linalg.eigvals(A)


eigvals_real = eigvals[np.isreal(eigvals)].real


lambda_max_pos = np.max(eigvals_real[eigvals_real > 0])
lambda_min_neg = np.min(eigvals_real[eigvals_real < 0])


lower_bound = max(1 / (1/(Mg+Mhat_ibr) + 1/lambda_max_pos) - Mg, 0)
upper_bound = 1 / (1/(Mg+Mhat_ibr) + 1/lambda_min_neg) - Mg

print("λ_max^+ =", lambda_max_pos)
print("λ_min^- =", lambda_min_neg)
if upper_bound > 1e7:
    print(f"M_ibr range: [{lower_bound:.6f}, inf) "
          "(The upper bound should be inf after removing numerical errors.)")
else:
    print(f"M_ibr range: [{lower_bound:.6f}, {upper_bound:.6f}]")
