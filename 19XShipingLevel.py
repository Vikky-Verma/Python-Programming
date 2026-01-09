def shipping_level(*args, **kwargs):
  for arg in args:
    print(arg, end=" ")
  print()
  # for value in kwargs.value():
  #   print(value, end=" ")
  if "apt" in kwargs:
    print(f"{kwargs.get('street')} {kwargs.get('apt')}")
  elif "pobox" in kwargs:
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('pobox')}")
  else:
    print(f"{kwargs.get('street')}")

  print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")



shipping_level("Dr.", "Spongebob",   "Squarepants", "III",
street ="123 Fake St.", 
pobox ="PO box #1001",
city="Detroit",
state="MI", 
zip="48201")