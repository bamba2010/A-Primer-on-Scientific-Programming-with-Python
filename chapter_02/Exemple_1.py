# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

# computing conversion with while loop
print("-----------------------------------")
c = -20
dc = 5
while c <= 40:
    F = (9.0 / 5) * c + 32
    print(c, F)
    c += c + dc
print("-----------------------------------")
