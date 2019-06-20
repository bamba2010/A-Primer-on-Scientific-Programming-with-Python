# Copyright (c) 2019 Cheick Bamba
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
from math import *


def f(a, b, c):
    """function that solves the quadratic equation"""
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return print("no real solutions")
    elif delta > 0:
        x1 = (-b - sqrt(delta)) / 2 * a
        x2 = (-b + sqrt(delta)) / 2 * a
        print("we have to real solutions x1 and x2")
        return x1, x2
    elif delta == 0:
        x = -b / 2 * a
        print("we have an unique solution x")
        return x


r = f(1, -2, 1)
print(r)
