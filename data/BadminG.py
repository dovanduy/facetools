#!usr/bin/python3.7
#Author: DulLah ©2019
# FB : fb.me/dulahz
#Telegram : t.me/unikers
#github: github.com/dz-id

import sys, requests, re, time
from data import cekKuki
from bs4 import BeautifulSoup as parser
from http.cookiejar import LWPCookieJar as kuki

global W, G, R
if sys.platform in ['linux','linux2']:
	W = '\033[0m'
	G = '\033[1;92m'
	R = '\033[1;91m'
else:
	W = ''
	G = ''
	R = ''

class Block:
	def __init__(self):
		cekKuki.cek(self)
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.token = open('log/token').read()
		self.url = 'https://mbasic.facebook.com{}'
		self.req = requests.Session()
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.id = input(W + '\n[' + G + '?' + W + '] enter group id : '+G)
		self.Main()
	
	def Main(self):
		try:
			id = []
			print(W + '[' + G + '*' + W + '] GET all admin id... ')
			aa = self.req.get(self.url.format('/browse/group/members/?id='+str(self.id)+'&start=0&listType=list_admin_moderator'),headers = self.HD)
			bb = parser(aa.content, 'html.parser')
			for i in bb.find_all('h3'):
				p = i.find('a')
				if 'None' in str(p):
					continue
				else:
					if 'profile.php' in p['href']:
						ids = re.findall(r'/?id=(.*?)&fref=',p['href'])[0]
					else:
						ids = re.findall(r'/(.*?)?fref',p['href'])[0]
					id.append(ids.replace('?',''))
			print(W + '[' + G + '*' + W + '] ' +str(len(id))+ ' admin found.')
			time.sleep(2)
			print('')
			for user in id:
				self.Continue(user)
		except requests.exceptions.ConnectionError:
			print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()
		except KeyError:
			print(W + '[' + R + '!' + W + '] ' + R + 'error!')
			print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
			sys.exit()

	def Continue(self,user):
		data = []
		user = requests.get('https://graph.facebook.com/'+str(user)+'?access_token='+str(self.token),headers = self.HD)
		user = user.json()
		name = user['name']
		user = user['id']
		rr = self.req.get(self.url.format('/privacy/touch/block/confirm/?bid=' + str(user)),headers = self.HD)
		bs = parser(rr.content,'html.parser')
		for x in bs('form'):
			if '/privacy/touch/block/id/?' in x['action']:
				data.append(x['action'])
				break
		for x in bs('input'):
			try:
				if 'fb_dtsg' in x['name']:
					data.append(x['value'])
				if 'jazoest' in x['name']:
					data.append(x['value'])
					break
			except: pass
		if len(data) == 3:
			url = self.url.format(data[0])
			form = {'fb_dtsg' : data[1], 'jazoest' : data[2], 'confirmed' : 'Blokir'}
			b = self.req.post(url, data = form, headers = self.HD)
			if b.status_code == 200:
				print(W + '[' + G + '-' + W + '] bloked - '+str(name)+' - ' + '('+str(user)+')')
			else:
				print(W + '[' + R + '×' + W + '] failed - '+str(name)+' - ' + '('+str(user)+')')
		else:
			print(W + '[' + R + '×' + W + '] Failed - '+str(name)+' - ' + '('+str(user)+')')
		
try:
	Block()
	print(W + '\n[' + G + '•' + W + '] done!')
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()