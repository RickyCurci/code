#!/usr/bin/python

from random import *
import requests
import json

BASE_URL = 'https://api.nytimes.com/svc/'
API_KEY = 'nyK2hJFeWGsMijWmGrkNLc0CmhljxKV8'

def topstories():
    section = 'science'
    RESPONSE = requests.get(BASE_URL+'topstories/v2/'+section+'.json?api-key='+API_KEY).json()
    print(len(RESPONSE['results']))
    for i in range(0, randint(0,len(RESPONSE['results']))):
        print(RESPONSE['results'][i]['title'])
    #PYTHON = json.load(JSON)

topstories()
