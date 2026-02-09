import  random

arpa = random.randint(1, 10)

while True:
    arvaus = int(input('kirjoita luku 1 ja 10 välillä:'))
    if arvaus < arpa:
        print('luku on liian pieni')
    elif arvaus > arpa:
        print('luku on liian iso')
    elif arvaus == arpa:
        print('Oikea luku!')
        break