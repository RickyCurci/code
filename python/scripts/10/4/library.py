 #!/usr/bin/python3

import mysql.connector
import time

class message:

    def new(user, data, content):
        try:

            mydb = mysql.connector.connect(

                host = '2.235.240.156',
                user = 'root',
                password = 'Riccardo05'

            )

            cursor = mydb.cursor()
            cursor.execute("USE message")

            query = "INSERT INTO chat (user, data, content) VALUES (%s, %s, %s);"
            value = (user, data, content)

            cursor.execute(query, value)
            mydb.commit()

            print('[ * ]{ OK [ INSERT ]}')

        except:

            print('[ / ]{ ERROR [ INSERT ]}')


    def show():
        try:

            mydb = mysql.connector.connect(

                host = '2.235.240.156',
                user = 'root',
                password = 'Riccardo05'

            )

            cursor = mydb.cursor()
            cursor.execute("USE message")


            query = "SELECT * FROM chat"
            cursor.execute(query)

            for row in cursor:
                print(row)

        except:

            print('[ / ]{ ERROR [ CONNECTION ]}')


    def login(user):

        try:

            mydb = mysql.connector.connect(

                host = '2.235.240.156',
                user = 'root',
                password = 'Riccardo05'

            )

            cursor = mydb.cursor()
            cursor.execute("USE message")

            query = "INSERT INTO users (user) VALUES (%s);"
            value = (user)

            cursor.execute(query, value)
            mydb.commit()

            print('OK LOG')

        except:

            print('NO LOG')
