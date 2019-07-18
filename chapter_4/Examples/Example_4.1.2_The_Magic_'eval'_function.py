# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
from math import sqrt

"""The eval function takes a string as argument and evaluate it as a python expression"""

r = eval('2+2*2')
print(r)

r = eval("[1,2,3]")
print(r)
r = eval('sqrt(2)')
print(r)

i1 = eval(input("Give input: "))
i2 = eval(input("Give input: "))
r = i1 + i2
print("%s + %s becomes %s\nwith value %s " % (type(i1), type(i2), type(r),r))
print(r)


formulas = input("Give a formul involving x:")
"""passing expression to input and eval functions"""
x = eval(input("give x:"))
from math import *
result = eval(formulas)
print("%s for x=%g yields %g" % (formulas,x,result))