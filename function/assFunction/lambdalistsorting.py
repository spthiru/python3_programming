sorting = lambda arg1,arg2:arg1<arg2;

a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
value = sorting(a,b)
if value == 1:
  print("a is less than b");
  print("b is bigger than a");
else:
  print("b is less than a");
  print("a is bigger than b");
