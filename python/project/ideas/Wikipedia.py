#!/usr/bin/python3

import wikipedia

def search(iteam):

    result = wikipedia.page(iteam)
    print(result.title)
    print(result.content)
search('Github')
