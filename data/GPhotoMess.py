#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, requests, time
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
	os.mkdir('result/photos')
except: pass

class PhotoGrabber:
	def __init__(self):
		cekKuki.cek(self)
		self.suc = 0
		self.count = 0
		self.token = open('log/token').read()
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.link = []
		self.req = requests.Session()
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.Main()
	
	def Excute(self,url):
		try:
			self.count +=1
			download = self.req.get(url,headers = self.HD)
			if download.status_code == 200:
				self.suc +=1
				self.time = time.strftime('%Y-%H-%M-%S')
				with open('result/photos/'+str(self.time)+'_'+str(self.suc)+'.jpg','wb') as save:
					save.write(download.content)
			sys.stdout.write(W + '\r[' + G + '*' + W + '] downloading photos {:.2f}% '.format(self.count/len(self.link)*100))
		except: pass
			
	def Get(self,link):
		try:
			a = self.req.get(link,headers = self.HD)
			b = parser(a.content, 'html.parser')
			for i in b.find_all('img'):
				if 'static.xx.fbcdn.net' in i['src']:
					continue
				else:
					self.link.append(i['src'])
			print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.link)) + W + '] GET photos url... ',end='');sys.stdout.flush()
			if 'Lihat Pesan Sebelumnya' in str(b):
				href = b.find('a', string = 'Lihat Pesan Sebelumnya')
				self.Get('https://mbasic.facebook.com'+href['href'])
			if len(self.link) == 0:
				print(W + '\n[' + R + '!' + W + '] ' + R + 'no photos found!')
			else:
				m = ThreadPool(5)
				m.map(self.Excute,self.link)
				print(W + '\n[' + G + '•' + W + '] done!')
				print(W + '[' + G + '#' + W + '] photos saved : ' + G + 'result/photos/*.jpg')
				sys.exit()
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
	
	def Main(self):
		try:
			id = input(W + '\n[' + G + '?' + W + '] account id : '+G)
			a = requests.get('https://graph.facebook.com/'+str(id)+'?access_token='+str(self.token),headers = self.HD).json()['id']
			self.Get('https://mbasic.facebook.com/messages/read/?tid='+str(a))
		except KeyError:
			print(W + '[' + R + '!' + W + '] ' + R + 'account not found!')
			sys.exit()
		except requests.exceptions.ConnectionError:
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
			
try:
	PhotoGrabber()
except Exception as E:
	print(W + '\n[' + R + '!' + W + '] ' + R + str(E))
	sys.exit()