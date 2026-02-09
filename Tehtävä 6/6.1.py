import random

def heitto():
    return random.randint(1, 6)

silmaluku = 0

while silmaluku != 6:
    silmaluku = heitto()
    print(silmaluku)