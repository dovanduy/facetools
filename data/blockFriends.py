#!usr/bin/python3.7
#Author: DulLah ©2019
# FB : fb.me/dulahz
#Telegram : t.me/unikers
#github: github.com/dz-id

import sys, requests, json
from data import cekKuki
from bs4 import BeautifulSoup as parser
from http.cookiejar import LWPCookieJar as kuki

global W, G, R
if sys.platform in ['linux','linux2']:
	W = '\033[0m'
	G = '\033[1;92m'
	R = '\033[1;91m'
else:
	W = ''
	G = ''
	R = ''

class Block:
	def __init__(self):
		cekKuki.cek(self)
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.token = open('log/token').read()
		self.url = 'https://mbasic.facebook.com{}'
		self.req = requests.Session()
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.id = []
		self.Main()
		
	def Main(self):
		try:
			
			r = requests.get('https://graph.facebook.com/me/friends?access_token=' + self.token,headers = self.HD)
			a = json.loads(r.text)
			
			print()
			for result in a['data']:
				data = []
				
				rr = self.req.get(self.url.format('/privacy/touch/block/confirm/?bid=' + str(result['id'])),headers = self.HD)
				bs = parser(rr.content,'html.parser')
				self.id.append(result['id'])
				
				for x in bs('form'):
					if '/privacy/touch/block/id/?' in x['action']:
						data.append(x['action'])
						break
					
				for x in bs('input'):
					try:
						if 'fb_dtsg' in x['name']:
							data.append(x['value'])
						if 'jazoest' in x['name']:
							data.append(x['value'])
							break
					except: pass
				
				if len(data) == 3:
					url = self.url.format(data[0])
					form = {'fb_dtsg' : data[1], 'jazoest' : data[2], 'confirmed' : 'Blokir'}
					b = self.req.post(url, data = form, headers = self.HD)
					if b.status_code == 200:
						print(W + '[' + G + '-' + W + '] ' + G + str(result['name']) + W + ' - bloked')
					else:
						print(W + '[' + R + 'x' + W + '] ' + G + str(result['name']) + W + ' - failed')
				else:
					print(W + '[' + R + 'x' + W + '] ' + G + str(result['name']) + W + ' - failed')
			
			if len(self.id) == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'no friends found!')
				sys.exit()
					
		except requests.exceptions.ConnectionError:
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
try:
	print(W + '\n[' + G + '*' + W + '] Get user id... ')
	Block()
	print(W + '\n[' + G + '•' + W + '] done!')
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()