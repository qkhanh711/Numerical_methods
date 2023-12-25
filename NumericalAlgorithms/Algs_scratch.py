from func import *


def Newton_Raphson(func, x0, tol=1e-7, max_iter=100):
    x = x0
    dfunc = (func(x + tol) - func(x)) / tol
    for iteration in range(max_iter):
        x = x - func(x) / dfunc
        if abs(func(x)) < tol:
            return x, iteration + 1
    return x, iteration + 1


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
    return x_k_plus_1, iteration + 1


def bisection(a, b, func_x, tol=1e-10):
    if abs(a - b) < tol:
        c = (a + b) / 2
        if func_x(c) == 0:
            return c
        elif func_x(a) * func_x(b) > 0:
            return bisection(a, c, func_x)
        elif func_x(a) * func_x(b) < 0:
            return bisection(c, b, func_x)
        else:
            return "No root in (a, b)"


if __name__ == "__main__":
    print(
    bisection(-2, 2, func_x),
    Newton_Raphson(func_x, 0),
    secant_method(func_x, -1, 0)
    )