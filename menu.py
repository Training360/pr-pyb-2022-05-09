# Kérjünk be a felhasználótól egész számokat, addig,
# amíg nullát nem ír be!

# DRY

# Fejlesszük tovább az alkalmazást, hogy ha nullát ad meg, akkor
# ne írja ki a számot, hanem azt írja ki, hogy exit!

# number = 10
# while not number == 0:
#     number = int(input("Adj meg egy számot!"))
#     if not number == 0:
#         print(f"A szám: {number}")
#     else:
#         print("Exit")

# while True:
#     number = int(input("Adj meg egy számot!"))
#     print(number)
#     if number == 0:
#         break
# print("End")


should_input_number = True
while should_input_number:
    number = int(input("Adj meg egy számot!"))
    if number != 0:
        print(f"A szám: {number}")
    else:
        print("Exit")
        should_input_number = False
print("End")