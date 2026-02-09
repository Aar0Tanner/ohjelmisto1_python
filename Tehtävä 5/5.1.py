import random

nopat = int(input('kerro arpakuutioiden määrä:'))
summa = 0

for i in range(nopat):
    luku = random.randint(1, 6)
    summa += luku

print(summa)