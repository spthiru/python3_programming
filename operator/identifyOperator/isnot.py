a = [1,2,3,4,5]
b = [1,2,3,4,5]

c = a
a = b
print(a is not c)
print(b is not a)
