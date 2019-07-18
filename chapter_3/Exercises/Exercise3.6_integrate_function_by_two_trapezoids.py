# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
from math import *


def Simpson(f, a, b):
    """ integrate a function by two trapezoids"""
    h = (b-a)/2
    integral = ((b - a) / 4) * 2*(f(a +h) + f(b))
    return integral


def h(x):
    """exponential of x from 0 to ln3"""
    return exp(x)

def application():
    print("Integral of exp(x) from 0 to ln3")
    approx = Simpson(h, 0, log(3))
    print(" approx = %18.15f, error = %9.2E" % (approx, 2 - approx))
t = application()