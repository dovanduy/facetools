#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import os, sys, requests, json
from data import cekKuki
from bs4 import BeautifulSoup as parser
from http.cookiejar import LWPCookieJar as kuki

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

def Excute(user,msg):
	try:
		data = []
		a = s.get(url.format('/messages/read/?tid=cid.c.' + str(user)),headers = HD)
		b = parser(a.content, 'html.parser')
		
		print(W +'[' + G + '*' + W + '] send a message to' + G, user)
		for x in b('form'):
			if '/messages/send/?' in x['action']:
				data.append(x['action'])
		
		for x in b('input'):
			try:
				if 'fb_dtsg' in x['name']:
					data.append(x['value'])
				if 'jazoest' in x['name']:
					data.append(x['value'])
					break
			except: pass
		
		if len(data) == 3:
			URL = url.format(data[0])
			form = {'fb_dtsg' : data[1], 'jazoest' : data[2], 'ids[' + str(user) + ']' : str(user), 'body' : msg, 'send' : 'Kirim'}
			p = s.post(URL, data = form, headers = HD)
			if 'send_success' in str(p.text):
				print(W +'[' + G + '-' + W + '] success')
			else:
				print(W +'[' + R + 'x' + W + '] failed')
		else:
			print(W +'[' + R + 'x' + W + '] failed')
			
	except requests.exceptions.ConnectionError:
		print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
		print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
		sys.exit()
	
def Get(pil):
	try:
		if pil == 'mass':
			
			limit = int(input(W + '\n[' + G + '?' + W + '] how many : ' + G))
			print(W + "[" + G + "!" + W + "] type '</>' for change lines")
			msg = input(W + '[' + G + '?' + W + '] message : ' + G)
			if msg == '':
				exit(W + '[' + R + '!' + W + '] ' + R + 'stuppid!')
			
			print('')
			msg = msg.replace('</>','\n')
			a = requests.get('https://graph.facebook.com/me/friends?access_token=' + token, headers = HD)
			z = json.loads(a.text)
			
			for i in z['data']:
				id.append(i['id'])
				Excute(i['id'],msg)
				
				if len(id) == limit:
					print(W + '\n[' + G + '•' + W + '] done!')
					sys.exit()
			
			if len(id) == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'no friends found!')
				sys.exit()
			else:
				print(W + '\n[' + G + '•' + W + '] done!')
				sys.exit()
		
		elif pil == 'online':
			
			limit = int(input(W + '\n[' + G + '?' + W + '] how many : ' + G))
			print(W + "[" + G + "!" + W + "] type '</>' for change lines")
			msg = input(W + '[' + G + '?' + W + '] message : ' + G)
			if msg == '':
				exit(W + '[' + R + '!' + W + '] ' + R + 'stuppid!')
			
			print('')
			msg = msg.replace('</>','\n')
			a = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit(' + str(limit) + ')&access_token=' + token, headers = HD)
			z = json.loads(a.text)
			
			for i in z['home']['data']:
				ids = i['id'].split('_')[0]
				id.append(ids)
				Excute(ids,msg)
				
				if len(id) == limit:
					print(W + '\n[' + G + '•' + W + '] done!')
					sys.exit()
			
			if len(id) == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'no user found!')
				sys.exit()
			else:
				print(W + '\n[' + G + '•' + W + '] done!')
				sys.exit()
		
		elif pil == 'target':
			
			target = input(W + '\n[' + G + '?' + W + '] target id : ' + G)
			limit = int(input(W + '[' + G + '?' + W + '] looping : ' + G))
			print(W + "[" + G + "!" + W + "] type '</>' for change lines")
			msg = input(W + '[' + G + '?' + W + '] message : ' + G)
			if msg == '':
				exit(W + '[' + R + '!' + W + '] ' + R + 'stuppid!')
			
			print('')
			msg = msg.replace('</>','\n')
			a = requests.get('https://graph.facebook.com/' + str(target) + '?access_token=' + token, headers = HD)
			z = json.loads(a.text)
			
			for i in range(limit):
				Excute(z['id'],msg)
			
			print(W + '\n[' + G + '•' + W + '] done!')
			sys.exit()
				
	except KeyError:
		print(W + '[' + R + '!' + W + '] ' + R + 'error when grabbing user id!')
		print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
		sys.exit()
	except ValueError:
		print(W + '[' + R + '!' + W + '] ' + R + 'enter the numbers!')
		Get(pil)
	except requests.exceptions.ConnectionError:
		print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
		print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
		sys.exit()

try:
	global token, HD
	url = 'https://mbasic.facebook.com{}'
	token = open('log/token').read()
	HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
	s = requests.Session()
	s.cookies = kuki('log/kuki')
	s.cookies.load()
	id = []
	
	print(W + '\n  {' + G + '01' + W + '} Mass Chat')
	print(W + '  {' + G + '02' + W + '} Mass Chat Online User')
	print(W + '  {' + G + '03' + W + '} Chat Spammer Target')
	print(W + '  {' + R + '00' + W + '} Back')
	
	cek = input(W + '\n[ ' + R + 'Dz' + W +' ]•> ' + G)
	
	if cek in ['1','01']:
		pil = 'mass'
		Get(pil)
	elif cek in ['2','02']:
		pil = 'online'
		Get(pil)
	elif cek in ['3','03']:
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