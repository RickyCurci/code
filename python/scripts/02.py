#!/usr/bin/python3

from random import *
import requests
import json

BASE_URL = 'https://api.covid19api.com/'
headers = {
    'headers': '5cf9dfd5-3449-485e-b5ae-70a60e997864'
}

states = ['italy','united-kindom','spain','china','russian','usa']
page = '''

|=======================================|
|               COVID-19                |
|---------------------------------------|
| [ITALY] => [1]    | [CHINA] => [4]    |
| [UK] => [2]       | [RUSSIAN] => [5]  |
| [SPAIN] => [3]    | [USA] => [6]      |
|---------------------------------------|
|R¹¢ĸyC↓¶¢¹_________|_________________|/|
|=======================================|

'''
print(page)
cursor = input(':>')
state = states[int(cursor) - 1]

def countries(state):
    RESPONSE = requests.get(BASE_URL+'dayone/country/'+state+'/status/confirmed').json()
    status = {

        'state': RESPONSE[len(RESPONSE) - 1]['Country'],
        'cases': RESPONSE[len(RESPONSE) - 1]['Cases']

    }
    print(status)


countries(state)
