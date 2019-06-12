Cdegrees = [-10, -5, 0, 5, 10, 20, 25, 30, 34]
Fdegrees = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
for i in range(len(Cdegrees)):
    """iterating through two lists using a for loop"""
    print("%5d %5.1f" % (Cdegrees[i], Fdegrees[i]))

print("Using the zip function")

Cdegrees = [-10, -5, 0, 5, 10, 20, 25, 30, 34]
Fdegrees = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
""" using zip() to go through two lists"""
for c, f in zip(Cdegrees, Fdegrees):
    print("%5d %5.1f" % (c, f))
