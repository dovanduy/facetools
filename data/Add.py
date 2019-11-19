#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, re, sys, requests, json
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
	
class Add:
	def __init__(self):
		cekKuki.cek(self)
		self.id = []
		self.req = requests.Session()
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.token = open('log/token').read()
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.url = 'https://mbasic.facebook.com{}'
		self.Main()
	
	def Excute(self,user):
		url = 'https://graph.facebook.com/me/friends?method=post&uids={}&access_token={}'.format(str(user),str(self.token))
		try:
			rr = requests.post(url, headers = self.HD)
			if rr.json() == True:
				print(W + '[' + G + '+' + W + ']',str(user), '- requests sent')
			else:
				print(W + '[' + R + '×' + W + ']',str(user), '- failed')
		
		except requests.exceptions.ConnectionError:
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
			
	def Get(self,tip,links):
		try:
			if tip == 'friends':
				
				friends = input(W + '\n[' + G + '?' + W +'] enter friends id : ' + G)
				limit = int(input(W + '[' + G + '?' + W +'] how many : ' + G))
				
				a = requests.get('https://graph.facebook.com/'+str(friends)+'/friends?access_token='+str(self.token),headers = self.HD)
				z = json.loads(a.text)
				
				print('')
				for i in z['data']:
					
					self.Excute(i['id'])
					self.id.append(i['id'])
					
					if len(self.id) == limit:
						print(W + '\n[' + G + '•' + W + '] done!')
						sys.exit()
						
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'no user found!')
				else:
					print(W + '\n[' + G + '•' + W + '] done!')
					sys.exit()
			
			elif tip == 'groups':
				
				groups = input(W + '\n[' + G + '?' + W +'] enter groups id : ' + G)
				limit = int(input(W + '[' + G + '?' + W +'] how many : ' + G))
				
				a = requests.get('https://graph.facebook.com/'+str(groups)+'/members?fields=id&limit=5000&access_token='+str(self.token))
				z = json.loads(a.text)
				
				print('')
				for i in z['data']:
					
					self.Excute(i['id'])
					self.id.append(i['id'])
					
					if len(self.id) == limit:
						print(W + '\n[' + G + '•' + W + '] done!')
						sys.exit()
						
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'no user found!')
				else:
					print(W + '\n[' + G + '•' + W + '] done!')
					sys.exit()
			
			elif tip == 'people':
				
				a = self.req.get(self.url.format(links),headers = self.HD)
				z = parser(a.content, 'html.parser')
				
				if 'Tambah Jadi Teman' in str(z):
					for i in z.find_all('a', string = 'Tambah Jadi Teman'):
						ids = re.findall(r'/?id=(.*)&hf=',i['href'])
						
						self.Excute(ids[0])
						self.id.append(ids[0])
						
						if len(self.id) == self.limit:
							print(W + '\n[' + G + '•' + W + '] done!')
							sys.exit()
							
					if 'Lihat selengkapnya' in str(z):
						href = z.find('a', string = 'Lihat selengkapnya')
						self.Get(tip,href['href'])
				
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'no user found!')
				else:
					print(W + '\n[' + G + '•' + W + '] done!')
					sys.exit()
			
			elif tip == 'files':
				
				file = input(W + '\n[' + G + '?' + W +'] lists id : ' + G)
				limit = int(input(W + '[' + G + '?' + W +'] how many : ' + G))
				
				print('')
				for ids in open(file).readlines():
					self.Excute(ids.strip())
					self.id.append(ids.strip())
					
					if len(self.id) == limit:
						print(W + '\n[' + G + '•' + W + '] done!')
						sys.exit()
				
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'no user found!')
				else:
					print(W + '\n[' + G + '•' + W + '] done!')
					sys.exit()
		
		except IOError:
			print(W + '[' + R + '!' + W + '] ' + R + 'files not found!')
			sys.exit()
		except KeyError:
			print(W + '[' + R + '!' + W + '] ' + R + 'error when grabbing user id!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
		except ValueError:
			print(W + '[' + R + '!' + W + '] ' + R + 'enter the numbers!')
			self.Get(tip)
		except requests.exceptions.ConnectionError:
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
	
	def Main(self):
		
		print(W + '\n  {' + G + '01' + W + '} Add Friends From Friends')
		print(W + '  {' + G + '02' + W + '} Add Friends From Groups')
		print(W + '  {' + G + '03' + W + '} Add Friends From People You May Know')
		print(W + '  {' + G + '04' + W + '} Add Friends By Lists Id')
		print(W + '  {' + R + '00' + W + '} Back')
		
		cek = input(W + '\n[ ' + R + 'Dz' + W +' ]•> ' + G)
		if cek in ['1','01']:
			self.Get('friends',' ')
		elif cek in ['2','02']:
			self.Get('groups',' ')
		elif cek in ['3','03']:
			self.limit = int(input(W + '\n[' + G + '?' + W +'] how many : ' + G))
			print('')
			self.Get('people','/friends/center/mbasic/')
		elif cek in ['4','04']:
			self.Get('files',' ')
		elif cek in ['0','00']:
			os.system('python Fb.py')
		else:
			print(W + '[' + R + '!' + W + '] ' + R + 'you stuppid!')
try:
	Add()
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()
except Exception as E:
	print(W + '[' + R + '!' + W + '] ' + R + E)