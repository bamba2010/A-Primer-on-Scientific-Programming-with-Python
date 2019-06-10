
# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

# (a)
from math import sin, cos, pi
x = pi/4
val = (sin(x))**2 + (cos(x))**2
print(val)

#########################
# (b)
v0 = 3
t = 1
a = 2
s = v0*t + (1/2)*t**2
print(s)
############################
a = 3.3; b = 5.3
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 -2*a*b + b2

eq1_pow = (a+b)**2
eq2_pow = (a-b)**2

print('First equation: %g = %g' %(eq1_sum, eq1_pow))
print('Second equation: %g = %g' %(eq2_pow, eq2_pow))
