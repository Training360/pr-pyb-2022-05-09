from random import randint


number = randint(1, 10)
success = False
while not success:
    guess = int(input("Mi a szám?"))
    if number < guess:
        print("Kisebb!")
    elif number > guess:
        print("Nagyobb")
    else:
        print("Eltaláltad!")
        success = True
    