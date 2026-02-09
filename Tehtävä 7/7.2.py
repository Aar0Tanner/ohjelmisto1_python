setti = set()

userinput = input('kirjoita nimi:')

while userinput != '':
    if userinput in setti:
        print('VIRHE! Nimi on jo listassa, kirjoita uusi nimi.')
    else:
        setti.add(userinput)
        print('nimi lisätty.')
    userinput = input('kirjoita nimi:')

for nimi in setti:
    print(nimi)