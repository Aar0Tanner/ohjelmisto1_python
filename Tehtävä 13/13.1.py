from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/alkuluku/<int:luku>')
def isPrime(luku):
    try:
        alkuluku = True
        if luku < 2:
            alkuluku = False
        else:
            for i in range(2, int(luku ** 0.5) + 1):
                if luku % i == 0:
                    alkuluku = False
                    break

        vastaus = {
            "Number": luku,
            "isPrime": alkuluku
        }

    except Exception:
        vastaus = {
            "status": 400,
            "teksti": "Virheellinen syöte"
        }
        return jsonify(vastaus), 400

    return jsonify(vastaus)

@app.errorhandler(404)
def page_not_found(virhe):
    vastaus = {
        "status": 404,
        "teksti": "Sivua ei löytynyt"
    }
    return jsonify(vastaus), 404


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)