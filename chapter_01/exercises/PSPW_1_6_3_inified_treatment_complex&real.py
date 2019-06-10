# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

from numpy.lib.scimath import sqrt
a = 1; b = 2; c = 100;
r1 = (-b + sqrt(b**2 - 4 *a*c))/(2*a)
r2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
print(r1)
print(r2)
