import numpy as np
from matplotlib import pylab as plt

def first_digit(x):
    """Return the first digit of x."""

    prefixes = ["0", ".", "-"]
    x_str = str(float(x))
    while x_str[0] in prefixes:
        x_str = x_str[1:]

    first = int(x_str[0])
    return first


