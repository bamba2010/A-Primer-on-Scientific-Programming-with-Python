
# Copyright (c) 2019 Cheick Bamba
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

import pprint

Cdegrees = [-10, -5, 0, 5, 10, 20, 25, 30, 34]
Fdegrees = [(9.0 / 5) * c + 32 for c in Cdegrees]
table = [Cdegrees, Fdegrees]
"""printing two lits inside one list"""
print(table)
"""printing second element of the second list(Fdegrees"""
print(table[1][2])

table1 = []
for c, F in zip(Cdegrees, Fdegrees):
    """using zip()"""
    table1.append([c, F])
print(table1)

table2 = [[c, F] for C, F in zip(Cdegrees, Fdegrees)]
pprint.pprint(table2)
print("using pprint.pformat for formating")
"""using pprint.pformat"""
s =pprint.pformat(table2)
print(s)
"""for print on multiple line"""
