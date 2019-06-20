# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
from math import *
def f(x):
    """ in line if statement"""
    return (sin(x) if 0<=x <= 2*pi else 0)
t = f(2*pi)
print(t)

"""lambda function and inline if statement"""
f = lambda x: sin(x) if 0<= x<= 2*pi else 0