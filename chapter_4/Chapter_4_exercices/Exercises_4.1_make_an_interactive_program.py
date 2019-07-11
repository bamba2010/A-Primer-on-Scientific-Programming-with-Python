
# Copyright (c) 2019 Cheick Bamba
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
"""reading input from user using input function"""

F = input("Please enter a temperature in Fahrenheit:")
F = float(F)
"""Program that ask for user a temperature in Fahrenheit and convert it to degree celcius"""
C = (5./9) * (F-32)
print(C)