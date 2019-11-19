#!usr/bin/python3.7
#Author: DulLah ©2019

import requests, sys
from http.cookiejar import LWPCookieJar as kuki

def cek(self):
	with requests.Session() as s:
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		try:
			
			aa = s.get('https://mbasic.facebook.com/me', headers = {'User-Agent' : open('UserAgent/ua.txt').read()}).text
			if 'mbasic_logout_button' in str(aa):
				pass
			else:
				print('\033[0m[\033[1;91mwarning\033[0m] \033[1;91mcookies invalids!')
				sys.exit()
				
		except requests.exceptions.ConnectionError:
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()