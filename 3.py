import random

tab = []
x = 0
for i in range(0, 10):
    a = random.randint(0, 59)
    tab.append(a)
    i += 1
print("To teraz się pobawimy")
print(tab)
print("Dodaję losowe 3 parzyste liczby")

for i in range(0, 3):
    a = random.randrange(0, 59, 2)
    tab.append(a)
    i += 1
print(tab)
print("Teraz usunę losowe 3 liczby nieparzyste:")

for i in range(0, 13):
    if tab[i-x] % 2 != 0 and x<3 :
        tab.pop(i-x)
        x += 1
    i += 1
print(tab)
print("A teraz zmienię element 5 i 10")

tab.insert(5,3)
tab.insert(10,33)

print(tab)