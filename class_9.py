# class MyClass:
#   x = 6
  
  
# p1 = MyClass()
# print(p1.x)

# p2 = MyClass()
# print(p2.x)


# class Person:
#     def xyz(self, name, age): 
#         self.name = name 
#         self.age = age
#         print(self)

# p1 = Person()
# p2 = Person()

# p1.xyz("John", 36)
# p2.xyz("Sumon", 25)

# print(p1.name)   
# print(p1.age)    
# print(p2.name)   
# print(p2.age)

# class Student:
#     def abc(self,name, age):
#         self.name = name
#         self.age = age
        
# s1 = Student()

# s1.abc("Sabbir", 22)
# print(s1.name)
# print(s1.age)
# print(s1)


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#     print(self)

#   def printname(self):
#     print(self.firstname, self.lastname)

# x = Person("John", "Doe")
# x.printname() 
# x2 = Person("Jane", "Doe")
# x2.printname()

# class Person:
#     def __init__(self, name, age): 
#         self.name = name 
#         self.age = age
#     def __str__(self):
#         return f"{self.name}({self.age})"
        
        
# p1 = Person("John", 36)

# print(p1)



# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()


# class Father:
#     home = "House"
#     car = "Toyota"
#     money = 1000000
    
# class Child(Father):
#     bike = "Yamaha"
#     money = 5000
    
# class child2(Father):
#     mobile = "iPhone"
#     money = 2000
    
# print(child2.car)


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2024)
# x.welcome()


# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   x.move()



# import datetime

# x = datetime.datetime.now()
# print(x) 

# import datetime

# x = datetime.datetime.now()

# print(x.year)
# print(x.strftime("%A")) 

# import datetime

# x = datetime.datetime(2020, 5, 17)

# print(x) 

# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)
# print(y)

# x = abs(-7.25)

# print(x) 

# x = pow(3, 3)

# print(x)

# import math

# x = math.sqrt(30)

# print(x) 


# import math

# x = math.ceil(1.4)
# y = math.floor(1.4)

# print(x) # returns 2
# print(y) # returns 1 


# import camelcase

# c = camelcase.CamelCase()

# txt = "hello world"

# print(c.hump(txt)) 


# try:
#   print(x)
# except:
#   print("An exception occurred")




