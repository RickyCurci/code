#!/usr/bin/python
import requests
import json

url = "https://instagramdimashirokovv1.p.rapidapi.com/tagged/5821462185/optional"

headers = {
    'x-rapidapi-host': "InstagramdimashirokovV1.p.rapidapi.com",
    'x-rapidapi-key': "2bb1e28a55msh76c05157cf754edp1045a0jsn1e1d7fff8b9b"
    }

response = requests.request("GET", url, headers=headers)

Json = response.text
Python = json.load(Json)

print(Python)
