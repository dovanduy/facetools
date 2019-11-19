#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, re, sys, time, requests, json
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
try:
	os.mkdir('result/dump')
except:pass
try:
	os.mkdir('result/dump/ID')
except: pass

class Dump:
	def __init__(self):
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.token = open('log/token').read()
		self.url = 'https://mbasic.facebook.com{}'
		self.req = requests.Session()
		self.count = []
		self.idj = []
		self.id = []
		self.Main()
			
	def Excute(self,id):
		try:
			jumping = []
			
			if self.t == 'F':
				
				print(W +'\n----------------------------------------')
				a = requests.get('https://graph.facebook.com/' + id + '?access_token=' + self.token, headers = self.HD)
				s = json.loads(a.text)
				
				name = s['name']
				
				print(W + '[' + G + '+' + W + '] dump id from : ' + G + name)
				
				r = requests.get('https://graph.facebook.com/' + id + '/friends?access_token=' + self.token, headers = self.HD)
				b = json.loads(r.text)
				
				for result in b['data']:
					self.idj.append(result['id'])
					jumping.append(result['id'])
					self.wrt.write(result['id']+'\n')
					print(W + '\r[' + G + '*' + W + '] [' + R + str(len(jumping)) + W + '] Writing Id... ',end='');sys.stdout.flush();time.sleep(0.0002)
				
				if len(jumping) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'lists friends privat!')
			
			elif self.t == 'G':
				try:
					
					r = requests.get(id, headers = self.HD)
					b = json.loads(r.text)
					
					for result in b['data']:
						self.idj.append(result['id'])
						self.anu.append(result['id'])
						self.wrt.write(result['id']+'\n')
						print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.anu)) + W + '] Writing Id... ',end='');sys.stdout.flush()
					
					if 'next' in str(b):
						self.Excute(b['paging']['next'])
					
					if len(self.anu) == 0:
						print(W + '[' + R + '!' + W + '] ' + R + 'lists members privat!')
					else: pass
				
				except KeyboardInterrupt:
							pass
					
			elif self.t == 'S':
				
				a = self.req.get(id, headers = self.HD)
				b = parser(a.content, 'html.parser')
				
				for result in b.find_all('a',href = True):
					c = result.find('div')
					
					if 'None' in str(c) or '+' in str(c):
						continue
					else:
						try:
							
							print( W + '\r|' + G + '•' + W + '| ' + c.text + '     ')
							r = re.findall(r'/(.*?)?refid=',result['href'])[0].replace('?','').replace('&','').replace('profile.phpid=','')
							wrt = open('result/dump/ID/search_ID.txt','a')
							wrt.write(r+'\n')
							wrt.close()
						
						except : pass
						
				cek = open('result/dump/ID/search_ID.txt').readlines()
				print(W + '\r[' + G + '*' + W + '] [' + R + str(len(cek)) + W + '] Writing id... ', end = '');sys.stdout.flush()
				
				if 'Lihat Hasil Selanjutnya' in str(b):
					e = b.find('a', string = 'Lihat Hasil Selanjutnya').get('href')
					self.Excute(e)
				else:
					print(W + '\n\n[' + G + '!' + W + '] no results anymore!')
					print(W + '[' + G + '!' + W + '] stopped!')
					print(W + '[' + G + '#' + W + '] file saved : ' + G + 'result/dump/ID/search_ID.txt')
					
			elif self.t == 'X':
				
				a = requests.get(id,headers = self.HD)
				b = json.loads(a.text)
				
				for result in b['data']:
					self.id.append(result['id'])
					self.wrt.write(result['id']+'\n')
					print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.id)) + W + '] Writing Id... ',end='');sys.stdout.flush()
					
				if 'next' in str(b):
					self.Excute(b['paging']['next'])
				else:
					self.wrt.close()
					print(W + '\n[' + G + '•' + W + '] done!')
					print(W + '[' + G + '#' + W + '] file saved : ' + G + 'result/dump/ID/' + self.groups + '_ID.txt')
					sys.exit()
			
		except KeyError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'error when grabbing id!')
			
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'check your connections!')
			sys.exit()
			
	def Cek(self):
		
		if self.e == '1':
			
			if os.path.exists('result/dump/ID/Myfriends_ID.txt'):
				if os.path.getsize('result/dump/ID/Myfriends_ID.txt') !=0:
					
					print(W + '\n[' + G +'!' + W + '] Myfriends_ID.txt exists!')
					dz = input(W + '[' + G +'?' + W + '] remove? [y/n] : ' + G)
					
					if dz.lower() == 'y':
						os.remove('result/dump/ID/Myfriends_ID.txt')
						print(W + '[' + G +'*' + W + '] success removed')
					else:
						print(W + '[' + G +'*' + W + '] ' + R + 'canceling')
						sys.exit()
						
				else: pass ; print()
			else: pass ; print()
		
		elif self.e == '2':
			
			if os.path.exists('result/dump/ID/' + self.target + '_ID.txt'):
				if os.path.getsize('result/dump/ID/' + self.target + '_ID.txt') !=0:
					
					print(W + '[' + G +'!' + W + '] ' + self.target + '_ID.txt exists!')
					dz = input(W + '[' + G +'?' + W + '] remove? [y/n] : ' + G)
					
					if dz.lower() == 'y':
						os.remove('result/dump/ID/' + self.target + '_ID.txt')
						print(W + '[' + G +'*' + W + '] success removed')
					else:
						print(W + '[' + G +'*' + W + '] ' + R + 'canceling')
						sys.exit()
						
				else: pass
			else: pass
		
		elif self.e == '3':
			
			if os.path.exists('result/dump/ID/' + self.groups + '_ID.txt'):
				if os.path.getsize('result/dump/ID/' + self.groups + '_ID.txt') !=0:
					
					print(W + '[' + G +'!' + W + '] ' + self.groups + '_ID.txt exists!')
					dz = input(W + '[' + G +'?' + W + '] remove? [y/n] : ' + G)
					
					if dz.lower() == 'y':
						os.remove('result/dump/ID/' + self.groups + '_ID.txt')
						print(W + '[' + G +'*' + W + '] success removed')
					else:
						print(W + '[' + G +'*' + W + '] ' + R + 'canceling')
						sys.exit()
						
				else: pass
			else: pass
		
		elif self.e == '4':
			
			if os.path.exists('result/dump/ID/jumpingF_ID.txt'):
				if os.path.getsize('result/dump/ID/jumpingF_ID.txt') !=0:
					
					print(W + '\n[' + G +'!' + W + '] jumpingF_ID.txt exists!')
					dz = input(W + '[' + G +'?' + W + '] remove? [y/n] : ' + G)
					
					if dz.lower() == 'y':
						os.remove('result/dump/ID/jumpingF_ID.txt')
						print(W + '[' + G +'*' + W + '] success removed')
					else:
						print(W + '[' + G +'*' + W + '] ' + R + 'canceling')
						sys.exit()
						
				else: pass ; print()
			else: pass ; print()
		
		elif self.e == '5':
			
			if os.path.exists('result/dump/ID/jumpingG_ID.txt'):
				if os.path.getsize('result/dump/ID/jumpingG_ID.txt') !=0:
					
					print(W + '\n[' + G +'!' + W + '] jumpingG_ID.txt exists!')
					dz = input(W + '[' + G +'?' + W + '] remove? [y/n] : ' + G)
					
					if dz.lower() == 'y':
						os.remove('result/dump/ID/jumpingG_ID.txt')
						print(W + '[' + G +'*' + W + '] success removed')
					else:
						print(W + '[' + G +'*' + W + '] ' + R + 'canceling')
						sys.exit()
						
				else: pass ; print()
			else: pass ; print()
		
		elif self.e == '6':
			
			if os.path.exists('result/dump/ID/jumpingFl_ID.txt'):
				if os.path.getsize('result/dump/ID/jumpingFl_ID.txt') !=0:
					
					print(W + '\n[' + G +'!' + W + '] jumpingFl_ID.txt exists!')
					dz = input(W + '[' + G +'?' + W + '] remove? [y/n] : ' + G)
					
					if dz.lower() == 'y':
						os.remove('result/dump/ID/jumpingFl_ID.txt')
						print(W + '[' + G +'*' + W + '] success removed')
					else:
						print(W + '[' + G +'*' + W + '] ' + R + 'canceling')
						sys.exit()
						
				else: pass ; print()
			else: pass ; print()
		
		elif self.e == '7':
			
			if os.path.exists('result/dump/ID/search_ID.txt'):
				if os.path.getsize('result/dump/ID/search_ID.txt') !=0:
					
					print(W + '\n[' + G +'!' + W + '] search_ID.txt exists!')
					dz = input(W + '[' + G +'?' + W + '] remove? [y/n] : ' + G)
					
					if dz.lower() == 'y':
						os.remove('result/dump/ID/search_ID.txt')
						print(W + '[' + G +'*' + W + '] success removed')
					else:
						print(W + '[' + G +'*' + W + '] ' + R + 'canceling')
						sys.exit()
						
				else: pass ; print()
			else: pass ; print()
		
	def Dmp(self):
		try:
			if self.e == '1':
				
				self.Cek()
				wrt = open('result/dump/ID/Myfriends_ID.txt','w')
				r = requests.get('https://graph.facebook.com/me/friends?access_token=' + self.token, headers = self.HD)
				b = json.loads(r.text)
				
				for result in b['data']:
					self.id.append(result['id'])
					wrt.write(result['id']+'\n')
					print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.id)) + W + '] Writing Id... ',end='');sys.stdout.flush();time.sleep(0.002)
				
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'no user id found!')
					sys.exit()
				else:
					wrt.close()
					print(W + '\n[' + G + '•' + W + '] done!')
					print(W + '[' + G + '#' + W + '] file saved : ' + G + 'result/dump/ID/Myfriends_ID.txt')
					sys.exit()
			
			elif self.e == '2':
				
				self.target = input(W + '\n[' + G + '?' + W + '] enter friends id : ' + G)
				self.Cek()
				a = requests.get('https://graph.facebook.com/' + self.target + '?access_token=' + self.token, headers = self.HD)
				i = json.loads(a.text)
				
				name = i['name']
				
				print(W + '[' + G + '+' + W + '] id from : ' + G + name)
				
				wrt = open('result/dump/ID/' + self.target + '_ID.txt','w')
				r = requests.get('https://graph.facebook.com/' + self.target + '/friends?access_token=' + self.token, headers = self.HD)
				b = json.loads(r.text)
				
				for result in b['data']:
					self.id.append(result['id'])
					wrt.write(result['id']+'\n')
					print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.id)) + W + '] Writing Id... ',end='');sys.stdout.flush();time.sleep(0.002)
					
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'no user id found!')
					sys.exit()
				else:
					wrt.close()
					print(W + '\n[' + G + '•' + W + '] done!')
					print(W + '[' + G + '#' + W + '] file saved : ' + G + 'result/dump/ID/' + self.target + '_ID.txt')
					sys.exit()
				
			elif self.e == '3':
				
				self.groups = input(W + '\n[' + G + '?' + W + '] enter groups id : ' + G)
				self.Cek()
				a = requests.get('https://graph.facebook.com/group/?id=' + self.groups + '&access_token=' + self.token, headers = self.HD)
				i = json.loads(a.text)
				
				self.t = 'X'
				name = i['name']
				
				print(W + '[' + G + '+' + W + '] id from : ' + G + name)
				
				self.wrt = open('result/dump/ID/' + self.groups + '_ID.txt','w')
				url_a = 'https://graph.facebook.com/' + self.groups + '/members?fields=id&limit=5000&access_token=' + self.token
				self.Excute(url_a)
					
			elif self.e == '4':
				
				self.Cek()
				r = requests.get('https://graph.facebook.com/me/friends?access_token=' + self.token, headers = self.HD)
				b = json.loads(r.text)
				
				for result in b['data']:
					self.id.append(result['id'])
					
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'no friends found!')
					sys.exit()
				else:
					print(W + '[' + G+ '+' + W + '] total friends (' + G + str(len(self.id)) + W + ')')
					limit = int(input(W + '[' + G + '?' + W + '] how many to jumping : ' + G))
					self.wrt = open('result/dump/ID/jumpingF_ID.txt','w')
					
					for ids in self.id:
						self.t = 'F'
						self.Excute(ids)
						self.count.append(ids)
						
						if len(self.count) == limit:
							self.wrt.close()
							print(W +'\n----------------------------------------')
							print(W + '\n[' + G + '•' + W + '] all done!')
							print(W + '[' + G + '*' + W + '] ' + G + str(len(self.idj)) + W + ' id retrieved')
							print(W + '[' + G + '#' + W + '] file saved : ' + G + 'result/dump/ID/jumpingF_ID.txt')
							sys.exit()
							
					self.wrt.close()
					print(W +'\n----------------------------------------')
					print(W + '\n[' + G + '•' + W + '] all done!')
					print(W + '[' + G + '*' + W + '] ' + G + str(len(self.idj)) + W + ' id retrieved')
					print(W + '[' + G + '#' + W + '] file saved : ' + G + 'result/dump/ID/jumpingF_ID.txt')
					sys.exit()
			
			elif self.e == '5':
				
				self.Cek()
				r = requests.get('https://graph.facebook.com/me/groups?access_token=' + self.token, headers = self.HD)
				b = json.loads(r.text)
				
				for result in b['data']:
					self.id.append(result['id'])
					
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'no groups found!')
					sys.exit()
				else:
					print(W + '[' + G+ '+' + W + '] total groups (' + G + str(len(self.id)) + W + ')')
					limit = int(input(W + '[' + G + '?' + W + '] how many to jumping : ' + G))
					print(W + '[' + G+ '!' + W + '] CTRL + C for skip')
					self.wrt = open('result/dump/ID/jumpingG_ID.txt','w')
					
					for ids in self.id:
						print(W +'\n----------------------------------------')
						self.anu = []
						
						a = requests.get('https://graph.facebook.com/' + ids + '?access_token=' + self.token, headers = self.HD)
						s = json.loads(a.text)
						
						name = s['name']
						
						print(W + '[' + G + '+' + W + '] dump id from : ' + G + name)
						url_a = 'https://graph.facebook.com/' + ids + '/members?fields=id&limit=5000&access_token=' + self.token
						self.t = 'G'
						self.Excute(url_a)
						self.count.append(ids)
						
						if len(self.count) == limit:
							self.wrt.close()
							print(W +'\n----------------------------------------')
							print(W + '\n[' + G + '•' + W + '] all done!')
							print(W + '[' + G + '*' + W + '] ' + G + str(len(self.idj)) + W + ' id retrieved')
							print(W + '[' + G + '#' + W + '] file saved : ' + G + 'result/dump/ID/jumpingG_ID.txt')
							sys.exit()
							
					self.wrt.close()
					print(W +'\n----------------------------------------')
					print(W + '\n[' + G + '•' + W + '] all done!')
					print(W + '[' + G + '*' + W + '] ' + G + str(len(self.idj)) + W + ' id retrieved')
					print(W + '[' + G + '#' + W + '] file saved : ' + G + 'result/dump/ID/jumpingG_ID.txt')
					sys.exit()
			
			elif self.e == '6':
				
				file = input(W + '[' + G + '?' + W + '] lists id : ' + G)
				
				for idne in open(file).readlines():
					self.id.append(idne.strip())
				
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'no uset id found!')
					sys.exit()
				else:
					print(W + '[' + G+ '+' + W + '] total id (' + G + str(len(self.id)) + W + ')')
					limit = int(input(W + '[' + G + '?' + W + '] how many to jumping : ' + G))
					self.wrt = open('result/dump/ID/jumpingFl_ID.txt','w')
					
					for ids in self.id:
						self.t = 'F'
						self.Excute(ids)
						self.count.append(ids)
						
						if len(self.count) == limit:
							self.wrt.close()
							print(W +'----------------------------------------')
							print(W + '\n[' + G + '•' + W + '] all done!')
							print(W + '[' + G + '*' + W + '] ' + G + str(len(self.idj)) + W + ' id retrieved')
							print(W + '[' + G + '#' + W + '] file saved : ' + G + 'result/dump/ID/jumpingFl_ID.txt')
							sys.exit()
							
					self.wrt.close()
					print(W +'----------------------------------------')
					print(W + '\n[' + G + '•' + W + '] all done!')
					print(W + '[' + G + '*' + W + '] ' + G + str(len(self.idj)) + W + ' id retrieved')
					print(W + '[' + G + '#' + W + '] file saved : ' + G + 'result/dump/ID/jumpingFl_ID.txt')
					sys.exit()
			
			elif self.e == '7':
				
				cekKuki.cek(self)
				self.Cek()
				name = input(W + '[' + G + '?' + W + '] search with name : ' + G)
				
				if name == '':
					print(W + '[' + R + '!' + W + '] ' + R + 'enter name!')
				else:
					print()
					s = self.req
					s.cookies = kuki('log/kuki')
					s.cookies.load()
					self.t = 'S'
					self.Excute(self.url.format('/search/people/?q=' + name))
					
		except KeyError:
			print(W + '[' + R + '!' + W + '] ' + R + 'failed when grabbing id!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
		
		except ValueError:
			print(W + '[' + R + '!' + W + '] ' + R + 'enter the numbers!')
			sys.exit()
			
		except IOError:
			print(W + '[' + R + '!' + W + '] ' + R + 'files not found!')
			sys.exit()
		
		except requests.exceptions.ConnectionError:
			print(W + '\r[' + R + '!' + W + '] ' + R + 'check your connections!')
			sys.exit()
		
	def Main(self):
		
		cek = input(W + '\n[ ' + R + 'Dz' + W +' ]•> ' + G)
		
		if cek in ['1','01']:
			self.e = '1'
			self.Dmp()
		elif cek in ['2','02']:
			self.e = '2'
			self.Dmp()
		elif cek in ['3','03']:
			self.e = '3'
			self.Dmp()
		elif cek in ['4','04']:
			self.e = '4'
			self.Dmp()
		elif cek in ['5','05']:
			self.e = '5'
			self.Dmp()
		elif cek in ['6','06']:
			self.e = '6'
			self.Dmp()
		elif cek in ['7','07']:
			self.e = '7'
			self.Dmp()
		elif cek in ['8','08']:
			import data.dumpEmail
			sys.exit()
		elif cek in ['9','09']:
			import data.dumpPhone
			sys.exit()
		elif cek in ['0','00']:
			os.system('python Fb.py')
		else:
			print(W + '[' + R +'!' + W +'] ' + R +'you stuppid!')
			sys.exit()

print(W + '\n  {' + G + '01' + W + '} Dump Id From My Friends')
print(W + '  {' + G + '02' + W + '} Dump Id From Friends')
print(W + '  {' + G + '03' + W + '} Dump Id From Groups')
print(W + '  {' + G + '04' + W + '} Dump Id From Friends ' + W +'(' + G + 'Jumping' + W + ')')
print(W + '  {' + G + '05' + W + '} Dump Id From groups ' + W +'(' + G + 'Jumping' + W + ')')
print(W + '  {' + G + '06' + W + '} Dump Id Using File ' + W +'(' + G + 'Jumping' + W + ')')
print(W + '  {' + G + '07' + W + '} Dump Id With Search Name')
print(W + '  {' + G + '08' + W + '} Dump Email From My Friends')
print(W + '  {' + G + '09' + W + '} Dump Phone Numbers From My Friends')
print(W + '  {' + R + '00' + W + '} Back')

try:
	Dump()
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()