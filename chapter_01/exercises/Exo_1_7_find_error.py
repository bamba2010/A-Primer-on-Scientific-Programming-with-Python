# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

# find error(s) in a proram
from math import sin
x = 1; print('sin(%g)=%g' % (x,sin(x)))
# the errors in this program were:
# use of sin function without importing math and sin
# missing parenthese
