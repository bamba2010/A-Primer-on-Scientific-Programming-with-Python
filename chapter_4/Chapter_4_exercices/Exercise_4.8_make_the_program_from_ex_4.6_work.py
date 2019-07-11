# Copyright (c) 2019 Cheick Bamba
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
import sys
g = 9.81
"""This code takes v0,t from the commande line and return s"""
v0 = float(sys.argv[1])
t = float(sys.argv[2])
s =  v0*t  - (1/2)*g*t**2
print(s)
