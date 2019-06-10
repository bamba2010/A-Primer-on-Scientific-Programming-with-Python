# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

from math import pi
h = 5 # height
b = 2 # base
r = 1.5 # radius
area_parallelogram = h*b
print (' The area of the parallelogram is %.3f' % (area_parallelogram))
area_square = b**2
print('The area of the square is %g' %(area_square))
area_circle = pi*r**2
print('The area of the circle is % .3f'%(area_circle))
volume_cone = 1.0/3*pi**r*2*h
print('The volume of the cone is %.3f' % (volume_cone))
