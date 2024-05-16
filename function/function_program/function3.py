def sp (arg):
   print(id (arg))
   arg = arg + 1
   print(id (arg))
var = 10
print(id(var))
sp(var)
print(var)   
