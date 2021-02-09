#!/usr/bin/python3
from random import *

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = [alphabet[i] for i in range(0, len(alphabet))]


special_char = [' ','.',',',';',':','!','?','(',')']

class txt:

    def crypt(key, source):

        crypt_txt = []
        text = open(source)

        for rows in text:
            letters = [rows[i] for i in range(0, len(rows))]


        letters.remove(letters[-1])
        print(letters)


        letters.remove('.')
        letters.remove(letters[0])

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

    def decrypt(source):

        old_txt = []
        text = open(source)

        for rows in text:
            letters = [rows[i] for i in range(0, len(rows))]



        letters.remove(letters[-1])
        print(letters)

        key = alphabet.index(letters[0])
        letters.remove('.')
        letters.remove(letters[0])

        for letter in letters:
            for digit in alphabet:
                if digit == letter:

                    old_txt.append(alphabet[alphabet.index(digit) - key])

        text = ''.join(old_txt)
        print(text)


txt.crypt(2, 'source.txt')
