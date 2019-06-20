# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
def yfunc(t,v0):
    """function with two return values"""
    g = 9.81
    y = v0*t -0.5*g*t**2
    dydt = v0-g*t
    return y, dydt

position, velocity = yfunc(0.6, 3)
print(position,velocity)
t_value= [0.05*i for i in range(10)]
for t in t_value:
    pos, vel = yfunc(t,v0=5)
    """to create a nice looking columns
    """
    print("t=% -10g position=%-10g velocity = % -10g" % (t,pos,vel))


def L(x,n):
    s = 0
    for i in range (1, n+1):
        s += (1.0/i)*(x/(1.0 +x))**i
    return s

p =L(2,10)
print(p)