# Írd ki a felhasználónak a következőt!

# Mit akarsz csinálni?
# 1. Két számot összeadni
# 2. Két számot kivonni

# Ha a felhasználó 1-est ír be, akkor kérd be a két számot, és add össze!
# Ha a felhasználó 2-est ír be, akkor kérd be a két számot, és vond ki!
# Ha a felhasználó egyebet ír be, akkor írd ki, hogy ismeretlen művelet!

menu = """
Mit akarsz csinálni?

1. Két számot összeadni
2. Két számot kivonni
"""

print(menu)
answer = input("")

if answer == "1" or answer == "2":
    n1 = int(input("Első szám?"))
    n2 = int(input("Második szám?"))

if answer == "1":    
    print(f"Összegük: {n1} + {n2} = {n1 + n2}")
elif answer == "2":
    print(f"Különbségük: {n1} - {n2} = {n1 - n2}")
else:
    print("Nem ismert művelet")