# Iterables = An object/Collection can return its elements one at a time, allowing it to be iterated over in a loop.

# numbers = [1, 2, 3, 4, 5] # list

# for number in numbers:
#   print(number, end=" ")

# print()

# for number in reversed(numbers):
#   print(number, end=" ")



# numbers = (1, 2, 3, 4, 5) # tuple

# for number in numbers:
#   print(number, end=" ")

# print()

# for number in reversed(numbers):
#   print(number, end=" ")



# fruits = {"apple", "orange", "banana", "coconut"} # set

# for fruit in fruits:
#   print(fruit, end=" ")

# print()

# for fruit in reversed(fruits):
#   print(fruit, end=" ") # sets are unordered, so reversed() may not give expected results



# name = "Vikky Verma" # string
# for char in name:
#   print(char, end=" ** ")


my_dictionary = {"A": 1, "B": 2, "C": 3} # dictionary
for key in my_dictionary:
  print(key, end=" ")
print()
for value in my_dictionary.values():
  print(value, end=" ")
print()
for key, value in my_dictionary.items():
  print(f"{key} = {value}", end=" ")
