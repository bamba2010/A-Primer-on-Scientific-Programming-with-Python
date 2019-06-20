# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
def diff2(f,x,h=1E-6):
    r =(f(x-h)-2*f(x) + f(x+h))/float(h*h)
    return r
def g(t):
    return t**(-6)
t = 1.2
d2g = diff2(g,t)
print("g (%f)=%f" %(t,d2g))

for k in range(1,15):
    h = 10**(-k)
    d2g = diff2(g,1,h)
    print("h=%.0e:  %.5f" %(h,d2g))