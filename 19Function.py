# function = A block of reusable code 
#           place () after the  function name to invoke it


# def happy_birthday(name, age):
#   print(f"Happy birthday to {name}!")
#   print(f"You are {age} years old!")
#   print("Happy birthday to you!")
#   print()

# happy_birthday("John", 20)


# def display_invoice(username, amount, due_date):
#   print(f"Hello {username},")
#   print(f"Your bill of ${amount:.2f} is due: {due_date}.")

# display_invoice("Alice", 150.75, "2024-07-15")


# return = statement used to end a function and send a result back to the caller

# def add_numbers(a, b):
#   return a + b

# def multiply_numbers(x, y):
#   return x * y

# def subtract_numbers(m, n):
#   return m - n

# def divide_numbers(p, q):
#   if q != 0:
#     return p / q
#   else:
#     return "Error: Division by zero"
  
# print(add_numbers(5, 3))    


# def create_name(first, last):
#   first = first.capitalize()
#   last = last.capitalize()
#   return first + " " + last

# full_name = create_name("Vikky", "Verma")
# print(full_name)



# deafult arguments = A default value for certain parameters default is used when that argument is omitted make your function more flexible , reduces  # of arguments 
# 1. positional, 2.Default, 3. keyword, 4. arbitrary

def net_price(list_price, discount=0, tax = 0.05):
  return list_price * (1-discount) *(1+ tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))