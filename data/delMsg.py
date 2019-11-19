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
	
class Mess:
	def __init__(self):
		self.url = 'https://mbasic.facebook.com{}'
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.req = requests.Session()
		cekKuki.cek(self)
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.link = []
		self.Main(self.url.format('/messages/'))
	
	def Excute(self,link):
		data = []
		
		try:
			r = self.req.get(link,headers = self.HD)
			bs = parser(r.content, 'html.parser')
			name = bs.title.text
			
			for x in bs('form'):
				if 'action_redirect' in x['action']:
					data.append(x['action'])
					break
			
			for x in bs('input'):
				try:
					
					if 'fb_dtsg' in x['name']:
						data.append(x['value'])
					if 'jazoest' in x['name']:
						data.append(x['value'])
					if 'delete' in x['name']:
						data.append(x['value'])
						break
				
				except: pass
			
			url = self.url.format(data[0])
			form = {'fb_dtsg' : data[1], 'jazoest' : data[2], 'delete' : data[3]}
			a = self.req.post(url, data = form, headers = self.HD)
			c = parser(a.content, 'html.parser').find('a', string = 'Hapus')
			href = self.url.format(c['href'])
			p = self.req.get(href,headers = self.HD)
			if p.status_code == 200:
				print(W + '[' + G + '-' + W + '] ' + G + name + R + ' >> ' + W + 'success delete messages')
			else:
				print(W + '[' + R + '×' + W + '] ' + G + namen + R + ' >> ' + W + ' failed')
				
		except IndexError: pass
		
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
		
	def Threads(self):
		try:
			threads = int(input(W + '\n[' + G + '?' + W + '] threads 1-50 : ' + G))
			if threads >50:
				print(W + '[' + R + '!' + W + '] ' + R + 'exceeds the limit!')
				self.Threads()
		except ValueError:
			print(W + '[' + R + '!' + W + '] ' + R + 'enter the numbers!')
			self.Threads()
			
		print()
		m = ThreadPool(threads)
		m.map(self.Excute,self.link)
		exit(W + '\n[' + G + '•' + W + '] done!')
		
	def Main(self,url):
		try:
			r = self.req.get(url, headers = self.HD)
			bs = parser(r.content, 'html.parser')
			for soup in bs.find_all('div'):
				p = soup.find('a')
				
				if '/messages/read/?' in str(p):
					self.link.append(self.url.format(p['href']))
					print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.link)) + W + '] GET messages url... ',end = '');sys.stdout.flush()
					
			if 'Lihat Pesan Sebelumnya' in str(bs):
				href = bs.find('a', string = 'Lihat Pesan Sebelumnya')
				self.Main(self.url.format(href['href']))
			else:
				if len(self.link) == 0:
					exit(W + '[' + R + '!' + W + '] ' + R + 'no messages found!')
					
				self.Threads()
				
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
print()
try:
	Mess()
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()