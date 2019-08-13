# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
import math


class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w

    def value(self, x):
        return math.exp(-self.a * x) * math.sin(self.w * x)


f = F(a=1.0, w=0.1)
print(f.value(x=2 * math.pi))
