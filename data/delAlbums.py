#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import sys, time, requests, json

global W, G, R, Y
if sys.platform in ['linux','linux2']:
	W = '\033[0m'
	G = '\033[1;92m'
	R = '\033[1;91m'
	Y = '\033[1;93m'
else:
	W = ''
	G = ''
	R = ''
	Y = ''

class DelAlbums:
	def __init__(self):
		self.token = open('log/token').read()
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.Main()
		
	def Main(self):
		try:
			print(W + '\n[' + G + '*' + W + '] Get albums id... ')
			
			r = requests.get('https://graph.facebook.com/me?fields=albums.limit(5000)&access_token=' + self.token,headers = self.HD)
			a = json.loads(r.text)
				
			print()
			for result in a['albums']['data']:
				s = requests.post('https://graph.facebook.com/' + result['id'] +'?method=delete&access_token=' + self.token, headers = self.HD).text
				if 'true' in str(s):
					print(W + '[' + G + '~' + W + '] ' + G + result['name']+ R + ' >> ' + W + 'success deleted')
				else:
					print(W + '[' + R + '×' + W + '] ' + G + result['name']+ R + ' >> ' + W + 'failed')
						
		except KeyError:
			print(W + '[' + R + '!' + W + '] ' + R + 'error!')
			sys.exit()
			
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
try:
	DelAlbums()
	exit(W + '\n[' + G + '•' + W + '] done!')
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()