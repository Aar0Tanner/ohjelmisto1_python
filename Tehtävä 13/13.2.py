from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

@app.route('/lentokenttä/<icao>')
def find_country(icao):
    db_user = os.environ['DB_USER']
    db_pass = os.environ['DB_PASS']
    try:
        yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user=db_user,
            password=db_pass,
            autocommit=True
        )

        sql = f"SELECT name FROM airport WHERE ident = '{icao}'"
        print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if kursori.rowcount > 0:
            for rivi in tulos:
                vastaus = {
                    "ICAO": icao,
                    "Name": rivi[0],
                }
                return jsonify(vastaus)

    except Exception:
        vastaus = {
            "status": 400,
            "teksti": "Virheellinen syöte"
        }
        return jsonify(vastaus), 400

@app.errorhandler(404)
def page_not_found(virhe):
    vastaus = {
        "status": 404,
        "teksti": "Sivua ei löytynyt"
    }
    return jsonify(vastaus), 404


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)