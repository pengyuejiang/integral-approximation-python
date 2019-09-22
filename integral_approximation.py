from sympy.parsing.sympy_parser import parse_expr
from math import *
from sympy import *
import numpy as np

# Left endpoints integral approximation
def left(expr, left_bound, right_bound, delta_x):
    x = symbols('x')
    expression = parse_expr(expr)
    sum = 0
    for i in np.arange(left_bound, right_bound, delta_x):
        sum += expression.subs(x, i)
    return delta_x * sum

# RIght endpoints integral approximation
def right(expr, left_bound, right_bound, delta_x):
    x = symbols('x')
    expression = parse_expr(expr)
    sum = 0
    for i in np.arange(left_bound + delta_x, right_bound + delta_x, delta_x):
        sum += expression.subs(x, i)
    return delta_x * sum

# Midpoints integral approximation
def mid(expr, left_bound, right_bound, delta_x):
    x = symbols('x')
    expression = parse_expr(expr)
    sum = 0
    for i in np.arange(left_bound, right_bound, delta_x):
        sum += expression.subs(x, i + delta_x / 2)
    return delta_x * sum

# Trapezoidal Rule for integral approximation
def trapezoidal(expr, left_bound, right_bound, delta_x):
    return (left(expr, left_bound, right_bound, delta_x) \
            + right(expr, left_bound, right_bound, delta_x)) / 2

# Simpson's Rule for integral approximation
def simpson(expr, left_bound, right_bound, delta_x):
    x = symbols('x')
    expression = parse_expr(expr)
    sum = 0
    numbers = list(np.arange(left_bound, right_bound + delta_x, delta_x))
    for i in range(len(numbers)):
        if i == 0 or i == len(numbers) - 1:
            sum += expression.subs(x, numbers[i])
        elif i % 2 == 0:
            sum += 2 * expression.subs(x, numbers[i])
        else:
            sum += 4 * expression.subs(x, numbers[i])
    return delta_x * sum / 3

if __name__ == '__main__':
    # Read input
    expr = input('Expression: ')
    left_bound = float(input('Left Bound: '))
    right_bound = float(input('Right Bound: '))
    delta_x = float(input('Delta x: '))
    type = int(input('Select the type of approximation:\n \
    1. Left Endpoints\n \
    2. Right Endpoints\n \
    3. Midpoints\n \
    4. Trapezoidal Rule\n \
    5. Simpson\'s Rule\n'))
    # Determine which function to call
    if type == 1:
        print('Result:', left(expr, left_bound, right_bound, delta_x))
    elif type == 2:
        print('Result:', right(expr, left_bound, right_bound, delta_x))
    elif type == 3:
        print('Result:', mid(expr, left_bound, right_bound, delta_x))
    elif type == 4:
        print('Result:', trapezoidal(expr, left_bound, right_bound, delta_x))
    elif type == 5:
        print('Result:', simpson(expr, left_bound, right_bound, delta_x))
