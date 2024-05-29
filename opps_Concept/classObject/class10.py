class Employee:

   def __init__(self, name, age):
      self.__name = name
      self.__age  = age

   def get_name(self):
      return (self.__name)

   def get_age(self):
      return (self.__age)

   def set_name(self, name):
      self.__name = name
      return

   def set_age(self, age):
      self.__age = age

   name = property(get_name, set_name, "name")
   age  = property(get_age, set_age, "age")

e1 = Employee("Bhavana", 10)

print(e1.name, e1.age)

e1.name = "aishu"
e1.age = 16

print(e1.name, e1.age)
