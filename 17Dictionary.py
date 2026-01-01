# dictionary = a collection of  {key: value} pairs ordered and changeable. No duplicate members.

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("India"))
# print(capitals.get("Japan"))

# if capitals.get("Japan"):
#     print("That capiatal exists")
# else:
#     print("That capital doesn't exists")


# capitals.update({"Germany": "Berlin"})  # adds item to the dictionary

# capitals.update({"USA": "Detroit"})
# capitals.pop("China") # removes item with specified key

# capitals.popitem() # removes last item

# capitals.clear() # removes all items




# keys = capitals.keys()  # returns a list of all keys in the dictionary
# for key in capitals.keys():
#     print(key)

# values = capitals.values()  # returns a list of all values in the dictionary
# for value in capitals.values():
#     print(value)

items = capitals.items()  # returns each item in the dictionary
for key, value in capitals.items():
    print(f"{key}: {value}")


