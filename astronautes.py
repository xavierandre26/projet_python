import requests
import json

astronautes = requests.get("http://api.open-notify.org/astros.json").json()
print(astronautes)
for astronaute in astronautes["people"]:
    if astronaute["craft"] == "ISS":
        print(astronaute)