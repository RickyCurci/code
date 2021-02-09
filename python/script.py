from random import *
import wikipedia
import request
import json


class  script:

    # /scripts/01 | nyt api system
    def nyt(section):

        base_url = 'https://api.nytimes.com/svc/'
        api_key = 'nyK2hJFeWGsMijWmGrkNLc0CmhljxKV8'

        section = section
        response = requests.get(base_url+'/topstories/v2/'+section+'.json?api-key='+api_key).json()
        print(len(response['results']))
        for i in range(0, randint(0,len(response['results']))):
            print(response['results'][i]['title'])


        #PYTHON = json.load(JSON)

    # /scripts/02 | covid19 case counter
    def covid19():

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

        RESPONSE = requests.get(BASE_URL+'dayone/country/'+state+'/status/confirmed').json()
        status = {

            'state': RESPONSE[len(RESPONSE) - 1]['Country'],
            'cases': RESPONSE[len(RESPONSE) - 1]['Cases']

            }

        print(status)

        # /scripts/03 | exchange update
        def exchange(first, second):

            VALUE = []

            payload = {'base': first, 'symbols': second}
            response = requests.get('https://api.exchangeratesapi.io/latest', params=payload)

            #Json DATA to Python DATA
            Json = response.text
            Python = json.loads(Json)

            #Value Conversion
            RATES = Python
            Convert_Rate = RATES['rates'][second]

            Quantity = int(input('QUANTITY: '))
            Convert_Rate = Convert_Rate * Quantity
            print(str(Quantity)+ ' ' + first + ' in ' + second + ' is rate ' + str(Convert_Rate))


        # /scripts/04 | wikipedia
        def wikipedia(iteam):

            result = wikipedia.page(iteam)
            print(result.title)
            print(' ')
            print(result.content)

        # /scripts/05 | password generator
        def password(lentgh):

            Letter = "ABCDEFGHIKLMNOPQRSTVXYZabcdefghiklmnopqrstuvxyz123456789#@"
            Char =  [Letter[int(i)] for i in range(0, len(Letter))]

            Limit = lenght

	        Password = []
	        for i in range(0,57):
		              Range = randint(0,55)
		              Element = Char[Range + 2]
		              Password.append(Element)


            Password.reverse()
	        Password = Password[0: Limit]
	        Password = "".join(str(i) for i in Password)
            print("YOUR PASSWORD IS: ",Password)

        # /scripts/06 | morse translate
        def morse(sentece):
            DataBase = {

               "A": ".-",
    	       "B": "-...",
    	       "C": "-.-.",
    	       "D": "-..",
    	       "E": ".",
    	       "F": "..-.",
    	       "G": "--.",
    	       "H": "....",
    	       "I": "..",
    	       "J": ".---",
    	       "K": "-.-",
    	       "L": ".-..",
    	       "M": "--",
    	       "N": "-.",
    	       "O": "---",
    	       "P": ".--.",
    	       "Q": "--.-",
    	       "R": ".-.",
    	       "S": "...",
    	       "T": "-",
    	       "U": "..-",
    	       "V": "...-",
    	       "W": ".--",
    	       "X": "-..-",
    	       "Y": "-.--",
    	       "Z": "--..",
    	       "1": ".----",
    	       "2": "..---",
    	       "3": "...--",
    	       "4": "....-",
               "5": ".....",
    	       "6": "-....",
    	       "7": "--...",
    	       "8": "---..",
    	       "9": "----.",
    	       "0": "-----",
    	       " ": "/"

           }

           SENTENCE = sentence
           X = SENTENCE
           X = [X[int(i)] for i in range(0, len(X))]

           SENTENCE = []

           for i in X:
               SENTENCE.append(DataBase[i])

               SENTENCE = ' '.join(str(i) for i in SENTENCE)

            print(SENTENCE)
