#!/usr/bin/python3
def crypting(key):

    string = 'Ciao come stai spero bene'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    string = string.lower()

    new_string = []

    alphabet = [alphabet[i] for i in range(0,len(alphabet))]
    string = [string[i] for i in range(0,len(string))]

    for i in range(0, key):
        alphabet.append(alphabet[i])
    for i in range(0, key):
        alphabet.remove(alphabet[i])

    print(alphabet)
    for digit in string:

        for letter in alphabet:


            if digit == letter:

                for number in range(0,key):
                    position = alphabet.index(digit)
                    print(position)

                    if (position + key + 1) >= len(alphabet) + number:
                        new_string.append(alphabet[number])
                    else:
                        new_string.append(alphabet[position + key])



            elif digit == ' ' or digit == '!' or digit == '"' or digit == '?':
                new_string.append(digit)


    print(new_string)

crypting(3)
