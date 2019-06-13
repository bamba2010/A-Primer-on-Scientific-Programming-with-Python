# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
# putting more than one list into a list
scores = []
# score of player no. 0:
scores.append([12, 16, 11, 12])
# score of player no .1
scores.append([9])
# score of player n0. 2:
scores.append([6, 9, 11, 14, 17, 15, 14, 20])
print(scores)
for p in range(len(scores)):
    for g in range(len(scores[p])):
        score = scores[p][g]
        print("%4d" % score)
