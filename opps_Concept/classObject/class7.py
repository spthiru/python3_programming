class scl:

   def __init__(self, name, age, salary):
      self.name   = name
      self._age    = age
      self.salary = salary

   def display(self):
      print("Name : ", self.name, "Age : ", self.age, "Salary : ", self. salary)

e1 = scl("Linux", 39, 10000)

print(e1.name, "\n", e1._age, "\n", e1.salary)
