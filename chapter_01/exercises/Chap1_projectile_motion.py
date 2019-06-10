# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

# The formula of projectile motion
def equation_projectile(t):
    n_0= 100
    g = 3.6
    y = n_0*t - (0.5)*g*t**2
    return y

y = equation_projectile(10)
print(y)
