while True:
    cm = float(input('kirjoita senttimetri muutettavaksi:'))
    inch = cm * 2.54
    if cm < 0:
        break
    print(f'{cm} senttimetriä on {inch} tuumaa')