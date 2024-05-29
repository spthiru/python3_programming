class mypython:

   def __init__(myselfsp, name, age):

      myselfsp.name = name
      myselfsp.age  = age

   def myfun(sp):
      print(sp.name)

p1 = mypython("sp", 24)

p1.myfun()

p1.age = 40

print(p1.age)
