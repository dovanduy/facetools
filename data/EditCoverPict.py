#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import sys, mechanize
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

class Pict:
	def __init__(self):
		self.Main()
			
	def Change(self):
		try:
			file = open(self.file,'rb')
			cj = kuki('log/kuki')
			cj.load()
			print(W + '[' + G + '*' + W + '] uploading picture.')
			br = mechanize.Browser()
			br.set_handle_equiv(True)
			br.set_cookiejar(cj)
			br.set_handle_gzip(True)
			br.set_handle_redirect(True)
			br.set_handle_referer(True)
			br.set_handle_robots(False)
			br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
			br.addheaders = [('User-Agent', open('UserAgent/ua.txt').read())]
			br.open('https://mbasic.facebook.com/photos/upload/?cover_photo')
			br._factory.is_html = True
			br.select_form(nr=0)
			br.form.add_file(file, 'image/jpeg', self.file, name='file1')
			sub = br.submit().read()
			if "Apa yang Anda pikirkan sekarang?" in str(sub):
				print(W +'[' + G + '*' + W + '] successfully changed')
			else:
				print(W +'[' + R + '*' + W + '] '+R+'failed')
		except (mechanize.URLError):
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
		except FileNotFoundError:
			print(W + '[' + R + '!' + W + '] ' + R + 'photo not found!')
			sys.exit()
			
	def Main(self):
		self.file = input(W + '\n[' + G + '?' + W + '] file photo : '+G)
		self.Change()

Pict()