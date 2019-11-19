#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import sys, re, requests
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
	
class DelPhoto:
	def __init__(self):
		self.url = 'https://mbasic.facebook.com{}'
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.req = requests.Session()
		cekKuki.cek(self)
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.link = []
		url = input(W + '\n[' + G + '?' + W + '] albums url : ' + G)
		url = url.replace('https://m.facebook.com','https://mbasic.facebook.com')
		self.Main(url)
	
	def Excute(self,link):
		data = []
		
		try:
			r = self.req.get(link,headers = self.HD)
			bs = parser(r.content, 'html.parser')
			a = bs.find('a', string = 'Edit Foto').get('href')
			s = self.req.get(self.url.format(a),headers = self.HD)
			bs2 = parser(s.content, 'html.parser')
			b = bs2.find('a' ,string = 'Hapus Foto').get('href')
			t = self.req.get(self.url.format(b),headers = self.HD)
			bs3 = parser(t.content, 'html.parser')
			
			for x in bs3('form'):
				if 'post' in x['method']:
					data.append(x['action'])
					break
			
			for x in bs3('input'):
				try:
					
					if 'fb_dtsg' in x['name']:
						data.append(x['value'])
					if 'jazoest' in x['name']:
						data.append(x['value'])
					if 'confirm_remove_profile_pic' in x['name']:
						data.append(x['value'])
					if 'remove_profile_pic' in x['name']:
						data.append(x['value'])
					if 'confirm_photo_delete' in x['name']:
						data.append(x['value'])
						break
				
				except: pass
				
			if len(data) == 5:
				url = self.url.format(data[0])
				form = {'fb_dtsg' : data[1], 'jazoest' : data[2], 'confirm_remove_profile_pic' : data[3], 'remove_profile_pic' : data[4]}
				f = self.req.post(url, data = form, headers = self.HD)
				id = re.findall(r"/?fbid=(.*?)&id=",link)[0]
				if  f.status_code == 200:
					print(W + '[' + G + '-' + W + '] ' + G + str(id) + R + ' >> ' + W + 'removed')
				else:
					print(W + '[' + R + '×' + W + '] ' + G + str(id) + R + ' >> ' + W + ' failed')
					
			elif len(data) == 4:
				url = self.url.format(data[0])
				form = {'fb_dtsg' : data[1], 'jazoest' : data[2], 'confirm_photo_delete' : data[3]}
				f = self.req.post(url, data = form, headers = self.HD)
				id = re.findall(r"/?fbid=(.*?)&id=",link)[0]
				if  f.status_code == 200:
					print(W + '[' + G + '-' + W + '] ' + G + str(id) + R + ' >> ' + W + 'removed')
				else:
					print(W + '[' + R + '×' + W + '] ' + G + str(id) + R + ' >> ' + W + ' failed')
		
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
		
		except IndexError: pass
		
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
		
	def Main(self,url):
		try:
			r = self.req.get(url, headers = self.HD)
			bs = parser(r.content, 'html.parser')
			for soup in bs.find_all('a'):
				
				if '/photo.php?' in str(soup):
					self.link.append(self.url.format(soup['href']))
					print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.link)) + W + '] GET photos url... ',end = '');sys.stdout.flush()
					
			if 'Lihat Foto Lainnya' in str(bs):
				href = bs.find('a', string = 'Lihat Foto Lainnya')
				self.Main(self.url.format(href['href']))
			else:
				if len(self.link) == 0:
					exit(W + '[' + R + '!' + W + '] ' + R + 'no photos found!')
					
				self.Threads()
				
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
try:
	DelPhoto()
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()