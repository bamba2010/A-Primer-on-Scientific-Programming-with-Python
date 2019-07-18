# Copyright (c) 2019 Cheick Bamba
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
"""reading input from user using input function"""
formulas = input("Give a formul involving x:")
"""passing expression to input and eval functions"""
x = eval(input("give x:"))
from math import *
result = eval(formulas)
print("%s for x=%g yields %g" % (formulas,x,result))