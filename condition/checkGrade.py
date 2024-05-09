mark = int(input("Enter your mark:"))
result = ""
if mark >= 90 and mark <= 100:
	result = "A+ Grade"
elif mark >= 65 and mark <= 89:
	result = "A Grade"
elif mark >= 50 and mark <= 64:
	result = "B Grade"
elif mark >= 35 and mark <= 49:
	result = "C Grade"
else :
    result = "Arrear"
print("Your Grade : ", result)
