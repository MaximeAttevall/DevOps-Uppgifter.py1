import random

numbers = []
for x in range(10):
    numbers.append(random.randint(0, 20))


print(numbers)
numbers.sort()
print(numbers)
