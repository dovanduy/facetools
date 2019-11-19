#!usr/bin/python3.7
#Author: DulLah ©2019
#contact: fb.me/dulahz
#github: github.com/dz-id

try:
	import sys, requests, json
	from multiprocessing.pool import ThreadPool
	
	if sys.platform in ['linux','linux2']:
		W = '\033[0m'
		G = '\033[1;92m'
		R = '\033[1;91m'
	else:
		W = ''
		G = ''
		R = ''
	
	HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
	token = open('log/token').read()
	id = []
except Exception as E:
	print(W + '[' + R + '!' + W + ']' + R + str(E))
try:
	limit = int(input(W + '\n[' + G + '?' + W + '] how many : ' + G))
	print('')
	r = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit(' + str(limit) + ')&access_token=' + token, headers = HD)
	b = json.loads(r.text)
	
	for i in b['home']['data']:
		id = i['id'].split('_')[0]
		p = requests.post('https://graph.facebook.com/' + str(id) + '/pokes?access_token=' + token, headers = HD)
		try:
			error = p.json['error']['message']
			print(W + '[' + R + str(id) + W + '] failed')
		except TypeError:
			print(W + '[' + G + str(id) + W + '] pokes')

except KeyError:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'error when grabbing posts id!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()
except ValueError:
	print(W + '[' + R + '!' + W + '] ' + R + 'enter the numbers!')
	sys.exit()
except requests.exceptions.ConnectionError:
	print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
	sys.exit()
print(W + '\n[' + G + '•' + W + '] done!')