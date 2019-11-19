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

class App:
	def __init__(self):
		self.Main()
	
	def Continue(self):
		try:
			app = []
			buka = self.br.open('https://mbasic.facebook.com/settings/apps/tabbed/')
			bs = parser(buka.read(), 'html.parser')
			for i in bs.find_all('h3'):
				p = i.find('div')
				if 'None' in str(p):
					continue
				else:
					app.append(p.text)
					print(W + '[' + G + '*' + W + '] app : '+ G + p.text)
			if len(app) == 0:
				print(W + '[' + R + '*' + W + '] no app found.')
			else:
				print(W + '[' + G + '*' + W + '] ' + str(len(app)) + ' app found.')
			print(W + '-'*45)
		except:
				pass
			
	def Login(self,user):
		try:
			print(W + '[' + G + '*' + W + '] check on account ->',user)
			self.br = mechanize.Browser()
			self.br.set_handle_equiv(True)
			self.br.set_handle_gzip(True)
			self.br.set_handle_redirect(True)
			self.br.set_handle_referer(True)
			self.br.set_handle_robots(False)
			self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
			self.br.addheaders = [('User-Agent', open('UserAgent/ua.txt').read())]
			self.br.open('https://mbasic.facebook.com/login.php')
			self.br._factory.is_html = True
			self.br.select_form(nr=0)
			self.br.form['email'] = user.split('|')[0]
			self.br.form['pass'] = user.split('|')[1]
			sub = self.br.submit().read()
			if 'save-device' in str(sub) or 'logout.php' in str(sub):
				self.Continue()
			elif 'checkpoint' in str(sub):
				print(Y + '  - account checkpoint')
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
			print(W + '\n  {' + G + '01' + W + '} Check App One Account')
			print(W + '  {' + G + '02' + W + '} Check App By Account Lists')
			print(W + '  {' + R + '00' + W + '} Back')
			cek = input(W + '\n[ ' + R + 'Dz' + W +' ]•> ' + G)
			if cek in ['1','01']:
				em = input(W + '\n[' + G + '?' + W + '] username : '+G)
				pw = input(W + '[' + G + '?' + W + '] password : '+G)
				print(W + '-'*45)
				user = em+'|'+pw
				self.Login(user)
				print(W + '[' + G + '•' + W + '] done!')
			elif cek in ['2','02']:
				print(W + '\n[' + R + '!' + W + '] sparator email|password')
				list = input(W + '[' + G + '?' + W + '] account lists : '+G)
				print(W + '-'*45)
				for id in open(list).readlines():
					self.Login(id.strip())
				print(W + '[' + G + '•' + W + '] done!')
			elif cek in ['0','00']:
				os.system('python Fb.py')
		except FileNotFoundError:
			print(W + '[' + R + '!' + W + '] ' + R + 'file not found!')
			sys.exit()

App()