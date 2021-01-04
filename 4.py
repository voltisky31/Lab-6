n = int(input("Podaj liczbę n: "))

dzielnik = 1

tab = []

while dzielnik <= n:

    if n%dzielnik==0:

        tab.append(dzielnik)

    dzielnik += 1

print(tab)