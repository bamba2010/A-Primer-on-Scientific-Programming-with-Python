# Copyright (c) 2019 Cheick Bamba
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)


def read_densities(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])
        if len(words[:-1]) == 2:
            substance = words[0] + " " + words[1]
        else:
            substance = words[0]
        densities[substance] = density
    infile.close()
    return densities


read = read_densities("/home/cheick/Documents/densities.txt")
print(read)
