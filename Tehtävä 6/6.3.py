def litra(bensa):
    return bensa * 3.785

maara = float(input('Kerro bensiinin määrä nestegalloonoina:'))

while maara >= 0:
    muunnos = litra(maara)
    print(f'{muunnos} litraa')
    maara = float(input('Kerro bensiinin määrä nestegalloonoina:'))