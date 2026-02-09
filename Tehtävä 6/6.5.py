def pariton(lista):
    lista2 = []

    for i in lista:
        if i % 2 == 0:
            lista2.append(i)

    return lista2

luvut = [1, 2, 3, 4, 5, 6]

luvut2 = pariton(luvut)

print(luvut)
print(luvut2)