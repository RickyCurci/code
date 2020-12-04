import requests
import json

url = 'https://freegeoip.app/json'
headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.get(url, headers=headers).text
location = response

print(location)
