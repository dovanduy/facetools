#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, requests, re
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
try:
	os.mkdir('result')
except: pass

class Join:
	def __init__(self):
		self.data = []
		self.count = 0
		cekKuki.cek(self)
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.req = requests.Session()
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.Main()
	
	def Continue(self,id):
		try:
			self.data.append(str(id))
			if len(self.data) == 2:
				self.data = [] #//
			elif len(self.data) == 1:
				a = self.req.get('https://mbasic.facebook.com/'+str(id),headers = self.HD)
				b = parser(a.content, 'html.parser')
				if 'Grup Publik' in str(b):
					print(W + '[' + G + '*' + W + '] ID     : ' + G + str(id))
					print(W + '[' + G + '*' + W + '] Name   : ' + G + str(b.title.text))
					print(W + '[' + G + '*' + W + '] Groups : ' + G + 'public')
					print(W + '-'*45)
					self.sv.write(str(id)+'\n')
				elif 'Grup Privat' in str(b):
					print(W + '[' + R + '*' + W + '] ID     : ' + R + str(id))
					print(W + '[' + R + '*' + W + '] Name   : ' + R + str(b.title.text))
					print(W + '[' + R + '*' + W + '] Groups : ' + R + 'privat')
					print(W + '-'*45)
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
			
	def Get(self,link):
		try:
			a = self.req.get(link,headers = self.HD)
			b = parser(a.content, 'html.parser')
			for i in b.find_all('a'):
				if '/groups/' in str(i):
					try:
						idg = re.findall(r'/groups/(.*?)?refid=',i['href'])[0].replace('?','')
						self.Continue(int(idg))
						self.count +=1
					except ValueError:
							pass
			if 'Lihat Hasil Selanjutnya' in str(b):
				href = b.find('a', string = 'Lihat Hasil Selanjutnya')
				self.Get(href['href'])
			if self.count == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'no result found!')
				sys.exit()
			else:
				print(W + '\n[' + G + '•' + W + '] done!')
				print(W + '[' + G + '#' + W + '] out : ' + G + 'result/GroupPublik.txt')
				self.sv.close()
				sys.exit()
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
	
	def Cek(self):
		print('')
		if os.path.exists('result/GroupPublik.txt'):
			if os.path.getsize('result/GroupPublik.txt') !=0:
				print(W + '[' + R + '!' + W + '] GroupPublik.txt exists!')
				y = input(W + '[' + G + '?' + W + '] remove? [y/n] : '+ G)
				if y.lower() == 'y':
					os.remove('result/GroupPublik.txt')
					print(W + '[' + G + '*' + W + '] success removed')
				else:
					print(W + '[' + R + '*' + W + '] ' + R + 'canceling')
					sys.exit()
			else: pass
		else: pass
		
	def Main(self):
		self.Cek()
		name = input(W + '[' + G + '?' + W + '] search with name : '+G)
		url = 'https://mbasic.facebook.com/search/groups/?q='+name
		self.sv = open('result/GroupPublik.txt','w')
		print(W + '-'*45)
		self.Get(url)
#///
Join()