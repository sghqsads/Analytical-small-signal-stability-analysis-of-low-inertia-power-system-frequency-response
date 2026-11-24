import numpy as np

H0 = np.array([
    [0.577565217, 6.00282609, 5.4347826, 0,        0],
    [0.08,        1.98817391,10.654348,  0,        0],
    [0,           0.57756522, 6.0028261, 5.4347826, 0],
    [0,           0.08,       1.98817391,10.654348,  0],
    [0,           0,          0.57756522, 6.00282609, 5.4347826]
])

H1 = np.array([
    [0, 3.80435,        0,           0,           0],
    [0, 1.08696,        2.71739,      0,           0],
    [0, 0,              3.80435,       0,           0],
    [0, 0,              1.08696,       2.717391304,0],
    [0, 0,              0,             3.804347826,0]
])



beta_ibr =0.4


A = -np.linalg.inv(H0) @ H1


eigvals = np.linalg.eigvals(A)


eigvals_real = eigvals[np.isreal(eigvals)].real


lambda_max_pos = np.max(eigvals_real[eigvals_real >= 0])
lambda_min_neg = np.min(eigvals_real[eigvals_real < 0])


lower_bound = max(beta_ibr  + 1/lambda_min_neg , 0)

if lambda_max_pos ==0:
    upper_bound = 1
else:
     upper_bound = min(beta_ibr  + 1/lambda_max_pos, 1)
    

print("λ_max^+ =", lambda_max_pos)
print("λ_min^- =", lambda_min_neg)
print(f"single IBR  Beta_ibr range: [{lower_bound / 3:.6f}, {upper_bound / 3:.6f}]")
