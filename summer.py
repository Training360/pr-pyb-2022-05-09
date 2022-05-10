# Kérj be számokat a felhasználótól, egészen addig,
# míg nullát nem ad be. Írd ki a beadott számok
# összegét kilépéskor!

sum = 0
should_exit = False
while not should_exit:
    number = int(input("Adj meg egy számot!"))
    if (number != 0):
        print("Szám: " + str(number))
        sum += number
    else:
        should_exit = True
print(sum)