import requests
import json

astronautes = requests.get("http://api.open-notify.org/astros.json")
print(astronautes.json())