#!usr/bin/python3.7
#Author: DulLah ©2019
# FB : fb.me/dulahz
#Telegram : t.me/unikers
#github: github.com/dz-id
import sys, time

if sys.platform in ['linux','linux2']:
	W = '\033[0m'
	G = '\033[1;92m'
	R = '\033[1;91m'
else:
	W = ''
	G = ''
	R = ''

def lunga(s):
	for x in s + '\n':
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(0.03)

lunga('\n-------------------------------------------------------\n')
lunga(W + '     ABOUT              ' + G + 'FACEBOOK TOOLSKIT')
lunga(W + '     CREATOR            ' + G +'DULLAH')
lunga(W + '     VERSION            ' + G + '2.0')
lunga(W + '     GITHUB             ' + G + 'GITHUB.COM/DZ-ID')
lunga(W + '     FACEBOOK           ' + G + 'FB.ME/DULAHZ')
lunga(W + '     TELEGRAM           ' + G + 'T.ME/UNIKERS')
lunga(W + '     REGION             ' + G + 'INDONESIA')
lunga(R + '\nIf you find any error or problems, please contact author' + W)