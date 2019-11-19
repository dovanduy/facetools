#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, re, requests
from data import cekKuki
from bs4 import BeautifulSoup as parser
from http.cookiejar import LWPCookieJar as kuki
from multiprocessing.pool import ThreadPool

global W, G, R
if sys.platform in ['linux','linux2']:
	W = '\033[0m'
	G = '\033[1;92m'
	R = '\033[1;91m'
else:
	W = ''
	G = ''
	R = ''

class Friends:
	def __init__(self):
		cekKuki.cek(self)
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.url = 'https://mbasic.facebook.com{}'
		self.req = requests.Session()
		s = self.req
		self.link = []
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.Main()
		
	def Excute(self,arg):
		try:
			if self.e == '1':
				
				a = self.req.get(arg, headers = self.HD)
				ids = re.findall(r'/?confirm=(.*?)&seenrequesttime=',arg)
				if a.status_code == 200:
					try:
						print(W + '[' + G + '-' + W + '] ' + G + str(ids[0]) + R + ' >> ' + W + 'accepted')
					except KeyError: print(W + '[' + G + '-' + W + '] ' + G + 'not known' + R + ' >> ' + W + 'accepted')
				else:
					try:
						print(W + '[' + R + '×' + W + '] ' + G + str(ids[0]) + R + ' >> ' + W + 'failed')
					except KeyError: print(W + '[' + R + '×' + W + '] ' + G + 'not known' + R + ' >> ' + W + 'failed')
					
			elif self.e == '2':
				
				a = self.req.get(arg, headers = self.HD)
				ids = re.findall(r'/?delete=(.*?)&seenrequesttime=',arg)
				if a.status_code == 200:
					try:
						print(W + '[' + G + '-' + W + '] ' + G + str(ids[0]) + R + ' >> ' + W + 'rejected')
					except KeyError: print(W + '[' + G + '-' + W + '] ' + G + 'not known' + R + ' >> ' + W + 'rejected')
				else:
					try:
						print(W + '[' + R + '×' + W + '] ' + G + str(ids[0]) + R + ' >> ' + W + 'failed')
					except KeyError: print(W + '[' + R + '×' + W + '] ' + G + 'not known' + R + ' >> ' + W + 'failed')
					
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
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
		exit(W + '\n[' + G + '•' + W + '] done!')
			
	def Frn(self,url):
		try:
			if self.e == '1':
				
				r = self.req.get(url, headers = self.HD)
				bs = parser(r.content, 'html.parser')
				
				if 'Konfirmasi' in str(bs):
					for a in bs.find_all('a', string = 'Konfirmasi'):
						if '/a/notifications.php?' in str(a):
							self.link.append(self.url.format(a.get('href')))
							print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.link)) + W + '] GET user id... ',end='');sys.stdout.flush()
							
				if 'Lihat selengkapnya' in str(bs):
					href = bs.find('a', string = 'Lihat selengkapnya').get('href')
					self.Frn(url.format(href))
					
				if len(self.link) == 0:
					print(W + '[' + R + '!' + W + '] no friends requests found!')
					sys.exit()
				else:
					self.Threads()
			
			elif self.e == '2':
				
				r = self.req.get(url, headers = self.HD)
				bs = parser(r.content, 'html.parser')
				
				if 'Hapus Permintaan' in str(bs):
					for a in bs.find_all('a', string = 'Hapus Permintaan'):
						if '/a/notifications.php?' in str(a):
							self.link.append(self.url.format(a.get('href')))
							print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.link)) + W + '] GET user id... ',end='');sys.stdout.flush()
				
				if 'Lihat selengkapnya' in str(bs):
					href = bs.find('a', string = 'Lihat selengkapnya').get('href')
					self.Frn(url.format(href))
					
				if len(self.link) == 0:
					print(W + '[' + R + '!' + W + '] no friends requests found!')
					sys.exit()
				else:
					self.Threads()
				
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
				
	def Main(self):
		print(W + '\n  {' + G + '01' + W + '} Accept All Friends Requests')
		print(W + '  {' + G + '02' + W + '} Reject All Friends Requests')
		print(W + '  {' + R + '00' + W + '} Back')
		
		cek = input(W + '\n[ ' + R + 'Dz' + W +' ]•> ' + G)
		if cek in ['1','01']:
			self.e = '1'
			print()
			self.Frn(self.url.format('/friends/center/requests/'))
		elif cek in ['2','02']:
			self.e = '2'
			print()
			self.Frn(self.url.format('/friends/center/requests/'))
		elif cek in ['0','00']:
			os.system('python Fb.py')
		else:
			print(W + '[' + R + '!' + W + '] ' + R + 'you stuppid!')
			sys.exit()
try:
	Friends()
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()