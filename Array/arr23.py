a = int(input("Enter Yor element size : "))

import array as arr
b = arr.array('i',[])
i = 0
c = 0
while i < a:
 c = int(input("Enter element value : "))
 b.insert(i,c)
 i += 1

k = len(b) - 1
while k >= 0:
  print(b[k])
  k -= 1
