# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
import  matplotlib.pyplot as plt
def read_densities(filename):
    infile = open(filename, 'r')
    x_axis = []
    y_axis = []
    for line in infile:
        words = line.split()
        print(words)
        x = float(words[0])
        y = float(words[1])
        x_axis.append(x)
        y_axis.append(y)
    plt.plot(x_axis, y_axis, label="x versus y")
    plt.legend()
    plt.show()
    infile.close()
    return x_axis,y_axis


read = read_densities("/home/cheick/read_two_column.txt")
print(read)
