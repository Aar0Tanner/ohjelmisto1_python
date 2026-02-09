vuosi = int(input('kirjoita vuosiluku:'))

if vuosi % 400 == 0 or vuosi % 100 != 0 and vuosi % 4 == 0:
    print('vuosi on karkausvuosi')
else:
    print('vuosi ei ole karkausvuosi')