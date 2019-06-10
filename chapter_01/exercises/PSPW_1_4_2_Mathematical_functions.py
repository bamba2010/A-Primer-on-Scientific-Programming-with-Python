# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

from math import sinh, exp, e, pi
x= 2*pi
r1 = sinh(x)
r2 = 0.5 *(exp(x) - exp(-x))
r3 = 0.5*(e**x - e**(-x))
print(r1, r2,r3)
print('%.5f %.5f  %.5f'% (r1, r2,r3))
