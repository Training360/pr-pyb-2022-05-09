# Kérj be a felhasználótól egy egész számot! Majd amennyiben páros,
# írd ki neki, hogy páros! Ha páratlan, írd ki neki, hogy páratlan!

# n = int(input("Adj meg egy egész számot!"))
# if n % 2 == 0:
#     print("Páros")
# else:
#     print("Páratlan")

# Kérj be a felhasználótól egy másik egész számot! Amennyiben nagyobb mint,
# nulla, írd ki, hogy pozitív! Ha nulla, írd ki, hogy nulla! Ellenkező esetben,
# írd ki, hogy negatív!

# n = int(input("Adj meg egy egész számot!"))
# if n > 0:
#     print("Pozitív")
# elif n == 0:
#     print("Nulla")
# else:
#     print("Negatív")

# Kérd be a felhasználó nevét! Ha nem írja be, akkor ír ki, hogy 
# "ez nem volt szép!"! name == ""

# name = input("Mi a neved?")
# if (name == ""):
#     print("Ez nem volt szép!")

# Nagyon szorgalmi: egész szám-e, vagy lebegőpontos - csak tanult megoldással
answer = input("Adj meg egy számot!")
# Karakterenként, és van-e benne pont
if int(float(answer)) == float(answer):
    print("Egész")
else:
    print("Lebegőpontos")