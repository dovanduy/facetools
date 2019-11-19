#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import sys, requests
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
	
class Hide:
	def __init__(self):
		self.loop = 0
		cekKuki.cek(self)
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.url = 'https://mbasic.facebook.com{}'
		self.req = requests.Session()
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.link = []
		self.success = []
		self.Main(self.url.format('/me'))
	
	def Excute(self,url):
		try:
			data = []
			a = self.req.get(url,headers = self.HD)
			b = parser(a.content, 'html.parser')
			
			for i in b('form'):
				if '/nfx/basic/handle_action/?' in i['action']:
					data.append(i['action'])
					break
			
			for i in b('input'):
				try:
					if 'fb_dtsg' in i['name']:
						data.append(i['value'])
					if 'jazoest' in i['name']:
						data.append(i['value'])
					if 'HIDE_FROM_TIMELINE' in i['value']:
						data.append(i['value'])
						break
				except: pass
			
			if len(data) == 4:
				anu = self.url.format(data[0])
				form = {'fb_dtsg' : data[1], 'jazoest' : data[2], 'action_key' : data[3]}
				u = self.req.post(anu, data = form, headers = self.HD)
				if u.status_code == 200:
					self.success.append(url)
					
			self.loop +=1
			print(W + '\r[' + G + '-' + W + '] process hide posts ' + str(self.loop) + '/' + str(len(self.link)) + ' > ' + str(len(self.success)),end = '  ');sys.stdout.flush()
					
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
	
	def Threads(self):
		try:
			threads = int(input(W + '\n[' + G + '?' + W + '] threads 1-30 : ' + G))
			if threads >30:
				print(W + '[' + R + '!' + W + '] ' + R + 'exceeds the limit!')
				self.Threads()
		except ValueError:
			print(W + '[' + R + '!' + W + '] ' + R + 'enter the numbers!')
			self.Threads()
			
		print()
		m = ThreadPool(threads)
		m.map(self.Excute,self.link)
		exit(W + '[' + G + '•' + W + '] done!')
			
	def Main(self,url):
		try:
			r = self.req.get(url, headers = self.HD)
			a = parser(r.content, 'html.parser')
			if 'Lainnya' in str(a):
				for i in a.find_all('a', string = 'Lainnya'):
					self.link.append(self.url.format(i['href']))
					print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.link)) + W + '] GET posts url... ',end='');sys.stdout.flush()
				
				if 'Lihat Berita Lain' in str(a):
					href = self.url.format(a.find('a', string = 'Lihat Berita Lain')['href'])
					self.Main(href)
					
			if len(self.link) == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'no posts found!')
				sys.exit()
			else:
				self.Threads()
				
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
try:
	print()
	Hide()
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()