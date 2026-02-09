import math

def hintalaatu(halkaisia, euro):
    m2 = math.pi * (halkaisia / 100)
    return euro / m2

pizza1 = float(input('Kerro pitsan halkaisian senttimetrimäärä:'))
hinta1 = float(input('Kerro pitsan hinta:'))

pizza2 = float(input('Kerro pitsan halkaisian senttimetrimäärä:'))
hinta2 = float(input('Kerro pitsan hinta:'))

eka = hintalaatu(pizza1, hinta1)
toka = hintalaatu(pizza2, hinta2)

#print(f'{eka:.2f}')
#print(f'{toka:.2f}')

if eka < toka:
    print(f'ensimmäinen pitsa on halvempi, sen hinta on {eka:.2f} €/m2')
elif toka < eka:
    print(f'toinen pitsa on halvempi, sen hinta on {toka:.2f} €/m2')
elif eka == toka:
    print(f'molemmat pitsat ovat samanhintaisia, niiden hinnat ovat {eka:,2f} €/m2')