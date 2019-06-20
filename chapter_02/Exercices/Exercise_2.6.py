# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
y_table = []
t_table =[]
vo = 1
g = 9.81
for t in range (0, 4, 1 ):
    y = vo*t -(1.0/2)*g*t**2
    t_table.append(t)
    y_table.append(y)
print([t_table], [y_table])