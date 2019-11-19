#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, requests
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
try:
	os.mkdir('result')
except: pass
try:
	os.mkdir('result/video')
except: pass

class Join:
	def __init__(self):
		cekKuki.cek(self)
		self.suc = 0
		self.fail = 0
		self.count = 0
		self.link = []
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.req = requests.Session()
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.Main()
	
	def Continue(self,url):
		try:
			a = self.req.get(url, headers = self.HD)
			b = parser(a.content, 'html.parser')
			if 'Anda Diblokir untuk Sementara Waktu' in str(b):
				self.fail +=1
			else: self.suc +=1
			self.count +=1
			print(W + '\r[' + G + '*' + W + '] process {:.2f}% '.format(self.count/len(self.link)*100) + 'success :-'+ G + str(self.suc) + W + ' fail :-'+ R + str(self.fail) + W + ' ',end='');sys.stdout.flush()
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
			
	def Get(self,link):
		try:
			a = self.req.get(link,headers = self.HD)
			b = parser(a.content, 'html.parser')
			for i in b.find_all('a'):
				if '/a/group/join/?' in str(i):
					self.link.append('https://mbasic.facebook.com'+i['href'])
				p = i.find('div')
				if 'None' in str(p) or '+' in str(p):
					continue
				else:
					print(G + '\r  - ' + W +str(p.text)+ '             ')
			print(W + '\r[' + G + '*' + W + '] GET group url... ',end='');sys.stdout.flush()
			if 'Lihat Hasil Selanjutnya' in str(b):
				href = b.find('a', string = 'Lihat Hasil Selanjutnya')
				self.Get(href['href'])
			if len(self.link) == 0:
				print(W + '\n[' + R + '!' + W + '] ' + R + 'no results found!')
				sys.exit()
			else:
				#///
				print(W + '\n[' + G + '*' + W + '] ' + str(len(self.link)) + ' groups successfully retrieved.')
				for link in self.link:
					self.Continue(link)
				print(W + '\n[' + G + '•' + W + '] done!')
				sys.exit()
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
	
	def Main(self):
		name = input(W + '\n[' + G + '?' + W + '] search with name : '+G)
		url = 'https://mbasic.facebook.com/search/groups/?q='+name
		self.Get(url)
#///
Join()