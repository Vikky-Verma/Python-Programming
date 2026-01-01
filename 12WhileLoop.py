# while loop = exexute some code WHILE some condition remains true

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#   print(f"You like {food}")
#   food = input("Enter a food you like (q to quit): ")

# print("Bye")


num = int(input("Enter a # between 1 - 10:"))

while num < 1 or num > 100:
  print(f"{num} is not valid")
  num = int(input("Enter a # between 1 - 10:"))

print(f"Your number is {num}")