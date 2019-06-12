# creatibg a tuple
t = (2, 4, 6, "temp.pdf")
print(t)
# tuple with no parenthesis
t1 = 2, 4, 6, "temp.pds"
for i in t:
    """looping through tuple"""
    print(i)
print(t1)
t2 = t + t1
"""adding two tuples"""
print(t2)

"""slicing with tuples"""
print(t[1])
print(t[2:])
