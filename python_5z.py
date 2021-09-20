from random import randint

numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
length = len(numbers)
rand_n = randint(0, length)
print(numbers[rand_n - 1])
