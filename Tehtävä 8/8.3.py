import mysql.connector
from geopy.distance import distance

def calculate_distance(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    answer = cursor.fetchall()
    return answer

connection = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='root',
        password='Aaro22',
        autocommit=True
)

icao1 = input('kirjoita ensimmäisen lentokentän ICAO koodi:').upper()
icao2 = input('kirjoita toisen lentokentän ICAO koodi:').upper()

calculate1 = calculate_distance(icao1)
calculate2 = calculate_distance(icao2)

if calculate1 and calculate2:
    etäisyys = distance(calculate1, calculate2).km
    print(f'Lentokenttien etäisyys on: {etäisyys:.2f} KM')
else:
    print('virhe! icao tunnukset ovat virheellisiä')