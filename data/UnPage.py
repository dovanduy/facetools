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
	print(W + '\n[' + G + '*' + W + '] Get user id... ')
	r = requests.get('https://graph.facebook.com/me/likes?access_token=' + token,headers = HD)
	a = json.loads(r.text)
	
	print('')
	for i in a['data']:
		id.append(i['id'])
		b = requests.delete('https://graph.facebook.com/' + str(i['id']) + '/likes?access_token=' + token,headers = HD)
		try:
			error = b.json()['error']['message']
			print(W + '[' + R + '×' + W + '] ' + R + str(i['name']) + W + ' (' + str(i['id']) + ') - failed.')
		except TypeError:
			print(W + '[' + G + '-' + W + '] ' + G + str(i['name']) + W + ' (' + str(i['id']) + ') - unliked.')
	if len(id) == 0:
		print(W + '[' + R + '!' + W + '] ' + R + 'there are no likes !')
	else:
		print(W + '\n[' + G + '•' + W + '] done!')

except KeyError:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'error!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()
except requests.exceptions.ConnectionError:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()
except KeyboardInterrupt:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Key interrupt!')
	print(W + '[' + R + '!' + W + '] ' + R + 'stopped!')
	sys.exit()