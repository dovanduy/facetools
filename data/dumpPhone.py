#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, time, requests, json
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
	os.mkidr('result/dump')
except: pass
try:
	os.mkdir('result/dump/phone')
except: pass

class Dump:
	def __init__(self):
		self.token = open('log/token').read()
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.id = []
		self.Main()
		
	def Excute(self,id):
		try:
			
			r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + self.token, headers = self.HD)
			b = json.loads(r.text)
			
			print(W + '|' + G + '•' + W + '| ' + G + b['name'] + R + ' >> ' + W + b['mobile_phone'])
			wrt.write(b['mobile_phone'] + '\n')
			
		except : pass
		
	def Threads(self):
		global wrt
		try:
			threads = int(input(W + '\n[' + G + '?' + W + '] threads 1-100 : ' + G))
		
		except ValueError:
			print(W + '[' + R + '!' + W + '] ' + R + 'enter the numbers!')
			self.Threads()
		
		if threads >100:
			print(W + '[' + R + '!' + W + '] ' + R + 'exceeds the limit!')
			self.Threads()
		
		print()
		wrt = open('result/dump/phone/phone.txt','w')
		m = ThreadPool(threads)
		m.map(self.Excute,self.id)
		wrt.close()
		print(W +'\n[' + G + '•' + W + '] done!')
		print(W +'[' + G + '#' + W + '] file saved : '+ G + 'result/dump/phone/phone.txt')
		sys.exit()
		
	def Cek(self):
		if os.path.exists('result/dump/phone/phone.txt'):
			if os.path.getsize('result/dump/phone/phone.txt') !=0:
				
				print(W + '\n[' + G +'!' + W + '] phone.txt exists!')
				dz = input(W + '[' + G +'?' + W + '] remove? [y/n] : ' + G)
					
				if dz.lower() == 'y':
					os.remove('result/dump/phone/phone.txt')
					print(W + '[' + G +'*' + W + '] success removed')
				else:
					print(W + '[' + G +'*' + W + '] ' + R + 'canceling')
					sys.exit()
					
			else : pass ; print()
		else : pass ; print()
		
	def Main(self):
		try:
			self.Cek()
			r = requests.get('https://graph.facebook.com/me/friends?access_token=' + self.token, headers = self.HD)
			a = json.loads(r.text)
			
			for result in a['data']:
				self.id.append(result['id'])
				print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.id)) + W + '] GET Id... ',end='');sys.stdout.flush();time.sleep(0.002)
			
			if len(self.id) == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'no friends found!')
				sys.exit()
			else:
				self.Threads()
		
		except KeyError:
			print(W + '[' + R + '!' + W + '] ' + R + 'error when grabbing id!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
			
		except requests.exceptions.ConnectionError:
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
try:
	Dump()
except KeyboardInterrupt:
	wrt.close()
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()