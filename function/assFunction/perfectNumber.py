def perfectNum(val):
   i = 1
   m = 0
   while i < val:
     if val % i == 0:
       m += i
     i += 1
   if m == val :
     return "perfect Number";
   else :
     return "not Perfect Number"; 

a = int(input("Enter the value to check perfect or not : "))
print(perfectNum(a))
