import mysql.connector

def find_airport(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokenttä, jonka ICAO-koodi on {icao} on {rivi[0]}. Kyseinen sijaitsee paikassa {rivi[1]}.")
    return

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='root',
        password='Aaro22',
        autocommit=True
)

find_airport("EFHK")