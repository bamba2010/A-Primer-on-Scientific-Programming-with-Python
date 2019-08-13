# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
def f(x):
    return x ** 2 + 4


"""can be rewritten as """
g = lambda x: x ** 2 + 4
print(g(5))
t = f(4)
print(t)
