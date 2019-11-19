#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, requests

global W, G, R
if sys.platform in ['linux','linux2']:
	W = '\033[0m'
	G = '\033[1;92m'
	R = '\033[1;91m'
else:
	W = ''
	G = ''
	R = ''
	
def Main():
	try:
		r = requests.get('https://graph.facebook.com/v5.0/me/groups?access_token='+str(token),headers = HD)
		for i in r.json()['data']:
			print(W + '[' + G + '•' + W + '] ID   : ' + G + str(i['id']))
			print(W + '[' + G + '•' + W + '] Name : ' + G + str(i['name']))
			print(W + '-'*45)
	except KeyError:
		print(W + '[' + R + '!' + W + '] ' + R + 'error when grabbing group id!')
		sys.exit()
	except requests.exceptions.ConnectionError:
		print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
		sys.exit()
try:
	print('')
	print(W + '-'*45)
	token = open('log/token').read()
	HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
	Main()
	sys.exit()
except Exception as E:
	print(W + '[' + R + '!' + W + '] ' + R + str(E))
	sys.exit()