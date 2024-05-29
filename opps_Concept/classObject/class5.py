class scl:

   def __init__(self, name = "sp", age =18):
      self.name = name
      self.age  = age

   def displayscl(self):
     print("Name : ", self.name, "Age : ", self.age)

e1 = scl()
e2 = scl("vishanth", 80)

e1.displayscl()
e2.displayscl()
