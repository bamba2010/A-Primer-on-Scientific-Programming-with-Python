# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

def growth_of_money(A, n):
    p = 0.05
    t = A*(1+p/100)**n
    return t
t= growth_of_money(1000, 3)
print(t)
