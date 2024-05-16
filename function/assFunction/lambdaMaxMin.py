def sort(data):
   i = 0
   while i < len(data):
      if data[i]<data[i+1]:
        data[i] = data[i+1]
      i +=1
   return data

sorting = lambda arg1: sort(arg1);

list = [10,34,2,5,25,99]
print(value = sorting(list))
