# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

c = -20
dc = 5
A =[]
B = []
while c <= 30:
    """Make the Farenheit_Celsius conversion table"""
    F = (9 / 5) * c + 32
    A.append(c)
    B.append(F)
    c = c + dc
print([A,B])