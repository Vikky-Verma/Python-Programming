# collection = single "variable" used to store multiple values

# List  = [] ordered and changeable , Duplicates OK

# Set = {} unorderd and immutable , but  Add/Remove OK. No duplicates

# Tuple = () orderd and unchangeable. Duplicates OK, Faster

# LIST

# fruits = ["apple", "orange", "banana", "coconut"]

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0,"pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("banana"))

# print(fruits[0])
# print(fruits[0:2])
# print(fruits[::2])


# print(fruits)
# for x in fruits:
#   print(x)


# SET
# fruits = {"apple", "orange", "banana", "coconut" ,"coconut"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)  # return true or false

# fruits.add("pineapple")  # at random places
# fruits.remove("apple") # from random places
# fruits.pop() # from random places
# fruits.clear()

# print(fruits)


# TUPLE
fruits = ("apple", "orange", "banana", "coconut" ,"coconut")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)  # return true or false

# print(fruits.index("apple"))
# print(fruits.count("coconut"))


# print(fruits)
for fruit in fruits:
  print(fruit)

