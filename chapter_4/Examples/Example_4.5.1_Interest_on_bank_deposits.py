# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
from math import log as ln

def present_amount (a0, p,n):
    return a0*(1+p/(360.0*100))**n
def initial_amount (A,p,n):
    return A*(1 +p(360.0*100))**(-n)
def days(a0,A,p):
    return ln(a0/A)/ln(1 + p/(360.0*100))
def annual_rate(a0,A,n):
    return 360*100*((A/a0)**(1.0/n) -1)