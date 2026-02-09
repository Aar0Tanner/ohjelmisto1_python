n = int(input('kerro luku:'))

if n < 1:
    print('ei ole alkuluku')
else:
    alkuluku = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            alkuluku = False
            print('ei ole alkuluku')
            break
    if alkuluku:
        print('On alkuluku')
