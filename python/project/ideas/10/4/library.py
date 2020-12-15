#!/usr/bin/python3

import mysql.connector
import time

class users:

    def singup(name):

        try:

            mydb = mysql.connector.connect(

                host = '2.235.240.156',
                user = 'Riccardo_Curci',
                password = '402cinque2020settembre12'

            )

            cursor = mydb.cursor()
            cursor.execute("USE message")


            cursor.execute('SELECT * FROM users;')
            for nickname in cursor:

                if name == nickname:
                    print('[ / ]{ ERROR [ USER ALREADY EXIST ]}')

                elif name != nickname:

                     query = "INSERT INTO users (nickname) VALUES (%s)"
                     value = (user)


                     cursor.execute(query, value)
                     mydb.commit()

                     print('[ * ]{ SINGUP [ OK ]}')


        except:

            print('[ / ]{ ERROR { CONNECTION | SINGUP }')




class message:

    def new(data, user, content):

        try:

            mydb = mysql.connector.connect(

                host = '2.235.240.156',
                user = 'Riccardo_Curci',
                password = '402cinque2020settembre12'

            )

            cursor = mydb.cursor()
            cursor.execute("USE message")

            query = "INSERT INTO chat (data, content) VALUES (%s, %s, %s)"
            value = (data, user, content)

            cursor.execute(query, value)
            mydb.commit()

            print('[ * ]{ INSERT }')

        except:
            print('[ / ]{ ERROR [ INSERT ]}')


    def show():

        try:

            mydb = mysql.connector.connect(

                host = '2.235.240.156',
                user = 'Riccardo_Curci',
                password = '402cinque2020settembre12'

            )

            cursor = mydb.cursor()
            cursor.execute("USE message")


            query = "SELECT * FROM chat"
            cursor.execute(query)

            for row in cursor:
                print(row)

        except:
            print('[ / ]{ ERROR [ CONNECTION ]}')
