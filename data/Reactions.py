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

def Excute(postid,tipe):
	try:
		parm = {'access_token' : token, 'type' : tipe}
		print(W + '[' + G + '*' + W + '] reaction type',tipe,'\n')
		
		for ids in postid:
			
			url = 'https://graph.facebook.com/{}/reactions'.format(ids)
			cp = 'https://graph.facebook.com/{}?access_token={}'.format(ids,token)
			
			s = requests.post(url, data = parm, headers = HD)
			a = requests.get(cp, headers = HD)
			try:
				
				id = ids.split('_')[1]
				cek = s.json()['success']
				try:
					print(W + '[' + G + str(id) + W + '] ' + str(a.json()['message'][:40].replace('\n',' ')) + G + ' - ' + W + 'reacted')
				except KeyError:
					try:
						print(W + '[' + G + str(id) + W + '] ' + str(a.json()['story'][:40].replace('\n',' ')) + G + ' - ' + W + 'reacted')
					except KeyError:
						print(W + '[' + R + str(id) + W + '] failed')
			
			except KeyError:
				try:
					print(W + '[' + R + str(id) + W + '] ' + str(a.json()['message'][:40].replace('\n',' ')) + G + ' - ' + W + 'failed')
				except KeyError:
					try:
						print(W + '[' + R + str(id) + W + '] ' + str(a.json()['story'][:40].replace('\n',' ')) + G + ' - ' + W + 'failed')
					except KeyError:
						print(W + '[' + R + str(id) + W + '] failed')
			
	except requests.exceptions.ConnectionError:
		print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
		print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
		sys.exit()

def Excute2(id,msg,tipe):
	try:
		parm = {'access_token' : token, 'type' : tipe}
		url = 'https://graph.facebook.com/v3.2/{}/reactions'.format(id)
		
		s = requests.post(url, data = parm, headers = HD)
		
		try:
			ids = id.split('_')[1]
			cek = s.json()['success']
			print(W + '[' + G + str(ids) + W + '] ' + str(msg[:40].replace('\n',' ')) + G + ' - ' + W + 'reacted')
		except KeyError:
			print(W + '[' + R + str(ids) + W + '] ' + str(msg[:40].replace('\n',' ')) + G + ' - ' + W + 'failed')
		
	except requests.exceptions.ConnectionError:
		print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
		print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
		sys.exit()

def Get(tipe,pil):
	try:
		if pil == 'home':
			limit = int(input(W + '\n[' + G + '?' + W +'] how many : ' + G))
			print(W + '[' + G + '*' + W + '] GET posts id... ')
			
			r = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit(' + str(limit) + ')&access_token=' + token, headers = HD)
			p = json.loads(r.text)
			
			for i in p['home']['data']:
				postid.append(i['id'])
			
			if len(postid) == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'no posts found!')
				sys.exit()
			else:
				Excute(postid,tipe)
				print(W + '\n[' + G + '•' + W + '] done!')
		
		elif pil == 'target':
			
			target = input(W + '\n[' + G + '?' + W +'] enter target id : ' + G)
			limit = int(input(W + '[' + G + '?' + W +'] how many : ' + G))
			
			r = requests.get('https://graph.facebook.com/v3.0/' + str(target) + '?fields=feed.limit(' + str(limit) + ')&access_token=' + token, headers = HD)
			p = json.loads(r.text)
			
			for i in p['feed']['data']:
				postid.append(i['id'])
			
			if len(postid) == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'no posts found!')
				sys.exit()
			else:
				Excute(postid,tipe)
				print(W + '\n[' + G + '•' + W + '] done!')
		
		elif pil == 'comment':
			
			count = 0
			target = input(W + '\n[' + G + '?' + W +'] enter target id : ' + G)
			print('')
			
			r = requests.get('https://graph.facebook.com/v3.0/' + str(target) + '?fields=feed.limit(5000)&access_token=' + token, headers = HD)
			p = json.loads(r.text)
			
			for i in p['feed']['data']:
				count +=1
				postid.append(i['id'])
				try:
					print(G + str(count) + W + '.',i['message'][:40].replace('\n',' '))
					
				except KeyError:
					try:
						print(G + str(count) + W + '.', i['story'][:40].replace('\n',' '))
						
					except KeyError:
						print(G + str(count) + W + '. upload a photo/video')
						
			if len(postid) == 0:
				print(W + '[' + R + '!' + W + '] ' + R + 'no posts found!')
				sys.exit()
			try:
				com = []
				cek = int(input(W + '\n[ ' + R + 'Select Numbers' + W +' ]•> ' + G))
				a = requests.get('https://graph.facebook.com/v3.2/' + str(postid[cek-1]) + '/comments?limit=5000&access_token=' + token, headers = HD)
				z = json.loads(a.text)
				
				print(W + '\n[' + G + '*' + W + '] reaction post_id ',postid[cek-1])
				print(W + '[' + G + '*' + W + '] type',tipe,'\n')
				for i in z['data']:
					com.append(i['id'])
					Excute2(i['id'],i['message'],tipe)
				
				if len(com) == 0:
					print(W + '[' + R + '!' + W + '] ' + R + 'no comment found!')
					sys.exit()
				
				print(W + '\n[' + G + '•' + W + '] done!')
				
			except ValueError:
				print(W + '[' + R + '!' + W + '] ' + R + 'enter the numbers!')
				sys.exit()
						
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
	
def Type(pil):
	print(W + '\n[-------- ' + G + 'TYPE REACTIONS' + W + ' --------]\n')
	print(G + '    01' + W + '. Like    ' + G +'   02' + W + '. Love')
	print(G + '    03' + W + '. Wow     ' + G +'   04' + W + '. Sad')
	print(G + '    05' + W + '. Angry     ' + G +' 06' + W + '. HaHa')
	
	cek = input(W + '\n[ ' + R + 'Dz' + W +' ]•> ' + G)
	if cek in ['1','01']:
		tipe = 'LIKE'
		Get(tipe,pil)
	elif cek in ['2','02']:
		tipe = 'LOVE'
		Get(tipe,pil)
	elif cek in ['3','03']:
		tipe = 'WOW'
		Get(tipe,pil)
	elif cek in ['4','04']:
		tipe = 'SAD'
		Get(tipe,pil)
	elif cek in ['5','05']:
		tipe = 'ANGRY'
		Get(tipe,pil)
	elif cek in ['6','06']:
		tipe = 'HAHA'
		Get(tipe,pil)
	else:
		exit(W + '[' + R + '!' + W + '] ' + R + 'stuppid!')

try:
	postid = []
	global token, HD
	token = open('log/token').read()
	HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
	
	print(W + '\n  {' + G + '01' + W + '} Reactions Home')
	print(W + '  {' + G + '02' + W + '} Bom Reactions Target')
	print(W + '  {' + G + '03' + W + '} Reactions Comment Target')
	print(W + '  {' + R + '00' + W + '} Back')
	
	cek = input(W + '\n[ ' + R + 'Dz' + W +' ]•> ' + G)
	
	if cek in ['1','01']:
		pil = 'home'
		Type(pil)
	elif cek in ['2','02']:
		pil = 'target'
		Type(pil)
	elif cek in ['3','03']:
		pil = 'comment'
		Type(pil)
	elif cek in ['0','00']:
		os.system('python Fb.py')
	else:
		exit(W + '[' + R + '!' + W + '] ' + R + 'stuppid!')
		
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()