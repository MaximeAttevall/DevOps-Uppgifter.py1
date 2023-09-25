import os
import random


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return f"{self.number} of {self.suit}"


def create_deck():
    colours = ["Hearts", "Spades", "Clubs", "Diamonds"]
    deck = []
    for suit in colours:
        for number in range(1, 14):
            card = Card(number, suit)
            deck.append(card)
    random.shuffle(deck)
    return deck


def draw_cards(deck, num_cards):
    hand = random.sample(deck, num_cards)
    for card in hand:
        deck.remove(card)
    return hand


def points_in_hand(hand):
    points = 0
    for card in hand:
        if card.number == 1:
            ace_choice = input("what value would you like ace to have, 1/14: ")
            if ace_choice == "1":
                points += 1
            elif ace_choice == "14":
                points += 14
        else:
            points += card.number
    return points


def print_card(card):
    if card.number == 1:
        print(f"Ace of {card.suit}")
    elif card.number == 11:
        print(f"Jack of {card.suit}")
    elif card.number == 12:
        print(f"Queen of {card.suit}")
    elif card.number == 13:
        print(f"King of {card.suit}")
    else:
        print(card.number, "of", card.suit)


def main():
    deck = create_deck()
    drawn_hand = draw_cards(deck, 1)
    computer_hand = draw_cards(deck, 1)
    points = points_in_hand(drawn_hand)
    computer_points = points_in_hand(computer_hand)
    for card in drawn_hand:
        print_card(card)

    print("your points: ", points)
    print("Computers points: ", computer_points)

    if points > 21:
        print("The computer won, you lost...")
    elif computer_points > 21:
        print("The computer lost, you won!!!")
    elif points > computer_points:
        print("You won!!")
    elif points <= computer_points:
        print("You lost...")



if __name__ == "__main__":
    main()
