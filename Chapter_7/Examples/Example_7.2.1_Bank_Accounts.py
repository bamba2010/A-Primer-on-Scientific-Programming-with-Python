# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

from classes import Account
a1 = Account('John Olosson', '19371554951', 20000)
a2 = Account('Liz Olosson', '19371564711', 20000)
a1.deposit(1000)
a1.withdraw (4000)
a2.withdraw(10500)
a1.withdraw(3500)
print('a1 balance is :'a1.balance)