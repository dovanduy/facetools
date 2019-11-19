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

def Excute(postid,msg,poto):
	try:
		parm = {'access_token' : token, 'message' : msg}
		print('')
		
		for ids in postid:
			
			file = {'file' : open(poto,'rb')}
			url = 'https://graph.facebook.com/{}/comments/photos?'.format(ids)
			s = requests.post(url, data = parm, files = file, headers = HD)
			try:
				
				error = s.json()['error']['message']
				print(W + '[' + R + '×' + W + ']', str(ids),'- failed')
			except KeyError:
				print(W + '[' + G + '-' + W + ']', str(ids),'- comented with photo')
		
	except IOError:
		url = 'https://graph.facebook.com/{}/comments'.format(ids)
		s = requests.post(url, data = parm, headers = HD)
		try:
				
			error = s.json()['error']['message']
			print(W + '[' + R + '×' + W + ']', str(ids),'- failed')
		except KeyError:
			print(W + '[' + G + '-' + W + ']', str(ids),'- comented without photo')
			
	except requests.exceptions.ConnectionError:
		print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
		print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
		sys.exit()

def Get(pil):
	try:
		if pil == 'home':
			limit = int(input(W + '\n[' + G + '?' + W +'] how many : ' + G))
			print(W +"[" + G + "!" + W + "] skip if without photos")
			poto = input(W + '[' + G + '?' + W +'] file photos : ' + G)
			print(W +"[" + G + "!" + W + "] type '</>' for change lines")
			msg = input(W + '[' + G + '?' + W +'] message : ' + G)
			print(W + '[' + G + '*' + W + '] GET posts id... ')
			
			msg = msg.replace('</>','\n')
			r = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit(' + str(limit) + ')&access_token=' + token, headers = HD)
			p = json.loads(r.text)
			
			for i in p['home']['data']:
				postid.append(i['id'])
			
			if len(postid) == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'no posts found!')
				sys.exit()
			else:
				Excute(postid,msg,poto)
				print(W + '\n[' + G + '•' + W + '] done!')
		
		elif pil == 'target':
			
			target = input(W + '\n[' + G + '?' + W +'] enter target id : ' + G)
			limit = int(input(W + '[' + G + '?' + W +'] how many : ' + G))
			print(W +"[" + G + "!" + W + "] skip if without photos")
			poto = input(W + '[' + G + '?' + W +'] file photos : ' + G)
			print(W +"[" + G + "!" + W + "] type '</>' for change lines")
			msg = input(W + '[' + G + '?' + W +'] message : ' + G)
			print(W + '[' + G + '*' + W + '] GET posts id... ')
			
			msg = msg.replace('</>','\n')
			r = requests.get('https://graph.facebook.com/v3.0/' + str(target) + '?fields=feed.limit(' + str(limit) + ')&access_token=' + token, headers = HD)
			p = json.loads(r.text)
			
			for i in p['feed']['data']:
				postid.append(i['id'])
			
			if len(postid) == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'no posts found!')
				sys.exit()
			else:
				Excute(postid,msg,poto)
				print(W + '\n[' + G + '•' + W + '] done!')
						
	except KeyError:
		print(W + '[' + R + '!' + W + '] ' + R + 'error when grabbing posts id!')
		print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
		sys.exit()
	except ValueError:
		print(W + '[' + R + '!' + W + '] ' + R + 'enter the numbers!')
		Get(tipe,pil)
	except requests.exceptions.ConnectionError:
		print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
		print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
		sys.exit()
	
try:
	postid = []
	global token, HD
	token = open('log/token').read()
	HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
	
	print(W + '\n  {' + G + '01' + W + '} Comment Home')
	print(W + '  {' + G + '02' + W + '} Bom Comment Target')
	print(W + '  {' + R + '00' + W + '} Back')
	
	cek = input(W + '\n[ ' + R + 'Dz' + W +' ]•> ' + G)
	
	if cek in ['1','01']:
		pil = 'home'
		Get(pil)
	elif cek in ['2','02']:
		pil = 'target'
		Get(pil)
	elif cek in ['0','00']:
		os.system('python Fb.py')
	else:
		exit(W + '[' + R + '!' + W + '] ' + R + 'stuppid!')
		
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()