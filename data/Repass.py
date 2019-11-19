#!usr/bin/python3.7
#Author: DulLah ©2019
# FB : fb.me/dulahz
#Telegram : t.me/unikers
#github: github.com/dz-id

import os, sys, requests, mechanize

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

def Change(newpass,user):
	try:
		br.open('https://mbasic.facebook.com/settings/security/password/')
		br._factory.is_html = True
		br.select_form(nr=1)
		br.form['password_old'] = user.split('|')[1]
		br.form['password_new'] = newpass
		br.form['password_confirm'] = newpass
		sub=br.submit().read()
		if 'Kata Sandi Telah Diubah' in str(sub) or 'Password Changed' in str(sub):
			print(W + '[' + G + '+' + W + '] ' + G + 'success',user.split('|')[0]+'|'+str(newpass))
			open('result/newpass.txt','a').write(user.split('|')[0]+'|'+str(newpass)+'\n')
			print(W + '-'*45)
		else:
			print(W + '[' + R + '+' + W + '] ' + R + 'failed when change password',user.split('|')[1])
			print(W + '-'*45)
	except:
		print(W + '[' + R + '+' + W + '] ' + R + 'failed when change password',user.split('|')[1])
		print(W + '-'*45)
		
def Login(newpass,user):
	try:
		global br
		print(W +'[' + G + '*' + W + '] trying login',user)
		br = mechanize.Browser()
		br.set_handle_equiv(True)
		br.set_handle_gzip(True)
		br.set_handle_redirect(True)
		br.set_handle_referer(True)
		br.set_handle_robots(False)
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 8.0.0; TA-1053 Build/OPR1.170623.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3368.0 Mobile Safari/537.36')]
		br.open('https://mbasic.facebook.com/login')
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = user.split('|')[0]
		br.form['pass'] = user.split('|')[1]
		sub = br.submit().read()
		if 'save-device' in str(sub) or 'mbasic_logout_button' in str(sub):
			Change(newpass,user)
		elif 'checkpoint' in str(sub):
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
	print(W + '\n[' + R + '!' + W + '] sparator email|password')
	file = input(W + '[' + G + '?' + W + '] account list : ' + G)
	for ids in open(file).readlines():
		id.append(ids.strip())
		
except FileNotFoundError:
	exit(W + '[' + R + '!' + W + '] ' + R + 'file not found!')
	
print(W + '[' + R + '!' + W + '] password must be 6 characters or more!')
newpass = input(W + '[' + G + '?' + W + '] new password : ' + G)
print('')
print(W + '-'*45)
for akun in id:
	Login(newpass,akun)
print(W + '\n[' + G + '*' + W + '] done!')
exit(W + '[' + G + '#' + W + '] file saved : ' + G + 'result/newpass.txt')