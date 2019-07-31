
# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

a = [1,3,5,7,11]
b = [13,17]
c = a+b
print(c)
b[0]=-1
print(b)
d = [e+1 for e in a]
print(d)
d.append(b[0] +1)
d.append(b[-1]+1)
print(d)