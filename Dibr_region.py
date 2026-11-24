import numpy as np

H0 = np.array([
    [26.728, 261.23, 250,    0,      0],
    [3.68,   87.576, 479.6,  0,      0],
    [0,      26.728, 261.23, 250,    0],
    [0,      3.68,   87.576, 479.6,  0],
    [0,      0,      26.728, 261.23, 250]
])

H1 = np.array([
    [0.08, 1.3,  0,   0,   0],
    [0,    0.56, 1,   0,   0],
    [0,    0.08, 1.3, 0,   0],
    [0,    0,    0.56,1,   0],
    [0,    0,    0.08,1.3, 0]
])








Dibr =12


A = -np.linalg.inv(H0) @ H1


eigvals = np.linalg.eigvals(A)


eigvals_real = eigvals[np.isreal(eigvals)].real


lambda_max_pos = np.max(eigvals_real[eigvals_real >= 0])
lambda_min_neg = np.min(eigvals_real[eigvals_real < 0])


lower_bound = max(Dibr  + 1/lambda_min_neg , 0)

if lambda_max_pos ==0:
    upper_bound =  float("inf")
else:
     upper_bound = Dibr  + 1/lambda_max_pos
    

print("λ_max^+ =", lambda_max_pos)
print("λ_min^- =", lambda_min_neg)
print(f"D_ibr range: [{lower_bound:.6f}, {upper_bound:.6f}]")
