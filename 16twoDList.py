groceries = [["apple", "orange", "banana", "coconut"], ["celery", "carrots", "potatoes"] ,["chicken", "fish", "turkey"]]

# print(groceries)

for collection in groceries:
  for food in collection:
    print(food, end=" ")
  print()