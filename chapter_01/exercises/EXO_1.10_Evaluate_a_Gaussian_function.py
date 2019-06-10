# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

# Gaussian function
from math import pi, exp,sqrt
m = 0
s = 2
x = 1
f = (1/((2*pi)*s))*exp((-1/2)*((x-m)/s)**2)
print(f)
