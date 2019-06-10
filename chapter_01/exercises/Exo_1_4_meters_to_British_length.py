# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

# function to convert meters to inches

def meters_to_inches(y):
    # since we know that 1 inch= 2.54 cm and 1 meter = 100 cm
    # then   x inch = (100/2.54)* y meters
    a = 100.0
    b = 2.54
    x = (a*y/b)
    return x

def meters_to_feet(y):
    a = 100.0
    b = 30.48
    m = (a*y/b)
    return m
def meters_to_yards(y):
    a = 100
    b = 91.44
    m =  (a*y/b)
    return m
def meters_to_miles(y):
    a = 100
    b = 160934.4
    m = (a*y/b)
    return m

x= meters_to_inches(640)
print(x)
m= meters_to_feet(640)
print(m)
x= meters_to_yards(640)
print(x)
x= meters_to_miles(640)
print(x)

