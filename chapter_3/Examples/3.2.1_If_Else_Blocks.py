# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

def N(x):
    if x < 0:
        return 0.0
    elif 0 <+ x < 1:
        return x
    elif 1 <= x <2:
        return  2-x
    elif x >=2:
        return  0

t = N(5)
print(t)
