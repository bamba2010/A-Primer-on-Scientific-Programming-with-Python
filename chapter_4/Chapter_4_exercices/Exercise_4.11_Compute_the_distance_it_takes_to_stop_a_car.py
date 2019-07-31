# Copyright (c) 2019 Cheick Bamba
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
import sys
g = 9.81
"""This code takes v0,t from the commande line and return s"""
"""It also throw exception when  no arguments are supplied to the command line or t is not between 0 and 2*v0/g"""
try:
    v0 = float(sys.argv[1])
    u = float(sys.argv[2])
except IndexError:
    print("The initial velocity and the friction must be supplied to the commad line")
    sys.exit(1)
    V0 = v0*5/18
if  u ==0 :
    raise ValueError(" u must not be 0")
else : d = 0.5*v0**2/u*g
print(d)
