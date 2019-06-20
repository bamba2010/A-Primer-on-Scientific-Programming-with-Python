# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
def sum(alist):
    """function that takes a string as argument and sum it element"""
    sum1 = 0
    for i in alist:
        sum1 += i
    return sum1


Cdegrees = [-10, -5, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
t = sum(Cdegrees)

print(t)
