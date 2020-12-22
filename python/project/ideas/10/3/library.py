#!/usr/bin/python3

import mysql.connector
import time

class reminders:

    def listselect(title):

        mydb = mysql.connector.connect(

            host = '2.235.240.156',
            user = 'root',
            password = 'Riccardo05'

        )

        cursor = mydb.cursor()
        cursor.execute('USE reminders')
        cursor.execute("SELECT * FROM "+str(title)+";")

        for item in cursor:
            print(item)

    def additem(title, content, data):

        try:

            mydb = mysql.connector.connect(

                host = '2.235.240.156',
                user = 'root',
                password = 'Riccardo05'

            )

            cursor = mydb.cursor()
            cursor.execute('USE reminders')

            query = "INSERT INTO "+title+"(status, content, data) VALUES('[  ]',"+content+","+data+");"
            cursor.execute(query)
            print('[ OK ]{ INSERT }')

        except:

            print('[ // ]{ INSERT [ ERROR ]}')
