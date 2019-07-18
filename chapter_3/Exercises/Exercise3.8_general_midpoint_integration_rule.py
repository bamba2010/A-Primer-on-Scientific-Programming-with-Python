# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
from math import *


def Simpson(f, a, b, n=500):
    """ general  rule for integrating functions with trapezoids"""
    h = (b - a) / float(n)
    sum1 = 0
    for i in range(1, n):
        sum1 += f(a + (i/2) * h)

    integral = h * sum1
    return integral


def h(x):
    return (3. / 2) * sin(x) ** 3


def application():
    print("Integral of 1.5*sin^3 from 0 to pi")
    for n in [1, 10]:
        approx = Simpson(h, 0, pi, n)
        print("n = %3d, approx = %18.15f, error = %9.2E" % (n, approx, 2 - approx))


t = application()
