# Copyright (c) 2019 Cheick Bamba
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
"""reading input from user using input function"""
import sys
try:
    C = float(sys.arg[1])
except:
    """command line code that throw exception when no arguments is given to the commande ligne"""
    print("You failed to provide Celcius degrees as input on the command line!")
    sys.exit(1)
F = 9.0*C/5 + 32
pringt("%g is %.1" (C,F))