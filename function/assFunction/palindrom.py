def palindrome(val):
   c = len(val)
   j = c-1
   i = 0
   m = 0 
   while i < c :
     if val[i] == val[j]:
        m += 1
     j -= 1
     i += 1
   if m == c :
     return "palindrome"
   else :
     return "not a palindrome" 

checkNum = str(input("Enter string to find palindrome or not : "))
print(palindrome(checkNum))
