# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

from math import pi
# The air resistance on a ball
C_D = 0.2
a = 0.11
A = pi*a**2
r = 1.2  # the density of air
# the force on ball with a hard kick
V = 120000.0/3600 # m/s
F_d = (1/2)*C_D*r*A*V**2
print(F_d)
# the force on the ball with a soft kick
V_s = 10000.0/3600 # m/s
# the gravity on the ball
m = 0.3
g = 9.81
F_g = m*g
print(F_g)
