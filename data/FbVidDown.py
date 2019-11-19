#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, requests, time
from data import cekKuki
from bs4 import BeautifulSoup as parser
from http.cookiejar import LWPCookieJar as kuki
from clint.textui import progress

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

class FbVid:
	def __init__(self):
		cekKuki.cek(self)
		self.count = 0
		self.time = time.strftime('%Y-%H-%M-%S')
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.req = requests.Session()
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.Main()
	
	def Continue(self,url):
		try:
			download = self.req.get('https://mbasic.facebook.com'+url,headers = self.HD)
			if download.status_code == 200:
				self.count +=1
				with open('result/video/'+str(self.time)+'_'+str(self.count)+'.mp4','wb') as save:
					video = int(download.headers.get('content-length'))
					for chunk in progress.bar(download.iter_content(chunk_size=1024), expected_size=(video/1024) + 1):
						if chunk:
							save.write(chunk)
							save.flush()
			print(W + '[' + G + '•' + W + '] done!')
			print(W + '[' + G + '#' + W + '] video saved : '+ G + 'result/video/'+str(self.time)+'_'+str(self.count)+'.mp4')
			exit()
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
			
	def Get(self,link):
		try:
			a = self.req.get(link,headers = self.HD)
			b = parser(a.content, 'html.parser')
			for i in b.find_all('a'):
				if '/video_redirect/?' in str(i):
					print(W + '[' + G + '*' + W + '] please wait... ')
					self.Continue(i['href'])
					break
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
	
	def Main(self):
		url = input(W + '\n[' + G + '?' + W + '] enter post video url : '+G)
		url = url.replace('https://web.facebook.com','https://mbasic.facebook.com')
		url = url.replace('https://m.facebook.com','https://mbasic.facebook.com')
		self.Get(url)
try:
	FbVid()
except Exception as E:
	print(W + '[' + R + '!' + W + '] ' + R + str(E))
	sys.exit()