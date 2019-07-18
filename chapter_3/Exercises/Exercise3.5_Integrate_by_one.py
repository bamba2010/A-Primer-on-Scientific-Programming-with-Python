# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
from math import *


def Simpson(f, a, b):
    """integrate functions by one trapezoids"""

    integral = ((b - a) / 2) * (f(a) + f(b))
    return integral


def h(x):
    """exponential of x from 0 to ln3"""
    return exp(x)


def h(x):
    """cos of x from 0 to pi"""
    return cos(x)


def h(x):
    """sin of x from 0 to pi"""
    return sin(x)


def h(x):
    """sin of x from 0 to pi/2"""
    return sin(x)


def application():
    print("Integral of exp(x) from 0 to ln3")
    approx = Simpson(h, 0, log(3))
    print(" approx = %18.15f, error = %9.2E" % (approx, 2 - approx))


# def application1():
#     print("Integral of exp(x) from 0 to pi")
#     approx = Simpson(h, 0, pi)
#     print(" approx = %18.15f, error = %9.2E" % (approx, 2 - approx))
#
#
# def application2():
#     print("Integral of exp(x) from 0 to pi")
#     approx = Simpson(h, 0, pi)
#     print(" approx = %18.15f, error = %9.2E" % (approx, 2 - approx))
#
#
# def application3():
#     print("Integral of exp(x) from 0 to pi/2")
#     approx = Simpson(h, 0, pi / 2)
#     print(" approx = %18.15f, error = %9.2E" % (approx, 2 - approx))
#
#
t = application()

# t1 = application1()
#
# t2 = application2()
#
# t3 = application3()
