# Írjatok egy is_not_negative() nevű logikai függvényt, ami
# True-t ad vissza, ha a szám nagyobb vagy egyenlő,
# mint nulla!

from random import randint


def is_not_negative(number):
    return number >= 0

# Írjatok egy olyan get_circle_area() nevű függvényt,
# melynek átadva a kör sugarát, visszaadja annak területét!
# r^2*pi

def get_circle_area(r):
    return r ** 2 * 3.14

# Írjatok egy olyan get_rectangle_area() nevű függvényt,
# ami visszaadja, a két oldalhossz alapján a téglalap területét!

def get_rectangle_area(a, b):
    return a * b

# Írjatok egy olyan absolute() nevű függvényt, ami visszaadja a 
# paraméterként megadott szám abszolútértékét!

def absolute(number):
    if number >= 0:
        return number
    else: 
        return -number

# Írj egy sum_numbers() függvényt, ami paraméterül kap számok listáját,
# és visszaadja a számok összegét!

def sum_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

# Írj egy roll_dice() függvényt, ami visszaad egy véletlenszerű 1-6 közötti egész számot!

def roll_dice():
    return randint(1, 6)

def count_positive_numbers(numbers):
    """Írj egy count_positive_numbers() függvényt, ami paraméterül kap egész számok listáját,
       és visszaadja, hogy hány pozitív szám van benne!"""
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count

def print_numbers(list):
    for i in list:
        print(i)

numbers = [1, 2, 3, 4]
print_numbers(numbers)


print(absolute(5))
print(absolute(-10))

print(sum_numbers([1, 2, 3, 4, 2, 3]))

print(roll_dice())

print(count_positive_numbers([-1, 1, -1, 1, -1, -1]))