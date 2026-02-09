lista = []

numero = input('kirjoita luku, tai lopeta painamalla enter:')

while numero != '':
    lista.append(int(numero))
    numero = input('kirjoita luku, tai lopeta painamalla enter:')

lista.sort(reverse=True)

print('viisi suurinta lukua suuruusjärjestyksessä:')
for luku in lista[:5]:
    print(luku)
