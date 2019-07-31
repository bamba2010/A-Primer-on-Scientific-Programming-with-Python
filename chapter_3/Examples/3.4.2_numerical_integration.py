# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
from math import *


def Simpson(f, a, b, n=500):
    """Simpson's rule for approximating integral of functions"""
    h = (b - a) / float(n)
    sum1 = 0
    for i in range(1, n // 2 + 1):
        sum1 += f(a + (2 * i - 1) * h)

    sum2 = 0
    for i in range(1, n // 2):
        sum2 += f(a + 2 * i * h)
    integral = (b - a) / (3 * n) * (f(a) + f(b) + 4 * sum1 + 2 * sum2)
    return integral


def h(x):
    return (3. / 2) * sin(x) ** 3


def application():
    print("Integral of 1.5*sin^3 from 0 to pi")
    for n in [2, 6, 12, 100, 500]:
        approx = Simpson(h, 0, pi, n)
        print("n = %3d, approx = %18.15f, error = %9.2E" % (n, approx, 2 - approx))

t = application()
