def secant_method(func, x0, x1, tol=1e-10, max_iter=100):
    x_k_minus_1 = x0
    x_k = x1
    for iteration in range(max_iter):
        f_k_minus_1 = func(x_k_minus_1)
        f_k = func(x_k)
        x_k_plus_1 = x_k - f_k * (x_k - x_k_minus_1) / (f_k - f_k_minus_1)
        if abs(x_k_plus_1 - x_k) < tol:
            return x_k_plus_1, iteration + 1
        x_k_minus_1, x_k = x_k, x_k_plus_1