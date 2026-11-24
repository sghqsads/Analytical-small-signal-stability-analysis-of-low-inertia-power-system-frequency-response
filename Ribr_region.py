import numpy as np

H0 = np.array([
    [26.568, 265.38, 250,    0,      0],
    [3.68,    87.956,485.1,  0,      0],
    [0,       26.568,265.38, 250,    0],
    [0,       3.68,  87.956, 485.1,  0],
    [0,       0,     26.568, 265.38, 250]
])

H1 = np.array([
    [0, 0.9, 0,   0,   0],
    [0, 0.2, 1,   0,   0],
    [0, 0,   0.9, 0,   0],
    [0, 0,   0.2, 1,   0],
    [0, 0,   0,   0.9, 0]
])





reci_Ribr =37.5


A = -np.linalg.inv(H0) @ H1


eigvals = np.linalg.eigvals(A)


eigvals_real = eigvals[np.isreal(eigvals)].real


lambda_max_pos = np.max(eigvals_real[eigvals_real >= 0])
lambda_min_neg = np.min(eigvals_real[eigvals_real < 0])


lower_bound = max(reci_Ribr  + 1/lambda_min_neg , 0)

if lambda_max_pos ==0:
    upper_bound =  float("inf")
else:
     upper_bound = reci_Ribr  + 1/lambda_max_pos
    

print("λ_max^+ =", lambda_max_pos)
print("λ_min^- =", lambda_min_neg)
print(f"single IBR 1/Ribr range: [{lower_bound / 3 *10/8:.6f}, {upper_bound / 3 *10/8:.6f}]")
