# creating a list
c = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
# adding new element to a list using append
c.append(3)
print(c)
# adding two list
c = c + [8, 9, 11]
print(c)
# deleting element from list
del c[2]
print(c)
# lenght of list
print(len(c))
# index of a element in the list
print(c.index(10))
# checking if an element exist in a list
print(2 in c)
# return element from the buttom of a list

print(c[-1])
# automating adding element to list with while loop

C = []
c_value = 50
c_max = 200
while c_value <= c_max:
    C.append(c_value)

    c_value += 5
print(C)
