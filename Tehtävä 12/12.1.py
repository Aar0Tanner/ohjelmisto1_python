import requests

req = "https://api.chucknorris.io/jokes/random"

try:
    ans = requests.get(req)
    if ans.status_code == 200:
        json_ans = ans.json()
        print(json_ans["value"])

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
