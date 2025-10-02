# myfamily = {
#   "child1" : {"name" : "Emil","year" : 2004},
#   "child2" : {"name" : "Tobias","year" : 2007},
#   "child3" : {"name" : "Linus","year" : 2011}
# } 

# x = myfamily["child2"]["year"]
# print(x)


# class MyClass:
#   x = 5

# print(MyClass)


# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# } 


# thisdict = {"brand": "Ford","model": "Mustang","year": 1964}

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # print(thisdict["brand"])
# # x = thisdict.keys() 
# x = thisdict.values() 
# print(x) #before the change


# students = {
#     "S001": {
#         "name": "Alice",
#         "age": 21,
#         "courses": {
#             "math": {"grade": "A", "credits": 3},
#             "physics": {"grade": "B+", "credits": 4},
#         }
#     },
#     "S002": {
#         "name": "Bob",
#         "age": 22,
#         "courses": {
#             "math": {"grade": "B", "credits": 3},
#             "chemistry": {"grade": "A-", "credits": 4},
#         }
#     },
#     "S003": {
#         "name": "Charlie",
#         "age": 20,
#         "courses": {
#             "biology": {"grade": "A", "credits": 4},
#             "physics": {"grade": "B", "credits": 4},
#         }
#     }
# }

# # Accessing nested values
# print(students["S001"]["courses"]["math"]["grade"])  


# def add(x, y):
#     return x + y
  
# print(add(5, 3))


# x = lambda a, b : a + b
# print(x(5, 6)) 


# cars = ["Ford", "Volvo", "BMW"]

# print(type(cars))


# class MyClass:
#   x = 6
  
# p1 = MyClass()
# print(p1.x)

# p2 = MyClass()
# print(p2.x)


class Person:
    def xyz(self, name, age): 
        self.name = name 
        self.age = age
        print(self)

p1 = Person()
p2 = Person()

p1.xyz("John", 36)
p2.xyz("Sumon", 25)

print(p1.name)   
print(p1.age)    
print(p2.name)   
print(p2.age)