#!usr/bin/python3.7
#Author: DulLah ©2019
# FB : fb.me/dulahz
#Telegram : t.me/unikers
#github: github.com/dz-id

import sys, requests, json
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
	
class Invite:
	def __init__(self):
		self.loop = 0
		cekKuki.cek(self)
		self.id = []
		self.req = requests.Session()
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.token = open('log/token').read()
		self.Main()
	
	def Excute(self,user):
		try:
			data = []
			a = self.req.get('https://mbasic.facebook.com/groups/members/search/?group_id='+str(self.group),headers = self.HD)
			b1 = parser(a.content, 'html.parser')
			
			for i in b1('form'):
				if '/groups/members/search/?' in i['action']:
					data.append(i['action'])
					break
			for i in b1('input'):
				try:
					if 'fb_dtsg' in i['name']:
						data.append(i['value'])
					if 'jazoest' in i['name']:
						data.append(i['value'])
					if 'group_name' in i['name']:
						data.append(i['value'])
					if 'group_id' in i['name']:
						data.append(i['value'])
						break
				except: pass
			
			if len(data) == 5:
				p = requests.get('https://graph.facebook.com/'+str(user)+'?access_token='+str(self.token),headers = self.HD)
				name = p.json()['name']
				url = 'https://mbasic.facebook.com'+data[0]
				form = {'fb_dtsg' : data[1], 'jazoest' : data[2], 'group_name' : data[3], 'group_id' : data[4], 'addees['+str(user)+']' : str(user), 'add' : 'Undang yang Dipilih'}
				s = self.req.post(url, data = form, headers = self.HD)
				if 'ditambahkan ke grup ini.' in str(s.text):
					print(W + '[' + G + '*' + W + '] ' + str(name) + ' (' + str(user)+ ') - invited')
				elif 'Orang ini tidak ditambahkan ke grup.' in str(s.text):
					print(W + '[' + R + '*' + W + '] ' + str(name) + ' (' + str(user)+ ') - already been invited')
				else:
					print(W + '[' + R + '*' + W + '] ' + str(name) + ' (' + str(user)+ ') - failed')
					
		except KeyError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'error:)*!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
		
	def Add(self):
		print('')
		for id in self.id:
			self.Excute(id)
			self.loop +=1
			
			if self.loop == self.count:
				print(W + '\n[' + G + '•' + W + '] done!')
				sys.exit()
	
	def Main(self):
		try:
			a = requests.get('https://graph.facebook.com/me/friends?access_token='+str(self.token),headers = self.HD)
			r = json.loads(a.text)
			
			for i in r['data']:
				self.id.append(i['id'])
			
			if len(self.id) !=0:
				print(W + '\n[' + G + '*' + W + '] total friends (' + G + str(len(self.id)) + W + ')')
				self.count = int(input(W + '[' + G + '?' + W + '] how many friends u wanna invite : '+ G))
				
				if self.count > len(self.id):
					print(W + '[' + R + '!' + W + '] ' + R + 'stuppid!')
					sys.exit()
			else:
				print(W + '[' + R + '!' + W + '] ' + R + 'no friends found!')
				sys.exit()
			
			self.group = input(W + '[' + G + '?' + W + '] enter group id : '+ G)
			#//
			self.Add()
		except ValueError:
			print(W + '[' + R + '!' + W + '] ' + R + 'enter the numbers!')
			sys.exit()
		except KeyError:
			print(W + '[' + R + '!' + W + '] ' + R + 'error when grabbing friends id!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
		except requests.exceptions.ConnectionError:
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()

try:
	Invite()
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()