kuha = float(input('kerro kuhan pituus senttimetreinä:'))
pituuserotus = (37 - kuha)
if kuha < 37:
    print(f'laske kuha järveen, kuhan pitää olla {pituuserotus} senttimetriä pitempi')
else:
    print('kuha on tarpeaksi pitkä!')