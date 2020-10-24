#!/usr/bin/python3
from selenium import webdriver
from random import *

import socket

class tool:

	def port_scanner(HOST, PORT):
#       ports = [21, 22, 23, 24, 80, 88, 443,]
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
#           for port in range(0, 100):
#				PORT = port #ports[port]

			conn = s.connect((HOST, PORT))
			print('['+str(PORT)+'] => OPEN')


		except:
			print('['+str(PORT)+'] => CLOSED')

	def brute_force():
		passowords = []
		list = open('password_lst.txt')

		for row in list:
			passowords.append(row)

		fp = webdriver.FirefoxProfile()
		# Here "2" stands for "Automatic Proxy Configuration"
		fp.set_preference("network.proxy.type", 2)
		fp.set_preference("network.proxy.autoconfig_url","http://proxy-address-here:8080/") 
		driver = webdriver.Firefox(firefox_profile=fp)
		browser.get('http://seleniumhq.org/')

tool.brute_force()
