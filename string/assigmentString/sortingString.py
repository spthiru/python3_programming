mystr = "ZXYA"
#print(int(mystr,2)) 
for x in mystr:
   for y in mystr:
     if mystr[x] < mystr[y]:
       k = mystr[x]
       mystr[y] = mystr[x]
       mystr[x] = k
   print(x,y)    
