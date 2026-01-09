import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# number = random.randint(low, high) # Generate a random integer between low and high (inclusive)

# number = random.random() # Generate a random float between low and high

# option = random.choice(options) # Randomly select an item from a list or tuple

random.shuffle(cards) # Shuffle the items in a list in place



print(cards)