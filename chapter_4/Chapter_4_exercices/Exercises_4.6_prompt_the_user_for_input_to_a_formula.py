# Copyright (c) 2019 Cheick Bamba
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
t= float(input("please enter a value for c: "))
"""This program aks the user to provide the values of v0 and t and evaluate y"""
v0 = float(input("please enter a value for v0:"))
g = 9.81
y = v0*t - 0.5*g*t**2
print(y)