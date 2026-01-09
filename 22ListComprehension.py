# List Comprehension = A concise way to create lists in python 
# Compact and easier to read than traditional loops
# [expression for value in iterable if condition]


# doubles = []
# for x in range(1, 11):
#   doubles.append(x * 2)

# print(doubles)



# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# square = [z ** 2 for z in range(1, 11)]
# print(doubles)
# print(triples)
# print(square)



# fruits = ["apple", "banana", "cherry", "kiwi", "mango", "watermelon"]

# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)


# if condition
# numbers = [1, -2, 3, -4, 5, -6]
# positive_nums = [num for num in numbers if num>=0]
# negative_nums = [num for num in numbers if num<0]
# even_nums = [num for num in numbers if num%2==0]
# odd_nums = [num for num in numbers if num%2!=0]
# print(positive_nums)  # [1, 3, 5]
# print(negative_nums)  # [-2, -4, -6]
# print(even_nums)      # [-2, -4, -6]
# print(odd_nums)       # [1, 3, 5]



grades = [85, 92, 78, 90, 88, 76, 95]
passing_grades = [grade for grade in grades if grade >= 80]
print(passing_grades)  # Output: [85, 92, 90,