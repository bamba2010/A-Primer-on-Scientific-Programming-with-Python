# Copyright (c) 2019 Cheick Bamba
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
import calendar,sys,numpy as np, math
try:
    year= int(sys.argv[1])
    month= int(sys.argv[2])
    day = int (sys.argv[3])
except IndexError:
    print("You must supply year,month and day to the command line")
    sys.exit(1)
if np.ceil(math.log10(year))<4 and np.ceil(math.log10(month))!=1 and np.ceil(math.log10(day))!=1:
    raise ValueError("the year must be four digits")
c=calendar.weekday(year, month, day)
print(c)