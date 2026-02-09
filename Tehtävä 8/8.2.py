import mysql.connector

def find_airports(iso_country):
    sql = f"SELECT airport.name, airport.type FROM airport, country WHERE country.iso_country = airport.iso_country and country.iso_country = '{iso_country}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    answer = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in answer:
            print(f'{row[0]}, {row[1]}')
    return

connection = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='root',
        password='Aaro22',
        autocommit=True
)

find_airports("FI")