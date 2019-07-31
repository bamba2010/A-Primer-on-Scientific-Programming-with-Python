# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

def f(F):
    """function that convert Fahrenheit to celsius"""
    C = (5.0 / 9) * (F - 32)
    return C


t = f(21)
print(t)


def t(C):
    """function that convert celsius to fahrenheit"""
    F = (9.0 / 5) * C + 32
    return F


T = t(-6.111111111111112)
print(T)
