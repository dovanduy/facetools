#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import sys, requests, time
from data import cekKuki
from bs4 import BeautifulSoup as parser
from http.cookiejar import LWPCookieJar as kuki

global W, G, R
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

class Overload:
	def __init__(self):
		cekKuki.cek(self)
		self.req = requests.Session()
		s = self.req
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.font = open('font.txt').read()
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.Main()
		
	def Main(self):
		try:
			data = []
			print(W + '\n[' + R + '!' + W + '] before continue please connect to the Spanish VPN')
			input(W + '[' + G + '*' + W + '] press enter.. ')
			time.sleep(2)
			print(W + '[' + G + '*' + W + '] please wait ')
			qq = self.req.get('https://mbasic.facebook.com/profile/edit/info/nicknames/?info_surface=info')
			bb = parser(qq.content, 'html.parser')
			for i in bb('form'):
				if '/profile/edit/info/save/fieldwithtextanddropdown/?' in i['action']:
					data.append(i['action'])
					break
			for i in bb('input'):
				try:
					if 'fb_dtsg' in i['name']:
						data.append(i['value'])
					if 'jazoest' in i['name']:
						data.append(i['value'])
					if 'additional_types[705456762826020]' in i['name']:
						data.append(i['value'])
						break
				except: pass
			if len(data) == 4:
				url = 'https://mbasic.facebook.com'+str(data[0])
				form = {'fb_dtsg' : data[1], 'jazoest' : data[2], 'additional_types[705456762826020]' : data[3], 'dropdown' : 'nickname', 'text' : self.font, 'checkbox' : 'checkbox', 'save' : 'Simpan'}
				s = self.req.post(url, data = form, headers = self.HD)
				if s.status_code == 200:
					print(W + '[' + G + '*' + W + '] success.')
					print(W + '[' + G + '•' + W + '] done!')
					sys.exit()
				else: print(W + '[' + R + '*' + W + '] failed please try again.')
			else: print(W + '[' + R + '*' + W + '] failed please try again.')
		except requests.exceptions.ConnectionError:
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
Overload()