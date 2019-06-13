# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

# range(start, stop, step)

Cdegrees = []
for C in range(-20, 45, 5):
    Cdegrees.append(C)
print(Cdegrees)

Cdegrees = []
for i in range(0, 21):
    """since range cannot support floating point"""
    c = -10 + i * 2.5
    Cdegrees.append(c)
print(Cdegrees)
