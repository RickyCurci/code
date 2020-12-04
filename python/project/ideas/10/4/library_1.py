#!/usr/bin/python3

import mysql.connector
import time


mydb = mysql.connector.connect(

    host = '2.235.240.156',
    user = 'root',
    password = 'Riccardo05',

)

cursor = mydb.cursor()
cursor.execute("USE message")


class message:

    def new(title, data, content):

        try:

            query = "INSERT INTO chat (title, data, content) VALUES ( %s, %s, %s)"
            value = (title, data, content)

            cursor.execute(query, value)
            print('[ * ]{ INSERT }')

        except:
            print('[ / ]{ ERROR [ INSERT ]}')


    def show():

        query = "SELECT * FROM chat"
        cursor.execute(query)

        for row in cursor:
            print(row)
