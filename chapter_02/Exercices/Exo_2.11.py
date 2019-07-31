# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
h_i=0.01
x_i = 1
d = []
for i in range(100):
    """generate equally spaced coordinates"""
    x_i+=h_i
    i = i+1
    print(x_i)