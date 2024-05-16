getString = str(input("Enter your input here : "))
digit = [str(x) for x in range(10)]

for x in getString:
  if x not in digit:
    print(x, end="")

print()
