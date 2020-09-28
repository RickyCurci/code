#!/usr/bin/python3
from random import *

cpu_num = []

bulls = 0
cows = 0

def generator(usr_num):


	for i in range(0, 4):
		cpu_num.append(randint(0, 9))

	usr_num = [int(usr_num[i]) for i in range(0, len(usr_num))]

	print(cpu_num)
	print(usr_num)

	for digit in cpu_num:
		for number in usr_num:
			if digit == number and cpu_num.index(digit) == usr_num.index(number):
				cows = cows + 1

				print(cows)
				print(bulls)

				generator()

			elif digit == number:
				bulls = bulls + 1

				print(cows)
				print(bulls)

				generator()

if __name__=='__main__':
	usr_num = input('Give me a number: ')
	generator(usr_num)
