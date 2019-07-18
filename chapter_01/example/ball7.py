# Copyright (c) 2019 Cheikh Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

v0 = 5  # initial vlocity
g = 9.81  # acceleration of gravity
t = 0.6  # time
y = v0 * t - 0.5 * g * t ** 2  # vertical position
print(
    """ At t={t:f} s, a ball with initial velocity v0 = {v0:.3E} m/s is located at the height {y:.2f} m.""".format(t=t,
                                                                                                                   v0=v0,
                                                                                                                   y=y))
