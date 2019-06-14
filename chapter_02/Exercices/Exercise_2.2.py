# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

c = -20
dc = 5
A =[]
B = []
D = []
while c <= 30:
    """Write approximate Farenheit-Celsius convention table"""
    F = (9 / 5) * c + 32
    C= (F-30)/2.0
    A.append(c)
    B.append(F)
    D.append(C)
    c = c + dc
print([A,B,D])