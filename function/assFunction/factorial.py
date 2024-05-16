def factorial(val):
   i = 1;
   total = 1;
   while i <= val:
     total *= i
     i += 1
   return total
a = int (input ("Enter number of factorial u want : "))
print("factorial of ", a, "is", factorial(a))
