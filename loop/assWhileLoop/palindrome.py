value = int(input("Enter the number to find palindrome : ")) 

result = ""
number = int(value)
number1 = int(value)
  
div = int(0)
mod = int(0)
y = int(1)

while value >= 1:
  y = y*10;
  value = int(value / 10)
   
div1 = int(0)
add = int(1)
s = int(0)
y = int (y/10)

while number >= 1:
 mod = number % 10
 number = int(number /10)
 add = mod * y
 s = s + add
 y = int(y/10)

if number1 == s:
   result = "palindrome"
else :
   result = "not palindrome"
   
print(result)
