# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
from math import pi, exp, sin
def somefunc(arg1, arg2, kwarg1 = True, kwarg2 = 0):

    """function with keword arguments"""
    print(arg1,arg2, kwarg1, kwarg2)

print(somefunc("Hello",[1,2]))

def f(t, A=1,a =1,omega=2*pi):
    return A*exp(-a*t)*sin(omega*t)
v1 =f(0.2)
print(v1)



