import mysql.connector

def find_country(iso_country):
    sql = f"SELECT name, continent FROM country where iso_country = '{iso_country}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokenttä, jonka ICAO-koopip3 install mysql-connector-python --userdi on {iso_country} sijaitsee maassa {rivi[0]}. Kyseinen maa sijaitsee maanosassa: {rivi[1]}")
    return

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='root',
        password='Aaro22',
        autocommit=True
)

find_country("FI")