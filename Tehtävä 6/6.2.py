import random

def heitto(tahko):
    return random.randint(1, tahkot)

tahkot = int(input('Kerro heitettävän nopan maksimisilmäluku:'))

silmaluku = 0

while silmaluku != tahkot:
    silmaluku = heitto(tahkot)
    print(silmaluku)