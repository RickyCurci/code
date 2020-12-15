import os
import requests


class robot:

	def github(username, password):

		data = {'username': username, 'password': password}
		request = requests.post('https://github.com/login', data = data)
	 		print(request)

		if request == True:
			print('*[{01} GITHUB]* => COMPLETE')

robot.github('RickyCurci','27Cinque2005')
