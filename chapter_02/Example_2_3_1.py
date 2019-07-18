

# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
print(" while loop result")
print("   C     F")
for c in Cdegrees:
    # This for loop implementation can be done using the while loop below
    F = (9.0 / 5) * c + 32
    print("%5d %5.1f" % (c, F))
print("for loop result")







Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
index = 0
while index < len(Cdegrees):
    # This while loop implemetation and the above for loop are the same
    C = Cdegrees[index]
    F = (9.0 / 5) * C + 32
    print(" %5d %5.1f" % (C, F))
    index += 1
print("C       F")
