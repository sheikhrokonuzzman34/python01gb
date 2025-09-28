# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)



# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple)) 


# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])



# x = ("apple", "banana", "cherry")
# print(type(x))
# y = list(x)
# print(type(y))

# y[1] = "kiwi"
# x = tuple(y)


# print(type(x))
# print(x) 

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)



# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist 

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x) 

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i]) 


# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


# thislist = ["orange", "mango", "kiwi","apple" ,"pineapple", "banana"]
# thislist.sort()
# print(thislist)


# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)


# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3) 


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1) 


# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)


# thisset = {"apple", "banana", "cherry"}
# print(type(thisset))
# print(thisset) 



# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(thisdict)
# print(type(thisdict))

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])

# thisdict =	{
#   "brand": "Ford",
#   "model": 2020,
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict) 
# print(len(thisdict))


# thisdict =	{
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# } 
# print(thisdict) 

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # x = thisdict["model"]
# x = thisdict.keys() 
# print(x)


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()
# v = car.values()

# print(v) #before the change

# car["color"] = "white"
# v = car.values()

# print(v) #after the change 
# print(car)



# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2025

# print(thisdict)


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict) 


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict) 


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict) 


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# thisdict.clear()
# for x in thisdict:
#   print(x) 

# for x in thisdict:
#   print(thisdict[x]) 

# for x in thisdict.values():
#   print(x)

for x in thisdict.keys():
  print(x) 