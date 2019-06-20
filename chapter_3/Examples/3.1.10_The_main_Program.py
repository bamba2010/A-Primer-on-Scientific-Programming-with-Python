from math import *
def f(x):
    e = exp(-0.1*x)
    s = sin(6*pi*x)
    return e*s
x = 2
y = f(x)
print("f(%g)=%g" %(x,y))
    