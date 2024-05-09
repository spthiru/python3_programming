a = int (input("Enter the a value : "))
b = int (input("Enter the b value : "))

print("press 1 for add")
print("press 2 for sub")
print("press 3 for mul")
print("press 4 for div")
print("press 5 for mod")
print("press 6 for exit")

c = int (input("Enter the c value : "))
if(c == 1):
   print(a+b)
if(c == 2):
   print(a-b)
if(c == 3):
   print(a*b)
if(c == 4):
   print(a/b)
if(c == 5):
   print(a%b)
if(c == 6):
   exit(0);
