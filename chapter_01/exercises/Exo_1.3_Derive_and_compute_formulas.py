# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

# convert 10^9 s to years

a = 365.0
j = 24.0
m = 60.0
n = 60.0

second_to_year = (10**9)/(a*j*m*n)
print(second_to_year)
# a new born can live more than 10^9 s 

""""""""
# use online convertor

# https://www.unitjuggler.com/convert-time-from-s-to-yr-365.html?val=1000000000
