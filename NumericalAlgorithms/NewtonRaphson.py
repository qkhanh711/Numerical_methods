def Newton_Raphson(func, x0, tol=1e-12, max_iter=100):
    x = x0
    dfunc = (func(x + tol) - func(x)) / tol
    for iteration in range(max_iter):
        x = x - func(x) / dfunc
        if abs(func(x)) < tol:
            return x, iteration + 1