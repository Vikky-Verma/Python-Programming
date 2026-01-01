
# name = input("Enter your full name: ")
phone_number = input("Enter your phone #: ")

# result = len(name)  # find the length 
# result = name.find("i") # first occurrence 
# result = name.rfind("i") # last occurrence 
# name = name.capitalize() # first letter capatilise
# name = name.upper() # all character capital
# name = name.lower()  # all character small 
# result = name.isdigit() # return string is digit or not
# result = name.isalpha() #  return all is alphabet or not
# result = phone_number.count("-")
phone_number = phone_number.replace("-" , " ")

print(phone_number)