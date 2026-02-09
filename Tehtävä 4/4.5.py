kerrat = 0
käyttäjätunnus = 'python'
salasana = 'rules'

while kerrat < 5:
    yritys1 = input('kirjoita käyttäjätunnus:')
    yritys2 = input('kirjoita salasana:')

    if yritys1 != käyttäjätunnus or yritys2 != salasana:
        print('väärä käyttäjätunnus tai salasana')
        kerrat += 1

    if yritys1 == käyttäjätunnus or yritys2 == salasana:
        print('kirjautuminen onnistui!')
        break