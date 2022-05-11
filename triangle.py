# Bónusz feladat: beadunk a classify_triangle() függvénynek három számot, és a függvény visszaadja, hogy
# szerkeszthető-e belőle háromszög, és az derékszögű-e, egyenlő szárú-e, vagy szabályos-e (stringként)

def classify_triangle(a, b, c):
    if nem_szerkesztheto(a, b, c):
        return "nem szerkeszthető háromszög"
    if szabalyos(a, b, c):
        return "szabályos"
    if derekszogu(a, b, c):
        if (egyenlo_szaru(a, b, c)):
            return "derékszögű egyenlő szárú"
        else:
            return "derékszögű általános"
    else:
        if (egyenlo_szaru(a, b, c)):
            return "egyenlő szárú"
        else:
            return "általános"

def nem_szerkesztheto(a, b, c):
    return a + b < c or a + c < b or b + c < a

def szabalyos(a, b, c):
    return a == b and b == c

def derekszogu(a, b, c):
    return pitagoras(a, b, c) or pitagoras(a, c, b) or pitagoras(b, c, a)

def pitagoras(x, y, z):
    return absolute((x ** 2 + y ** 2) - (z ** 2)) < 0.00005

def absolute(n):
    if n < 0:
        return -n
    else:
        return n

def egyenlo_szaru(a, b, c):
    return a == b or a == c or c == b

#print(classify_triangle(1, 2, 4))
#print(classify_triangle(2, 2, 2))
#print(classify_triangle(3, 4, 5))
#print(classify_triangle(4, 5, 6))
#print(classify_triangle(4, 4, 5))
print(classify_triangle(1, 1, 2 ** 0.5))