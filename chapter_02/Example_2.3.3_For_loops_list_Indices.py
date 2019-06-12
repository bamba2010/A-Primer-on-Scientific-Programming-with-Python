n = 21
C_min = -10
C_max = 40
dc = (C_max - C_min) / float(n - 1)
Cdegrees = [0] * n
for i in range(len(Cdegrees)):
    """ range() and len()"""
    Cdegrees[i] = -10 + i * dc
print(Cdegrees)





Fdegrees = [0] * n
for i in range(len(Cdegrees)):
    Fdegrees[i] = (9.0 / 5) * Cdegrees[i] + 32
print(Fdegrees)
