from http.client import responses

import requests

response = requests.get("https://en.wikipedia.org/wiki/Game")
if response.status_code == 200:
    print("Wikipedia Page Found")
