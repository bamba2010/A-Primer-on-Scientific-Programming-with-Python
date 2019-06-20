# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
def F3(C):
    F_value = (9.0/5)*C + 32
    print("Inside F : C = %s F_value =%s r =%s" % (C, F_value,r))
    return  "%0.1f degrees Celcius correspond to"\
            "%0.1f degrees Fahrenheit" % (C, F_value)

C = 60 # make a global variable C
r = 21 # another global variable
s3 = F3(r)
print(s3)
print(C)
