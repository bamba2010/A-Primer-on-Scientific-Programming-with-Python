Cdegrees = [-10, -5, 0, 5, 10, 20, 25, 30, 34]
for c in range(len(Cdegrees)):
    """traversing elements of a list and changing them"""
    Cdegrees[c] += 5
print(Cdegrees)


for i, c in enumerate(Cdegrees):
    """tranversing list elements using enumerate"""
    Cdegrees[i] = c + 5
print(Cdegrees)