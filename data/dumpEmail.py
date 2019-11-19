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
	os.mkdir('result/dump/email')
except: pass

class Dump:
	def __init__(self):
		self.loop = 0
		self.token = open('log/token').read()
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.id = []
		self.yahoo = []
		self.hotmail = []
		self.gmail = []
		self.other = []
		self.Main()
		
	def Excute(self,id):
		try:
			
			self.loop +=1
			r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + self.token, headers = self.HD)
			b = json.loads(r.text)
			
			if '@yahoo.com' in str(b['email']):
				fil = open('result/dump/email/ymail.txt','a')
				fil.write(b['email']+'\n')
				fil.close()
				self.yahoo.append(W + b['email'])
					
			elif '@hotmail.com' in str(b['email']):
				fil = open('result/dump/email/hotmail.txt','a')
				fil.write(b['email']+'\n')
				fil.close()
				try:
					self.hotmail.append(W + b['email'] + ' -> ' + b['birthday'].replace('/','-'))
				except KeyError:
					self.hotmail.append(W + b['email'] + ' -> --')
			
			elif '@gmail.com' in str(b['email']):
				fil = open('result/dump/email/gmail.txt','a')
				fil.write(b['email']+'\n')
				fil.close()
				self.gmail.append(W + b['email'])
			
			else:
				fil = open('result/dump/email/other.txt','a')
				fil.write(b['email']+'\n')
				fil.close()
				self.other.append(W + b['email'])
		except: pass
		print(W + '\r[' + G + '*' + W + '] searching email ' + str(self.loop) + '/' + str(len(self.id))+ ' please wait... ',end = '');sys.stdout.flush()
	
	def Results(self):
		if len(self.yahoo) !=0:
			print(W + '\n\n[----------- ' + G + 'YAHOO' + W + ' -----------]\n')
			for x in self.yahoo : print(W + '|' + G + '•' + W + '| ' + str(x))
			print(W +'[' + G + '#' + W + '] yahoo saved : '+ G + 'result/dump/email/ymail.txt')
		if len(self.hotmail) !=0:
			print(W + '\n\n[---------- ' + G + 'HOTMAIL' + W + ' ----------]\n')
			for x in self.hotmail : print(W + '|' + G + '•' + W + '| ' + str(x))
			print(W +'[' + G + '#' + W + '] hotmail saved : '+ G + 'result/dump/email/hotmail.txt')
		if len(self.gmail) !=0:
			print(W + '\n\n[----------- ' + G + 'GMAIL' + W + ' -----------]\n')
			for x in self.gmail : print(W + '|' + G + '•' + W + '| ' + str(x))
			print(W +'[' + G + '#' + W + '] gmail saved : '+ G + 'result/dump/email/gmail.txt')
		if len(self.other) !=0:
			print(W + '\n\n[----------- ' + G + 'OTHER' + W + ' -----------]\n')
			for x in self.other : print(W + '|' + G + '•' + W + '| ' + str(x))
			print(W +'[' + G + '#' + W + '] other saved : '+ G + 'result/dump/email/other.txt')
		if len(self.yahoo) == 0 and len(self.hotmail) == 0 and len(self.gmail) == 0 and len(self.other) == 0:
			print(W + '\n\n[' + R + '!' + W + '] ' + R + 'no result found!')
		
	def Threads(self):
		try:
			threads = int(input(W + '\n[' + G + '?' + W + '] threads 1-100 : ' + G))
		
		except ValueError:
			print(W + '[' + R + '!' + W + '] ' + R + 'enter the numbers!')
			self.Threads()
		
		if threads >100:
			print(W + '[' + R + '!' + W + '] ' + R + 'exceeds the limit!')
			self.Threads()
		
		m = ThreadPool(threads)
		m.map(self.Excute,self.id)
		self.Results()
		sys.exit()
		
	def Main(self):
		try:
			print()
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
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt, exit.')
	sya.exit()
