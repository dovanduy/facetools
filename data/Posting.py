#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, requests, json

global W, G, R
if sys.platform in ['linux','linux2']:
	W = '\033[0m'
	G = '\033[1;92m'
	R = '\033[1;91m'
else:
	W = ''
	G = ''
	R = ''

def Excute(id,poto,msg):
		try:
			parm = {'access_token' : token, 'message' : msg}
			file = {'file' : open(poto,'rb')}
			url = 'https://graph.facebook.com/{}/photos?'.format(id)
			s = requests.post(url, data = parm, files = file, headers = HD)
			try:
				
				error = s.json()['error']['message']
				print(W + '[' + R + '×' + W + '] - failed')
			except KeyError:
				print(W + '[' + G + 'success' + W + '] url : facebook.com/'+str(s.json()['id']))
				
		except IOError:
			url = 'https://graph.facebook.com/{}/feed?'.format(id)
			s = requests.post(url, data = parm, headers = HD)
			try:
				
				error = s.json()['error']['message']
				print(W + '[' + R + '×' + W + '] - failed')
			except KeyError:
				print(W + '[' + G + 'success' + W + '] url : facebook.com/'+str(s.json()['id']))
		
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
				
def Post(pil):
	try:
		if pil == 'home':
			print(W +"\n[" + G + "!" + W + "] skip if without photos")
			poto = input(W + '[' + G + '?' + W +'] file photos : ' + G)
			print(W +"[" + G + "!" + W + "] type '</>' for change lines")
			msg = input(W + '[' + G + '?' + W +'] captions : ' + G)
			
			print('')
			id = 'me'
			msg = msg.replace('</>','\n')
			Excute(id,poto,msg)
		
		elif pil == 'friends':
			
			print(W +"\n[" + G + "!" + W + "] skip if without photos")
			poto = input(W + '[' + G + '?' + W +'] file photos : ' + G)
			print(W +"[" + G + "!" + W + "] type '</>' for change lines")
			msg = input(W + '[' + G + '?' + W +'] captions : ' + G)
			
			print('')
			msg = msg.replace('</>','\n')
			r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token, headers = HD)
			p = json.loads(r.text)
			
			for i in p['data']:
				
				id = i['id']
				userid.append(id)
				Excute(id,poto,msg)
			
			if len(userid) == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'no friends found!')
				sys.exit()
			else:
				print(W + '\n[' + G + '•' + W + '] done!')
		
		elif pil == 'groups':
			
			print(W +"\n[" + G + "!" + W + "] skip if without photos")
			poto = input(W + '[' + G + '?' + W +'] file photos : ' + G)
			print(W +"[" + G + "!" + W + "] type '</>' for change lines")
			msg = input(W + '[' + G + '?' + W +'] captions : ' + G)
			
			print('')
			msg = msg.replace('</>','\n')
			r = requests.get('https://graph.facebook.com/me/groups?access_token=' + token, headers = HD)
			p = json.loads(r.text)
			
			for i in p['data']:
				
				id = i['id']
				userid.append(id)
				Excute(id,poto,msg)
			
			if len(userid) == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'no groups found!')
				sys.exit()
			else:
				print(W + '\n[' + G + '•' + W + '] done!')
						
	except KeyError:
		print(W + '[' + R + '!' + W + '] ' + R + 'error when grabbing id!')
		print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
		sys.exit()
	except requests.exceptions.ConnectionError:
		print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
		print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
		sys.exit()
	
try:
	userid = []
	global token, HD
	token = open('log/token').read()
	HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
	
	print(W + '\n  {' + G + '01' + W + '} Post In Your Timeline')
	print(W + '  {' + G + '02' + W + '} Post In Friends Timeline')
	print(W + '  {' + G + '03' + W + '} Post In Your Groups')
	print(W + '  {' + R + '00' + W + '} Back')
	
	cek = input(W + '\n[ ' + R + 'Dz' + W +' ]•> ' + G)
	
	if cek in ['1','01']:
		pil = 'home'
		Post(pil)
	elif cek in ['2','02']:
		pil = 'friends'
		Post(pil)
	elif cek in ['3','03']:
		pil = 'groups'
		Post(pil)
	elif cek in ['0','00']:
		os.system('python Fb.py')
	else:
		exit(W + '[' + R + '!' + W + '] ' + R + 'stuppid!')
		
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()