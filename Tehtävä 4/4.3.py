lista = []

while True:
    numero = input('kirjoita luku:')
    if numero == '':
        break
    lista.append(float(numero))
print(min(lista), max(lista))