end = int(input("Enter how many number u want :"))

a = 0
b = 0
c = 1
i = 0
print("0")
while i <= end :
  a = b + c
  c = b
  b = a
  print(b)
  i += 1
