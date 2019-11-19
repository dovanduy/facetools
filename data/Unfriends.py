#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, time, requests, json
from multiprocessing.pool import ThreadPool

global W, G, R, Y
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

class Unfriends:
	def __init__(self):
		self.token = open('log/token').read()
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.id = []
		self.Main()
	
	def Excute(self,id):
		try:
			r = requests.get('https://graph.facebook.com/' + str(id) + '/feed?access_token=' + self.token + '&limit=1', headers = self.HD)
			a = json.loads(r.text)
			
			b = requests.get('https://graph.facebook.com/' + str(id) + '?access_token=' + self.token, headers = self.HD)
			c = json.loads(b.text)
			
			time = a['data'][0]['created_time'].split('-')[0]
			name = c['name']
			
			if time < self.year:
				rr = requests.delete('https://graph.facebook.com/me/friends?uid=' + str(id) + '&access_token=' + self.token, headers = self.HD)
				if rr.json() == True:
					print(W + '[' + R + str(time) + W +'] ' + G + str(name) + W + ' - INACTIVE - ' + G + 'removed')
				else:
					print(W + '[' + R + str(time) + W +'] ' + G + str(name) + W + ' - INACTIVE - ' + R + 'failed')
			else:
				print(W + '[' + G + str(time) + W +'] ' + G + str(name) + W + ' - ACTIVE - ' + G + 'next')
		
		except: pass
	
	def Unf(self):
		try:
			if self.e == '1':
				
				self.year = input(W + '\n[' + G + '?' + W + '] YEAR : ' + G)
				print(W + '[' + G + '*' + W + '] Get user id... ')
				
				r = requests.get('https://graph.facebook.com/me/friends?access_token=' + self.token,headers = self.HD)
				a = json.loads(r.text)
				
				for result in a['data']:
					self.id.append(result['id'])
				
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] no friends found!')
					sys.exit()
				
				date = time.strftime('%Y')
				if self.year == '':
					self.year = date
				
				print()
				m = ThreadPool(10)
				m.map(self.Excute,self.id)
				exit(W + '\n[' + G + '•' + W + '] done!')
				
			elif self.e == '2':
				
				print(W + '\n[' + G + '*' + W + '] Get user id...')
				
				r = requests.get('https://graph.facebook.com/me/friends?access_token=' + self.token,headers = self.HD)
				a = json.loads(r.text)
				
				print()
				for result in a['data']:
					rr = requests.delete('https://graph.facebook.com/me/friends?uid=' + str(result['id']) + '&access_token=' + self.token, headers = self.HD)
					self.id.append(result['id'])
					if rr.json() == True:
						print(W + '[' + G + '-' + W +'] ' + G + str(result['name']) + W + ' - removed')
					else:
						print(W + '[' + R + '×' + W +'] ' + G + str(result['name']) + W + ' - failed')
				
				if len(self.id) == 0:
					print(W + '[' + R + '!' + W + '] no friends found!')
					sys.exit()
				
				exit(W + '\n[' + G + '•' + W + '] done!')
			
			elif self.e == '3':
				
				tipe = input(W + '\n[' + G + '?' + W + '] gender [f/m] : ' + G)
				if tipe.lower() == 'f':
					gen = 'female'
				elif tipe.lower() == 'm':
					gen = 'male'
				else: exit(W + '[' + R + '!' + W + '] ' + R + 'stuppid!')
				print(W + '[' + G + '*' + W + '] Get user id...')
				
				r = requests.get('https://graph.facebook.com/me/friends?access_token=' + self.token,headers = self.HD)
				a = json.loads(r.text)
				
				print('')
				for result in a['data']:
					try:
						p = requests.get('https://graph.facebook.com/'+str(result['id'])+'?access_token=' + self.token,headers = self.HD)
						if gen in p.json()['gender']:
							rr = requests.delete('https://graph.facebook.com/me/friends?uid=' + str(result['id']) + '&access_token=' + self.token, headers = self.HD)
							if rr.json() == True:
								print(W + '[' + G + '-' + W +'] ' + G + str(result['name']) + W + ' - removed')
							else:
								print(W + '[' + R + '×' + W +'] ' + G + str(result['name']) + W + ' - failed')
					except: pass
				
				exit(W + '\n[' + G + '•' + W + '] done!')
					
		except KeyError:
			print(W + '[' + R + '!' + W + '] ' + R + 'error when grabbing id!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
			
		except requests.exceptions.ConnectionError:
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
				
	def Main(self):
		
		cek = input(W + '\n[ ' + R + 'Dz' + W +' ]•> ' + G)
		
		if cek in ['1','01']:
			self.e = '1'
			self.Unf()
		elif cek in ['2','02']:
			self.e = '2'
			self.Unf()
		elif cek in ['3','03']:
			self.e = '3'
			self.Unf()
		elif cek in ['0','00']:
			os.system('python Fb.py')
		else:
			exit(W + '[' + R + '!' + W + '] ' + R + 'you stuppid!')
try:
	print(W + '\n  {' + G + '01' + W + '} Unfriends Inactive User')
	print(W + '  {' + G + '02' + W + '} Unfriends All Friends')
	print(W + '  {' + G + '03' + W + '} Unfriends Based On Gender')
	print(W + '  {' + R + '00' + W + '} Back')
	Unfriends()
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()