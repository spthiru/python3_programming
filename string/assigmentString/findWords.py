getWrd = str(input("Enter your input here: "))
blank = " "
newline = "\n"
count = 1

for x in getWrd:
   if x == blank or x == newline:
     count += 1

print("Given input have",count,"word")

