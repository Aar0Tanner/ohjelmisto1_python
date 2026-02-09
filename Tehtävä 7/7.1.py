vuodenajat = ('talvi', 'kevät', 'kesä', 'syksy')


numero = int(input('kirjoita kuukauden numero(1-12), (ensimmäinen kuukausi on joulukuu):'))

if numero in range(1,4):
    print(vuodenajat[0])
elif numero in range(4,7):
    print(vuodenajat[1])
elif numero in range(7,10):
    print(vuodenajat[2])
else:
    print(vuodenajat[3])