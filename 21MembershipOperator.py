# Membership Operator = uesd to test  whether a value or variable is found in a sequence (string, list, tuple, or dictionary)

#  1. in
#  2. not in


# string
# word = "APPLE" 

# letter = input("Guess a letter in the seceret word: ")

# if letter in word:
#   print(f"There is a {letter}")
# else:
#   print(f"{letter} was not found")

# if letter  not in word:
#   print(f"{letter} was not found")
# else:
#   print(f"There is a {letter}")



# Set
# students = {"Spongebob", "Patrick",
# "Sandy"}  
# student = input("Enter the name of a student: ")

# if student in students:
#   print(f"{student} is student")
# else:
#   print(f"{student} is not a student")

# if student  not in students:
#   print(f"{student} is not a student")
# else:
#   print(f"{student} is student")
  
  
  

# Dictionary
# grades = {"Spongebob": "A", "Patrick": "B", "Sandy": "C"}

# student = input("Enter the name of a student: ")

# if student in grades:
#   print(f"{student}'s grade is {grades[student]}")
# else:
#   print(f"{student} was not found")



email = "BroCode@gmail.com"

if "@" in email and "." in email:
  print("Valid email")
else:
  print("Invalid email")