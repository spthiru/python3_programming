a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
c = int(input("Enter c value:"))


def maxThree(x ,y ,z):
   if x > y and x > z :
      return x;
   elif y > z and y > x:
      return y;
   else:
     return z;
print("maximum value is :", maxThree(a, b, c))
