# Adott egy lista, és ennek elemeit kell kiírni vesszővel elválasztva.
# names = ["John Doe", "Jack Doe", "Jane Doe"]
# John Doe, Jack Doe, Jane Doe,
# Úgy módosítsuk az alkalmazást, hogy ne legyen lezáró vessző
# John Doe, Jack Doe, Jane Doe


# names = ["John Doe", "Jack Doe", "Jane Doe"]
# line = ""
# i = 0
# for name in names:
#     i += 1
#     if i != 1:
#         line += ", "
#     line += name
# print(line)

names = ["John Doe", "Jack Doe", "Jane Doe"]
line = ""
i = 0
for name in names:
    i += 1
    line += name
    if i != len(names):
        line += ", "
print(line)

for number in range(1, 101):
    if number % 15 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)