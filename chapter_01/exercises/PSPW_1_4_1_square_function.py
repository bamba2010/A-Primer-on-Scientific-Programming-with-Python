# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

from math import sqrt
v0 = 5
g = 9.81
yc = 0.2

t1 = (v0 - sqrt(v0**2-2*g*yc))
t2 = (v0 + (v0**2 -2*g*yc))

print('At t =%g s and %g s, the height is %g m.'%(t1,t2,yc))


