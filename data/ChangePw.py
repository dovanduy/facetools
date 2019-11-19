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

class Pw:
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
			br.open('https://mbasic.facebook.com/settings/security/password/')
			br._factory.is_html = True
			br.select_form(nr=1)
			br.form['password_old'] = self.pw
			br.form['password_new'] = self.new
			br.form['password_confirm'] = self.new
			sub = br.submit().read()
			if 'Kata Sandi Telah Diubah' in str(sub) or 'Password Changed' in str(sub):
				print(W +'[' + G + '*' + W + '] successfully changed to',str(self.new))
			else:
				print(W +'[' + R + '*' + W + '] '+R+'failed')
		except (mechanize.URLError):
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
		
	def Main(self):
			self.pw = input(W + '\n[' + G + '?' + W + '] your password : '+G)
			self.new = input(W + '[' + G + '?' + W + '] new password : '+G)
			y = input(W + '[' + G + '?' + W + '] are you sure? [y/n] : '+G)
			if y.lower() == 'y':
				self.Change()
			else: print(W + '[' + R + '*' + W + '] canceling')
			sys.exit()
			
Pw()