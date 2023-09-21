import random

numbers = []

for x in range(10):
    numbers.append(random.randint(0, 9))


def get_even(list):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

print(numbers)
print(get_even(numbers))