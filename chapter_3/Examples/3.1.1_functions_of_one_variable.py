# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)


def F(C):
    """function that takes C and convert from celsius to fahrenheit"""

    return (9.0 / 5) * C + 32


a = 10
F1 = F(a)
Cdegrees = [-10, -5, 0, 5, 10, 15, 20, 25, 30, 35]
Cfahrenheit = [F(C) for C in Cdegrees]
print(Cfahrenheit)
temp = F(15.5)
"""Calling F(C) function"""
print(F(a + 1))
sum_temp = F(10) + F(20)
print(sum_temp)


def F2(C):
    F_value = (9.0 / 5) * C + 32

    return "%.1f degrees Celsius corresponds to" \
           "%.f  degrees Fahrenheit" % (C, F_value)


s1 = F2(21)
print(s1)
