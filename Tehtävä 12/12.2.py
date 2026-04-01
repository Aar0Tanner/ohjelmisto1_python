import requests

def get_weather():
    api_key = ""
    city = input("Syötä paikkakunnan nimi: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=fi"

    try:
        ans = requests.get(url)
        json_ans = ans.json()

        if ans.status_code == 200:
            weather = json_ans['weather'][0]['description']
            temperature = json_ans['main']['temp']

            print(f"\nSää paikkakunnalla {city}:")
            print(f"Kuvaus: {weather}")
            print(f"Lämpötila: {temperature} °C")
        else:
            print(f"Virhe: Paikkakuntaa '{city}' ei löytynyt tai API-avain on virheellinen.")

    except Exception as e:
        print(f"Tapahtui virhe pyynnön aikana: {e}")

get_weather()