# range(start, stop, step)

Cdegrees = []
for C in range(-20, 45, 5):
    Cdegrees.append(C)
print(Cdegrees)

Cdegrees = []
for i in range(0, 21):
    """since range cannot support floating point"""
    c = -10 + i * 2.5
    Cdegrees.append(c)
print(Cdegrees)
