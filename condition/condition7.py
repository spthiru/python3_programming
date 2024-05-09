month = int (input("Enter number of the month : "))
result = ""

if month == 1:
  result = "January"
elif month == 2:
  result = "February"
elif month == 3:
  result = "March"
elif month == 4:
  result = "April"
elif month == 5:
  result = "May"
elif month == 6:
  result = "June"
elif month == 7:
  result = "July"
elif month == 8:
  result = "Aguest"
elif month == 9:
  result = "September"
elif month == 10:
  result = "October"
elif month == 11:
  result = "November"
elif month == 12:
  result = "December"
else:
  result = "Enter vaild number"
print(result)
