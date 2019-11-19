#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, requests, json
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

class Groups:
	def __init__(self):
		cekKuki.cek(self)
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.token = open('log/token').read()
		self.req = requests.Session()
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.id = []
		self.count = 0
		self.Main()
	
	def Excute(self,id):
		try:
			
			data = []
			r = self.req.get('https://mbasic.facebook.com/group/leave/?group_id=' + str(id),headers = self.HD)
			bs = parser(r.content, 'html.parser')
			
			for x in bs('form'):
				if '/a/group/leave/?' in x['action']:
					data.append(x['action'])
					
			for x in bs('input'):
				try:
					if 'fb_dtsg' in x['name']:
						data.append(x['value'])
					if 'jazoest' in x['name']:
						data.append(x['value'])
						break
				except: pass
			
			if len(data) == 3:
				url = 'https://mbasic.facebook.com' + data[0]
				form = {'fb_dtsg' : data[1], 'jazoest' : data[2], 'group_id' : id, 'confirm' : 'Keluar dari Grup'}
				le = self.req.post(url, data = form, headers = self.HD)
				bs1 = parser(le.content, 'html.parser')
				if 'Gabung ke Grup' in str(bs1):
					print(W + '[' + G + '-' + W + '] ' + G + str(bs1.title.text) + W + ' - success leave the groups')
				else:
					print(W + '[' + R + '×' + W + '] ' + G + str(bs1.title.text) + W + ' - failed leave the groups')
			else:
				print(W + '[' + R + '×' + W + '] ' + G + str(id) + W + ' - failed leave the groups')
		
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
			
	def Grps(self):
		try:
			if self.e == 1:
				print()
				
				r = requests.get('https://graph.facebook.com/me/groups?access_token=' + self.token,headers = self.HD)
				a = json.loads(r.text)
				
				for i in a['data']:
					self.id.append(i['id'])
					self.count +=1
					print(G + str(self.count) + W + '. ' + str(i['name']))
				
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'no groups found!')
					sys.exit()
				else:
					cek = int(input(W + '\n[ ' + R + 'Select Numbers' + W +' ]•> ' + G))
					print()
					self.Excute(self.id[cek-1])
					exit(W + '\n[' + G + '•' + W + '] done!')
			
			if self.e == 2:
				print()
				
				r = requests.get('https://graph.facebook.com/me/groups?access_token=' + self.token,headers = self.HD)
				a = json.loads(r.text)
				
				for i in a['data']:
					self.id.append(i['id'])
					self.Excute(i['id'])
				
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'no groups found!')
					sys.exit()
				else:
					exit(W + '\n[' + G + '•' + W + '] done!')
					
		except KeyError:
			print(W + '[' + R + '!' + W + '] ' + R + 'error when grabbing groups id!')
			sys.exit()
		
		except requests.exceptions.ConnectionError:
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
					
	def Main(self):
		
		print(W + '\n  {' + G + '01' + W + '} Leave One Groups')
		print(W + '  {' + G + '02' + W + '} Leave All groups')
		print(W + '  {' + R + '00' + W + '} Back')
		
		cek = input(W + '\n[ ' + R + 'Dz' + W +' ]•> ' + G)
		
		if cek in ['1','01']:
			self.e = 1
			self.Grps()
		elif cek in ['2','02']:
			self.e = 2
			self.Grps()
		elif cek in ['0','00']:
			os.system('python Fb.py')
		else:
			print(W + '[' + R + '!' + W + '] ' + R + 'you stuppid!')
			sys.exit()
try:
	Groups()
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()