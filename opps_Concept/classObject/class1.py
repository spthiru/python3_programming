class scl:
   
   def __init__(self, name, age):
      self.name = name
      self.age  = age

   def display(self):
      print("Name : ", self.name, "Age : ", self.age)

print(scl.__doc__)
print(scl.__name__)
print(scl.__module__)
print(scl.__bases__)
print(scl.__dict__)
