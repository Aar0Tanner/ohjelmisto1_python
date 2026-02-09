import random

N = 1000000
kerrat = 0
n = 0

while kerrat < N:
    arpax = random.uniform(-1,1)
    arpay = random.uniform(-1,1)
    yhtalo = arpax ** 2 + arpay ** 2

    if yhtalo < 1:
        n += 1
    kerrat += 1

pii = n * 4 / N
print(pii)