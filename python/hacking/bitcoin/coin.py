from random import *
import mysql.connector

class coin:

    def create():

        values = []
        for i in range(0, 24):
            values.append(randint(0, 100000))
            time.sleep(86400)

        for i in values:
            value = values[i]
            time.sleep(3600)

        print(value)


coin.create()
