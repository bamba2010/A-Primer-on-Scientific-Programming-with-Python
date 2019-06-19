from math import sin, pi
# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)



def f(x):
    """f(x) = { sin(x), 0<=x <=pi or 0 otherwise} can be written as follow"""
    if 0 <= x <= pi:
        value = sin(x)
    else :
        value = 0
        return value
t = f(pi)
print(t)

Cdegrees= [-10, -5, 0 , 5, 10, 15, 20, 25, 30, 35]
for c in Cdegrees:
 if c < -273.15:
    print("%g degrees Celcius in non_physical!" % c)

 else :
     F = (9.0/5)*c +32
     print(F)