a = int(input("Enter your array size : "))

import array as arr
b = arr.array('i',[])

i = 0
c = 0
while i < a :
  c = int(input("Enter the element value : "))
  b.insert(i,c)
  i += 1

print(b)
y = 0
l = 0
while y < a:
   m = 0
   while m < a:
     if b[y] < b[m] :
       l = b[m]
       b[m] = b[y]
       b[y] = l
     m += 1
   y += 1

print(b)
