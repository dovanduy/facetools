#!usr/bin/python3.7
#Author: DulLah ©2019
# FB : fb.me/dulahz
#Telegram : t.me/unikers
#github: github.com/dz-id

import sys, requests, json, re
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
	
class Invite:
	def __init__(self):
		cekKuki.cek(self)
		self.req = requests.Session()
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.token = open('log/token').read()
		self.Main()
	
	def Excute(self,user):
		try:
			a = self.req.get('https://mbasic.facebook.com'+user,headers = self.HD)
			id = re.findall(r'/?invitee=(.*?)&page_id=',user)
			r = requests.get('https://graph.facebook.com/'+id[0]+'?access_token='+self.token,headers = self.HD)
			name = r.json()['name']
			if a.status_code == 200:
				print(W + '[' + G + '*' + W + '] ' + str(name) + ' (' + str(id[0]) + ') - invited')
			else:
				print(W + '[' + R + '×' + W + '] ' + str(name) + ' (' + str(id[0]) + ') - failed')
				
		except KeyboardInterrupt:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
			
	def Get(self,url):
		try:
			r = self.req.get('https://mbasic.facebook.com'+str(url),headers = self.HD)
			b = parser(r.content, 'html.parser')
			if 'Undang' in str(b):
				for i in b.find_all('a', string = 'Undang'):
					self.Excute(i['href'])
					
				if 'Lihat Selengkapnya' in str(b):
					href = b.find('a', string = 'Lihat Selengkapnya')
					self.Get(href['href'])
				else:
					print(W + '\n[' + G + '•' + W + '] done!')
					exit()
					
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
			
	def Main(self):
		try:
			data = []
			page = input(W + '\n[' + G + '?' + W + '] enter your page id : '+ G)
			
			a = self.req.get('https://mbasic.facebook.com/'+str(page), headers = self.HD)
			b = parser(a.content, 'html.parser')
			for i in b.find_all('a'):
				if '/invite_friends/?' in str(i):
					data.append(i['href'])
					break
			
			if len(data) == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'page not found!')
				sys.exit()
			#//
			print(W + '[' + R + '!' + W + '] CTRL+c for stop\n')
			self.Get(data[0])
		except requests.exceptions.ConnectionError:
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
#//
Invite()