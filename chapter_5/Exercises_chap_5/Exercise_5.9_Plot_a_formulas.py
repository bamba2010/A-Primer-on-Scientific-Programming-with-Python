# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
from matplotlib.pylab import *
def f(t):
    v0=10
    g = 9.81
    return v0*t -0.5*g*t**2
v0=10
g=9.81
t = linspace(0,2*v0/g,10)
y1 = f(t)
xlabel("s")
ylabel("m")
legend(["v0*t -0.5*g*t**2"])
title(" motion of a projectile")
plot(t,y1,"r-") # r- means red, bo means blue

show()