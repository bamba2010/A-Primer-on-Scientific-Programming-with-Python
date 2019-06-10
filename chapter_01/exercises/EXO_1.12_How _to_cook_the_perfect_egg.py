# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

from math import log2, pi
# t for a large egg
M = 67 # masse in g
r = 1.038  # density in gcm^-3
c = 3.7 # specific heat capacity Jg^-1K^-1
K= 5.4*10**(-3)
T_w = 100 # temperature of the boiling water
T_o = 4 # original temperature taken from fidge
T_y = 70
t =(((M**(2/3))*c*(r**(1/3)))/K*pi**2*(4*pi/3)**(2/3))*log2(0.76*((T_o-T_w)/(T_y-T_w)))

print(t)
