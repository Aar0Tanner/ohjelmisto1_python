leiviskät = int(input('anna leiviskät:'))
naulat = int(input('anna naulat:'))
luodit = int(input('anna luodit:'))

naulatsum = ((leiviskät * 20) + naulat)
luoditsum = ((naulatsum * 32) + luodit)
grammaluku = (luoditsum * 13.3)

grammat = grammaluku % 1000
kilogrammat = int(grammaluku / 1000)

print(f'{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa')