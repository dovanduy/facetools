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

class Bio:
	def __init__(self):
		self.Main()
			
	def Change(self):
		try:
			cj = kuki('log/kuki')
			cj.load()
			br = mechanize.Browser()
			br.set_handle_equiv(True)
			br.set_cookiejar(cj)
			br.set_handle_gzip(True)
			br.set_handle_redirect(True)
			br.set_handle_referer(True)
			br.set_handle_robots(False)
			br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
			br.addheaders = [('User-Agent', open('UserAgent/ua.txt').read())]
			br.open('https://mbasic.facebook.com/profile/basic/intro/bio/')
			br._factory.is_html = True
			br.select_form(nr=1)
			br.form['bio'] = self.bio
			sub = br.submit().read()
			if not 'Jelaskan siapa Anda' in str(sub):
				print(W +'[' + G + '*' + W + '] successfully changed to',str(self.bio.replace('\n',' ')))
			else:
				print(W +'[' + R + '*' + W + '] '+R+'failed')
		except (mechanize.URLError):
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
		
	def Main(self):
		print(W + "\n[" + R + "!" + W + "] type '</>' for change lines. max 101 Character")
		self.bio = input(W + '[' + G + '?' + W + '] your bio : '+G)
		self.bio = self.bio.replace('</>','\n')
		self.Change()

Bio()