def summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

luvut = [6, 9, 6, 7]

tulos = summa(luvut)

print("Listan summa on:", tulos)
