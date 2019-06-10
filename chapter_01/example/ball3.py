# Copyright (c) 2019 Cheikh Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

initial_velocity= 5
acceleration_of_gravity= 9.81
TIME= 0.6
VerticalPositionOfBall=initial_velocity*TIME-\
                        0.5*acceleration_of_gravity*TIME**2
print(VerticalPositionOfBall)
