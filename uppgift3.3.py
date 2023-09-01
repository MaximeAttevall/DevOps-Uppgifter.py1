import random

# Define the ASCII art for each number on the dice
DICE_ART = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘",
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘",
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘",
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘",
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘",
    ),
    6: (
        "┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘",
    ),
}

while True:
    # Roll the dice (generate a random number between 1 and 6)
    dice = random.randint(1, 6)

    # Ask the user if they want to roll the dice
    a = input("Would you like to roll the dice? (yes/no): ")

    if a.lower() == 'yes':
        # Display the ASCII art for the rolled number
        print("\nYou rolled a", dice)
        for line in DICE_ART[dice]:
            print(line)
    elif a.lower() == 'no':
        print("Okay, thanks for playing!")
        break
    else:
        print("Please enter 'yes' or 'no'.")
