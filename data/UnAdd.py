#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import sys, requests, time
from data import cekKuki
from bs4 import BeautifulSoup as parser
from multiprocessing.pool import ThreadPool
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

class Cancel:
	def __init__(self):
		cekKuki.cek(self)
		self.id = []
		self.suc = 0
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.url = 'https://mbasic.facebook.com{}'
		self.req = requests.Session()
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.Main(self.url.format('/friends/center/requests/outgoing/'))
	
	def Execute(self,id):
		try:
			can = self.req.get(id,headers = self.HD)
			if can.status_code == 200:
				self.suc +=1
			print(W + '\r[' + G + '*' + W + '] '+str(self.suc)+ ' requests canceled. ',end='');sys.stdout.flush()
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
	
	def Main(self,link):
		try:
			r = self.req.get(link,headers = self.HD)
			bs = parser(r.content, 'html.parser')
			if 'Batalkan Permintaan' in str(bs):
				for i in bs.find_all('a',string = 'Batalkan Permintaan'):
					self.id.append(self.url.format(i['href']))
			if 'Lihat selengkapnya' in str(bs):
				href = bs.find('a', string = 'Lihat selengkapnya')
				self.Main(self.url.format(href['href']))
			if len(self.id) == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'no requests sent found!')
				sys.exit()
			print(W + '[' + G + '*' + W + '] ' + str(len(self.id)) + ' requests sent found.')
			time.sleep(2)
			ThreadPool(10).map(self.Execute,self.id)
			print(W + '\n[' + G + '•' + W + '] done!')
			sys.exit()
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
try:
	print(W + '\n[' + G + '*' + W + '] Get user id... ')
	Cancel()
	print(W + '\n[' + G + '•' + W + '] done!')
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()