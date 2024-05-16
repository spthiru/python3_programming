def primeCheck(val:int):
   i = 1
   m = 0
   while i < val:
     if val % i == 0:
       m += 1;
     i += 1;
   if m < 2:
     return "prime Number";
   else : 
     return "not a prime Number"

a = int(input())
print(primeCheck(a))
