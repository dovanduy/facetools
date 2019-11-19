#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, requests, mechanize
from bs4 import BeautifulSoup as parser

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

class Checkpoint:
	def __init__(self):
		self.Main()
	
	def Continue(self):
		try:
			self.br.open('https://mbasic.facebook.com/login/checkpoint/?ref=dbl')
			self.br._factory.is_html = True
			self.br.select_form(nr=0)
			cek = self.br.submit().read()
			tipe = parser(cek, 'html.parser')
			for i in tipe.find_all('option'):
				print(Y + '  - ' + i.text)
			print(W + '-'*45)
		except: pass
			
	def Login(self,user):
		try:
			print(W + '[' + G + '*' + W + '] trying login ->',user)
			self.br = mechanize.Browser()
			self.br.set_handle_equiv(True)
			self.br.set_handle_gzip(True)
			self.br.set_handle_redirect(True)
			self.br.set_handle_referer(True)
			self.br.set_handle_robots(False)
			self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
			self.br.addheaders = [('User-Agent', open('UserAgent/ua.txt').read())]
			self.br.open('https://mbasic.facebook.com')
			self.br._factory.is_html = True
			self.br.select_form(nr=0)
			self.br.form['email'] = user.split('|')[0]
			self.br.form['pass'] = user.split('|')[1]
			sub = self.br.submit().read()
			if 'checkpoint' in str(sub):
				self.Continue()
			elif 'save-device' in str(sub) or 'logout.php' in str(sub):
				print(G + '  - no cekpoint detected')
				print(W + '-'*45)
			else:
				print(R + '  - failed login')
				print(W + '-'*45)
		except KeyboardInterrupt:
			print(W + '[' + R + '!' + W + '] ' + R + 'key interupt!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
		except requests.exceptions.ConnectionError:
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
		
	def Main(self):
		try:
			print(W + '\n[' + R + '!' + W + '] sparator email|password')
			list = input(W + '[' + G + '?' + W + '] account lists : '+G)
			print(W + '-'*45)
			for id in open(list).readlines():
				self.Login(id.strip())
			print(W + '[' + G + '•' + W + '] done!')
		except FileNotFoundError:
			print(W + '[' + R + '!' + W + '] ' + R + 'file not found!')
			sys.exit()

Checkpoint()