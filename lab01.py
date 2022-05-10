# Írd ki egymás után 5x a neved!
for i in range(5):
    print("Trainer")

# Írd ki egymás utána a neved 5x, de írj elé sorszámot is! Pl.:
# A sorszám és a pont között ne legyen space!
# 0. Trainer
# 1. Trainer
# 2. Trainer

for i in range(5):
    # print(i, ". Trainer", sep="")
    # print(str(i) + ". Trainer")
    print(f"{i}. Trainer")


# Írd ki egymás utána a neved 5x, írj elé sorszámot is, de egytől!
# for i in range(5):
#    print(f"{i + 1}. Trainer") 

# for i in range(5):
#     j = i + 1
#     print(f"{j}. Trainer") 

# i = 1
# while i <= 5:
#     print(f"{i}. Trainer")
#     i += 1

for i in range(1, 6):
    print(f"{i}. Trainer")

# Írd ki az első 10 pozitív egész számot, és mellé annak négyzetét!
# 1 - 1
# 2 - 4
# 3 - 9

for i in range(1, 11):
    print(f"{i} - {i ** 2}")

# Hónapok! Írd ki az első 6 hónapra a következőt!
# Az év 1. hónapja január.
# Az év 2. hónapja február.
# months = ["január", "február", "március"]
# Tipp: kell egy számlálót tartalmazó egész változó, amit 
# növelgetsz a ciklusban.

i = 1
month_list = ["január", "február", "március", "április"]
for month in month_list:
    print(f"Az év {i}. hónapja {month}.")
    # print("Az év ", i, ". hónapja ", month, ".", sep="")
    i += 1

word = "almakörte"
for character in word:
    print(character)