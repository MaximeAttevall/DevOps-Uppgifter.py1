#10.2
import os

text_file = "numbers.txt"

open_file = open(text_file, "r")
numbers = open_file.read()

numbers_to_look_for = "0123456789"
for number in numbers_to_look_for:
    print(numbers.count(number))