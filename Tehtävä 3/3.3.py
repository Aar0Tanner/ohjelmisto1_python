sukupuoli = input('kerro biologinen sukupuolesi: ').lower()
hemoglobiini = float(input('kerro hemoglobiiniarvosi (g/l): '))

if sukupuoli == "mies":
    if hemoglobiini < 134:
        print('hemoglobiiniarvosi ovat alhaiset')
    elif hemoglobiini > 195:
        print('hemoglobiiniarvosi ovat korkeat')
    else:
        print('hemoglobiiniarvosi ovat normaalit')

elif sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("hemoglobiiniarvosi ovat alhaiset")
    elif hemoglobiini > 175:
        print("hemoglobiiniarvosi ovat korkeat")
    else:
        print("hemoglobiiniarvosi ovat normaalit")

else:
    print("virhe")
