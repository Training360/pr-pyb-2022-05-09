for i in range(5):
    for c in "alma":
        print(str(i) + c)

# Írjátok ki a szorzótáblát
# Két ciklust kell egymásba ágyazni

line = ""
for i in range(1, 11):
    line += str(i)
print(line)

content = ""
for i in range(1, 11):
    for j in range (1, 11):
        result = i * j        
        if result < 10:
            content += " " * 3
        elif result < 100:
            content += " " * 2
        else:
            content += " "
        content += str(result)
    content += "\n"
print(content)

# Hozz létre egy listát, mely egész számokat tartalmaz!
# Írd ki az összegüket!
numbers = [43, 32, 43, 532, 32, 35, 32]
sum = 0
for number in numbers:
    sum += number
print(sum)

# Hozz létre egy listát, mely pozitív és negatív számokat is tartalmaz!
# Add össze csak a pozitív számokat!
# Példa: ciklusban feltétel

numbers = [-1, 0, +1, -1, 0, +1, -1]
sum = 0
for number in numbers:
    if number > 0:
        sum += number
print(sum)