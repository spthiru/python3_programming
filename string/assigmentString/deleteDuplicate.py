getStr = str(input("Enter your input here : "))

print(getStr)
count = 0

for x in getStr:
  for y in getStr:
     if x == y :
       count += 1
  if count <= 1:
   print(x, end ="")
  count = 0 
print() 
