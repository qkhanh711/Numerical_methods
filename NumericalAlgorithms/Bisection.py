from func import func_x

def bisection(a, b, func_x):
    c = (a + b) / 2
    if func_x(c) == 0:
        return c
    elif func_x(a) * func_x(b) > 0:
        return bisection(a, c, func_x)
    elif func_x(a) * func_x(b) < 0:
        return bisection(c, b, func_x)
    else:
        return "No root in (a, b)"

bisection(-2, 2, func_x)