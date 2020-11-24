#!/usr/bin/python3
from random import *

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = [alphabet[i] for i in range(0, len(alphabet))]


special_char = [' ','.',',',';',':','!','?']

class txt:

    def crypting(key, source):

        crypt_txt = []
        text = open(source)

        for rows in text:
            letters = [rows[i] for i in range(0, len(rows))]


        for letter in letters:
            for digit in alphabet:

                if digit == letter:
                    crypt_txt.append(alphabet[alphabet.index(digit) + key])

            for char in special_char:
                if char == letter:
                    crypt_txt.append(char)

        text = str(alphabet[key])+'.'+''.join(crypt_txt)
        print(text)
        # KEY = alphabet[key] EX: [KEY = 2] KEY = alphabet[2] = 'c'

    def decrypt(cry_txt):
        cry_txt = [cry_txt[i] for i in range(0, len(cry_txt))]
        old_txt = []

        key = alphabet.index(cry_txt[0])
        cry_txt.remove('.')
        cry_txt.remove(cry_txt[0])
        for letter in cry_txt:
            for digit in alphabet:
                if digit == letter:

                    old_txt.append(alphabet[alphabet.index(digit) - key])

        txt = ''.join(old_txt)
        print(txt)
        
