# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
def yfunc(t,v0):
    g = 9.81
    return v0*t -0.5*g*t**2


y = yfunc(0.1,6)
print(y)
y = yfunc(0.1,v0=6)
print(y)
y = yfunc(t=0.1,v0=6)
print(y)
y = yfunc(v0=6,t = 0.1)
print(y)

def makelist(start, stop, inc):
    """list of object function"""
    value = start
    result = []
    while value <= stop:
        result.append(value)
        value = value + inc
    return  result

mylist = makelist(0, 100, 2)
print(mylist)