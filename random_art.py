import random
from math import sin, cos, pi, tan, hypot, e

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def cube(a):
    return a ** 3


def avg(x, y):
    return x + y / 2


def wut(x, y):
    return (x**10) + (y**3)


def wtf(x, y, z):
    return (x**3) + (y**4) + (z**5)


def omg_wtf(prob):
    return("wtf(" + str(generate_expression(prob**2)) + ','
                  + str(generate_expression(prob**2)) + ','
                  + str(generate_expression(prob**2)) + ")")


def wut_wut(prob):
    return("wut(" + str(generate_expression(prob**2)) + ','
                  + str(generate_expression(prob**2)) + ")")


def sin_pi(prob):
    return "sin(pi*" + str(generate_expression(prob**2)) + ")"


def tan_pi(prob):
    return "tan(pi*" + str(generate_expression(prob**2)) + ")"


def cube_pi(prob):
    return "cube(pi*" + str(generate_expression(prob**2)) + ")"


def cos_pi(prob):
    return "cos(pi*" + str(generate_expression(prob**2)) + ")"


def avg_num(prob):
    return ("avg(" + str(generate_expression(prob**2)) + ','
                   + str(generate_expression(prob**2)) + ")")


def hypot_num(prob):
    return ("hypot(" + str(generate_expression(prob**2)) + ','
                     + str(generate_expression(prob**2)) + ")")


def cos_num(prob):
    return "cos(" + str(generate_expression(prob**2)) + ")"


def sin_num(prob):
    return "sin(" + str(generate_expression(prob**2)) + ")"


def cube_num(prob):
    return "cube(" + str(generate_expression(prob**2)) + ")"


def generate_expression(prob=0.99):
    if random.random() < prob:
        return random.choice([sin_pi(prob), cos_pi(prob),
                              sin_num(prob), avg_num(prob),
                              omg_wtf(prob)])
    else:
        return random.choice(['x', 'y'])


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    expr = generate_expression()
    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return eval(expr)
