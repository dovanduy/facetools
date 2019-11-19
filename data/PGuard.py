#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, requests

global W, G, R
if sys.platform in ['linux','linux2']:
	W = '\033[0m'
	G = '\033[1;92m'
	R = '\033[1;91m'
else:
	W = ''
	G = ''
	R = ''

class Guard:
	def __init__(self):
		self.HD = open('UserAgent/ua.txt').read()
		self.token = open('log/token').read()
		self.Main()
	
	def Grd(self, guard = True):
		try:
			e = requests.get('https://graph.facebook.com/me?access_token='+self.token,headers = {'User-Agent' : self.HD})
			id = e.json()['id']
			data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation'%(guard,str(id))
			headers = {"Content-Type" : "application/x-www-form-urlencoded", "User-Agent" : self.HD, "Authorization" : "OAuth %s" % self.token}
			s = requests.post('https://graph.facebook.com/graphql', data = data, headers = headers)
			result = s.json()
			if result["data"]["is_shielded_set"]["is_shielded"] == True:
				print(W + '\n[' + G + '*' + W + '] guard activated.')
			elif result["data"]["is_shielded_set"]["is_shielded"] == False:
				print(W + '\n[' + R + '*' + W + '] guard is turned off.')
			else:
				print(W + '\n[' + R + '*' + W + '] error.')
		except KeyError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'error')
			sys.exit()
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
		print(W + '[' + G + '•' + W + '] done!')
		sys.exit()
					
	def Main(self):
		print(W + '\n  {' + G + '01' + W + '} Guard Active')
		print(W + '  {' + G + '02' + W + '} Guard Non Active')
		print(W + '  {' + R + '00' + W + '} Back')
		cek = input(W + '\n[ ' + R + 'Dz' + W +' ]•> ' + G)
		if cek in ['1','01']:
			self.Grd('true')
		elif cek in ['2','02']:
			self.Grd('false')
		elif cek in ['0','00']:
			os.system('python Fb.py')
		else:
			print(W + '[' + R + '!' + W + '] ' + R + 'you stuppid!')
			sys.exit()
Guard()