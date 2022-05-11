def print_employee(name="Anonymous", year_of_birth=2000):
    print(f"A {name} dolgozó {year_of_birth}-ben született.")
    print("Fizetése legyen 200000 Ft")


def add(a, b):
    return a + b


def is_even(number):
    if number % 2 == 0:
        return "páros"
    else:
        return "páratlan"

def print_is_even(number):
    if number % 2 == 0:
        print("páros")
    else:
        print("páratlan")

# True-t ad vissza, hogyha a paraméter páros, ellenkező esetben False-t

def is_even_number(number):
    return number % 2 == 0
    

print_employee("John Doe", 1980)
print("***")
jack = "Jack Doe"
print_employee(jack, 1985)
print("***")
lastname = "Doe"
firstname = "Jane"
print_employee(firstname + " " + lastname, 1990)

name = "John Smith"
print_employee(name, 1995)


print_employee("Jane Smith")
print_employee()


sum = add(8, 10)
print(sum)

print(add(8, 10))

print(add(add(5, 6), 10))

print(add(3, 2) + 2)

print(is_even(8))

print("***")

print_is_even(8)
print_is_even(11)