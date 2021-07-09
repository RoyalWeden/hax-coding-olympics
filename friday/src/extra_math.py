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