mark = int (input("Enter your mark : "))

result =""
if mark > 35:
   result = "passed the examination"
elif mark > 75:
   result = "passed with distiction"
elif mark < 35:
   result = "fail"
else:
   result = "pass"

print(result)
