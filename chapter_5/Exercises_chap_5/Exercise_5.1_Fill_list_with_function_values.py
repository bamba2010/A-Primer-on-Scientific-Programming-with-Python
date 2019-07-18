
# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
import math
def f(x):
    return (1/math.sqrt(2*math.pi))*math.exp(-0.5*x**2)

n =4
dx =1.0/(n-1)

xlist= [i*dx for i in range(-n,n+1)]
ylist=[f(x) for x in xlist]
print("xlist is")
print(xlist)
print("ylist is")
print(ylist)