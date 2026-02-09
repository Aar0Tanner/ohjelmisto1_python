# funktio lisää uuden lentokentän sanakirjaan
def lisaa():
    icaoinput = input('kerro lentokentän icao tunnus:').upper()
    kenttainput = input('kerro lentokentän nimi:')
    lentoasemat[icaoinput] = kenttainput
    print('tiedot ollaan tallennettu tietokantaan')
    return

#funktio hakee lentokentän tiedot
def hae():
    icao = input('kirjoita lentokentän icao tunnus:').upper()
    if icao in lentoasemat:
        print('lentoaseman nimi on: ', lentoasemat[icao])
    else:
        print('lentoasemaa ei löydy tietokannasta')
    return


#tulostaa valinnat
def tulosta():
    print('\nValitse toiminto:')
    print('1 = lisää uusi lentoasema:')
    print('3 = hae lentoasema icao tunnuksella:')
    print('9 = lopeta:')
    return

lentoasemat = {}

while True:
    tulosta()
    valinta = int(input('valintasi:'))
    if valinta == 1:
        lisaa()
    elif valinta == 3:
        hae()
    elif valinta == 9:
        print('ohjelma lopetettu.')
        break
    else:
        print('tuntematon toiminto')