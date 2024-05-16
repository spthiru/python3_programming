digit = [str(x) for x in range(10)]
mystr = 'HE234LLO,PY935TH34ON'
char = []
for x in mystr:
   if x not in digit:
     char.append(x)
     newstr = ''.join(char)
print(newstr)
