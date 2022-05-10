from random import randint, random, randrange, shuffle, choice

number = random()
number = randrange(0, 10)
number = randint(3, 6)
print(number)

numbers = ["a", "b", "c", "d"] 
print(choice(numbers))

shuffle(numbers)
print(numbers)