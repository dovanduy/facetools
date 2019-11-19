#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, time, requests, json

global W, G, R
if sys.platform in ['linux','linux2']:
	W = '\033[0m'
	G = '\033[1;92m'
	R = '\033[1;91m'
else:
	W = ''
	G = ''
	R = ''

class Info:
	def __init__(self):
		self.token=open('log/token').read()
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.Main()
		
	def Main(self):
		try:
			
			friends = input(W + '\n[' + G + '?' + W + '] enter id or name : ' + G)
			for x in ['searching...','            ','searching...','            ','searching...','            ','searching...','            ','searching...','            ','searching...']:
				sys.stdout.write(W + '\r[' + G + '*' + W + '] ' + str(x));sys.stdout.flush();time.sleep(0.3)
			
			r = requests.get('https://graph.facebook.com/me/friends?access_token=' + self.token,headers = self.HD)
			a = json.loads(r.text)
			
			for dz in a['data']:
				if friends in dz['name'] or friends in dz['id']:
					
					print(W + '\n\n[-------- ' + G + 'INFORMATION' + W + ' --------]\n')
					
					b = requests.get('https://graph.facebook.com/' + dz['id'] + '?access_token=' + self.token, headers = self.HD)
					c = json.loads(b.text)
					
					try:
						print(W + '[' + G + '•' + W + '] Name : ' + G + c['name'])
					except KeyError: print(W + '[' + G + '•' + W + '] Name : ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] ID : ' + G + c['id'])
					except KeyError: print(W + '[' + G + '•' + W + '] ID : ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] Gender : ' + G + c['gender'])
					except KeyError: print(W + '[' + G + '•' + W + '] Gender : ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] Email : ' + G + c['email'])
					except KeyError: print(W + '[' + G + '•' + W + '] Email : ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] Mobile Phone : ' + G + c['mobile_phone'])
					except KeyError: print(W + '[' + G + '•' + W + '] Mobile Phone : ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] Birthday : ' + G + c['birthday'])
					except KeyError: print(W + '[' + G + '•' + W + '] Birthday : ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] Location : ' + G + c['location']['name'])
					except KeyError: print(W + '[' + G + '•' + W + '] Location : ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] Hometown : ' + G + c['hometown']['name'])
					except KeyError: print(W + '[' + G + '•' + W + '] Hometown : ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] Bio : ' + G + c['bio'])
					except KeyError: print(W + '[' + G + '•' + W + '] Bio : ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] Quotes : ' + G + c['quotes'])
					except KeyError: print(W + '[' + G + '•' + W + '] Quotes : ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] Relationship status : ' + G + c['relationship_status'])
					except KeyError: print(W + '[' + G + '•' + W + '] Relationship status : ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] Religion : ' + G + c['religion'])
					except KeyError: print(W + '[' + G + '•' + W + '] Religion : ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] Political : ' + G + c['political'])
					except KeyError: print(W + '[' + G + '•' + W + '] Political : ' + R + 'not found!')
					try:
						if c['start_date'] == '0000-00':
							print(W + '[' + G + '•' + W + '] Start Date : ---')
						else:
							print(W + '[' + G + '•' + W + '] Start Date : ' + G + c['start_date'])
					except KeyError: pass
					try:
						if c['end_date'] == '0000-00':
							print(W + '[' + G + '•' + W + '] End Date : ---')
						else:
							print(W + '[' + G + '•' + W + '] End Date : ' + G + c['end_date'])
					except KeyError: pass
					try:
						print(W + '[' + G + '•' + W + '] Link : ' + G + c['link'])
					except KeyError: print(W + '[' + G + '•' + W + '] Link : ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] Languages : ')
						for x in c['languages']:
							try:
								print(W + '    ~ ' + G + x['name'])
							except KeyError:
								print(W + '    ~ ' + R + 'not found!')
					except KeyError: print(W + '    ~ ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] School : ')
						for x in c['education']:
							try:
								print(W + '    ~ ' + G + x['school']['name'])
							except KeyError:
								print(W + '    ~ ' + R + 'not found!')
					except KeyError: print(W + '    ~ ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] Favorite athletes : ')
						for x in c['favorite_athletes']:
							try:
								print(W + '    ~ ' + G + x['name'])
							except KeyError:
								print(W + '    ~ ' + R + 'not found!')
					except KeyError: print(W + '    ~ ' + R + 'not found!')
					try:
						print(W + '[' + G + '•' + W + '] Favorite teams : ')
						for x in c['favorite_teams']:
							try:
								print(W + '    ~ ' + G + x['name'])
							except KeyError:
								print(W + '    ~ ' + R + 'not found!')
					except KeyError: print(W + '    ~ ' + R + 'not found!')
					
					print(W +'\n[' + G + '•' + W + '] done!')
					sys.exit()
				
			print(W + '\n[' + R + '!' + W + '] ' + R + 'user not found!')
			sys.exit()
							
		except KeyError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'error!,exit')
			sys.exit()
		
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
Info()