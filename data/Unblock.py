#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import sys, requests
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

class UnBlock:
	def __init__(self):
		cekKuki.cek(self)
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.url = 'https://mbasic.facebook.com{}'
		self.req = requests.Session()
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.Main()
	
	def Excute(self,id):
		try:
			data = []
			a = self.req.get(self.url.format(id),headers = self.HD)
			bs = parser(a.content, 'html.parser')
			
			for x in bs('form'):
				if '/privacy/touch/unblock/write/?' in x['action']:
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
				form = {'fb_dtsg' : data[1], 'jazoest' : data[2], 'confirmed' : 'Buka Blokir'}
				b = self.req.post(url, data = form, headers = self.HD).text
				ids = id.replace('/privacy/touch/unblock/confirm/?unblock_id=','')
				if 'Anda telah menghapus blokir' in str(b):
					print(W + '[' + G + '-' + W + '] user_id - ' + G + str(ids) + W + ' - unbloked')
				else:
					print(W + '[' + R + 'x' + W + '] user_id - ' + G + str(ids) + W + ' - failed')
			else:
				print(W + '[' + R + 'x' + W + '] user_id - ' + G + str(ids) + W + ' - failed')
					
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
	
	def Main(self):
		try:
			
			r = self.req.get(self.url.format('/privacy/touch/block/'),headers = self.HD)
			bs = parser(r.content, 'html.parser')
			
			if 'Batalkan Blokir' in str(bs):
				print()
				for i in bs.find_all('a',string = 'Batalkan Blokir'):
					self.Excute(i['href'])
			else:
				print(W + '[' + R + '!' + W + '] ' + R + 'no account blocked found!')
				sys.exit()
		
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
try:
	print(W + '\n[' + G + '*' + W + '] Get user id... ')
	UnBlock()
	print(W + '\n[' + G + '•' + W + '] done!')
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()