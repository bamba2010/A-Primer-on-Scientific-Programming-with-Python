# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

from cmath import sin, sinh
from math import exp
u = 2.5 + 3j
v = 2
w = u +v
print(w)

a = -2
b = 0.5
s = a + b*1j
print(s)
p = complex(a,b)
print(p)
print(w*s)
print(s.real)
print(s.imag)

# python with complex number
r1 = sin(8j)
print(r1)
r2 = 1j*sinh(8)
print(r2)
q = 8

