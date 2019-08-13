# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
"""Turning an Instance into a String"""
class Y:
    def __init__(self, v0):
        self.v0= v0
        self.g = 9.81

    def __call__(self,t):
        return self.v0*t - 0.5*self.g*t**2
    def __str__(self):
        return 'v0*t - 0.5*self.g*t**2; v0=%g' % self.v0

y= Y(1.5)
print(y(0.2))