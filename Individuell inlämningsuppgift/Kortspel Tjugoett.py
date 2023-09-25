import json
import random
import os

value_cards = open("card.json", "r")

if os.path.exists("cards.json"):
    notes = json.load(value_cards)
value_cards.close()

# Function to generate a random card
def get_random_card():
    colour = ["Heart", "Clover", "Spade", "Diamond"]
    card_value = random.randint(1, 14)
    colour = random.choice(colour)
    return f"{card_value} of {colour}s"


ui_width = 30
print(".: Cardgame 21 :.".center(ui_width))
print("-" * ui_width)
print(" exit | Exit program")
print("-" * ui_width)

hand = []

for cards in range(2):
    card = get_random_card()
    hand.append(card)
    print(f"You drew: {card}")


while True:
    action = input("Would you like a new card? (yes/no) > ").lower()
    if action == "yes":
        card = get_random_card()
        hand.append(card)
        print(f"You drew: {card}")
    elif action == "no":
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


print("Your hand:")
for card in hand:
    print(card)


#FAIL ATTEMPT