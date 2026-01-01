#Exercise 2 Shoping cart Program

item = input("What item would you like to buy?: ")
price = float(input("Waht is the price?: "))
quantity = int(input("How many would you like?: "))
total =price*quantity

print(f"You have bought {quantity} X {item}/s")
print(f"Your total is: ${total}")