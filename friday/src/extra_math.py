import numpy as np

def factorial(x):
    total = 1
    for i in range(1, x+1):
        total *= i
    return total

def get_math_val(x):
    if x == 'e':
        return np.e
    elif x == 'pi':
        return np.pi
    else:
        return float(x)

def get_trig(num, func, is_degree):
    if not is_degree:
        if func == 'sin':
            return np.sin(num)
        elif func == 'cos':
            return np.cos(num)
        elif func == 'tan':
            return np.tan(num)
    else:
        num = num * np.pi / 180
        if func == 'sin':
            return np.sin(num)
        elif func == 'cos':
            return np.cos(num)
        elif func == 'tan':
            return np.tan(num)