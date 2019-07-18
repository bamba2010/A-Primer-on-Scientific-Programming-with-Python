# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
formulas= input('Write a formula involving x:')
code = """
def f(x):
  return %s
""" % formulas
exec(code)

x = 5
while x is not None :
    "The eval function takes n expression and evaluate it as a function"
    f = eval(input('Give x(None to quit):'))
    if x is not None:
        print("f(%g)=%g" %(x,f))


