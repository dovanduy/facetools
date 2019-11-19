#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

import sys, time, requests, json

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

class DelPosts:
	def __init__(self):
		now = time.strftime('%Y')
		self.token = open('log/token').read()
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		url = 'https://graph.facebook.com/v3.0/me?fields=feed&access_token=' +self.token
		self.intime = input(W + '\n[' + G + '?' + W + '] YEAR : ' + G)
		if self.intime == '':
			self.intime = now
		print('')
		self.Main(url)
		
	def Main(self,url):
		try:
			
			r = requests.get(url,headers = self.HD)
			a = json.loads(r.text)
			
			for result in a['feed']['data']:
				year = str(result['created_time']).split('-')
				
				try:
					if year[0] <= str(self.intime):
						s = requests.delete('https://graph.facebook.com/v3.0/' + str(result['id']) + '?access_token=' + self.token, headers = self.HD).text
						if 'true' in str(s):
							try:
								print(W + '[' + R + year[0] + W + '] ' + G + result['message'][:20].replace('\n','') + R + ' >> ' + W + 'success deleted')
							except KeyError: print(W + '[' + R + year[0] + W + '] ' + G + result['id'] + R + ' >> ' + W + 'success deleted')
						else:
							try:
								print(W + '[' + R + year[0] + W + '] ' + G + result['message'][:20].replace('\n','') + R + ' >> ' + W + 'failed')
							except KeyError:print(W + '[' + R + year[0] + W + '] ' + G + result['id'] + R + ' >> ' + W + 'failed')
				except: pass
				
			try:
				self.Main(a['feed']['paging']['next'])
			except:
				try:
					self.Main(a['paging']['next'])
				except: pass
			
		except: pass
try:
	DelPosts()
	exit(W + '\n[' + G + '•' + W + '] done!')
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()