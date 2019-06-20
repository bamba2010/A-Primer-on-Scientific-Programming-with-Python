# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

# using for loop to print out all elements of a loop
degrees = [0, 10, 20, 40, 100]
for c in degrees:
    print("list elemet:", c)
print(" The degree list has", len(degrees), "elemenrts")
# computing conversion from  F to C
Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
print("   C     F")
for c in Cdegrees:
    F = (9.0 / 5) * c + 32
    print("%5d %5.1f" % (c, F))
