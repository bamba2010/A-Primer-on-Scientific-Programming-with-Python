# Copyright (c) 2019 Cheick Bamba
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
import sys
"""this code takes two commandes lines aguments and return their product, return type """
c1 = eval(sys.argv[1])
c2 = eval(sys.argv[2])
c= c1*c2
print("%s + %s becomes %s\nwith value %s"%(type(c1),type(c2),type(c),c))
