#!usr/bin/python3.7
# coding: utf-8

# Facebook Toolskit Version 2.0
# Copyright: (©) 2019  DulLah
# Hargailah Sejelek Apapun Itu:V

import os, sys, time, requests, mechanize, hashlib, json, shutil
from data import Clr
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import Style
from http.cookiejar import LWPCookieJar as kuki

headers = open('UserAgent/ua.txt').read()
br = mechanize.Browser()
cj = kuki('log/kuki')
br.set_cookiejar(cj)
br.set_handle_gzip(True)
br.set_handle_redirect(True) 
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', headers),('Referer', 'https://mbasic.facebook.com/'),('Connection', 'keep-alive')]
up = '2.1'

if sys.platform in ['linux','linux2']:
	C = '\033[1;96m'
	W = '\033[0m'
	G = '\033[1;92m'
	R = '\033[1;91m'
	Y = '\033[1;93m'
else:
	C = ''
	W = ''
	G = ''
	R = ''
	Y = ''

try:
	shutil.rmtree('__pycache__')
except: pass
try:
	shutil.rmtree('data/__pycache__')
except: pass
	
def banner():
	print(G +'''
   ____           ______          __  
  / __/__ _______/_  __/__  ___  / /__ '''+ W + '''Made By DulLah''' + G + '''
 / _// _ `/ __/ -_) / / _ \/ _ \/ (_-<''' + W + ''' Github.com/dz-id ''' + G + '''
/_/  \_,_/\__/\__/_/  \___/\___/_/___/''' + W + ''' Copyright 2019''')

def Log():
	e = ''
	er = 0
	ere = 0
	erer = 50
	for _ in range(erer):
		er +=1
		sys.stdout.write('\r' + W + '[' + G + '•' + W + '] ' +e+ ' {:.0f}% '.format(er/erer*100));sys.stdout.flush();time.sleep(0.05)
		e +='#'
		ere +=1
		if ere == 10:
			e = ''
			ere = 0

def update():
	try:
		req = requests.get('https://raw.githubusercontent.com/dz-id/facebook-toolskit/master/version.txt').text
		if req == str(up):
			y = input(W + '\n[' + G + '*' + W + '] backup folder like: result? [y/n] : '+G)
			if y.lower() == 'y':
				try:
					os.mkdir('../facetools-backupdir')
				except: pass
				if os.path.exists('result'):
					print(W + '[' + G + '*' + W + '] moving result folder...')
					os.system('mv result ../facetools-backupdir')
				else:
					print(W + '[' + G + '*' + W + '] no directory found')
				print(W + '[' + G + '*' + W + '] updating...\n')
				if os.name in ['nt','win32']:
					os.system('cd .. & rd /s/q facetools')
					os.system('cd .. & git clone https://github.com/dz-id/facetools')
				else:
					os.system('cd ..;rm -rf facetools')
					os.system('cd ..;git clone https://github.com/dz-id/facetools')
		else:
			print(W + '\n[' + G + '*' + W + '] already up to date.')
	except requests.exceptions.ConnectionError:
		print(W + '\n[' + R + '!' + W + '] ' + R + 'check your connections!')
		sys.exit()
		
try:
	HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
	token = open('log/token').read()
except IOError:
		try:
			Clr.Clr()
			banner()
			try:
				os.mkdir('log')
			except: pass
			print(W + '\n[' + R + '!' + W + ']' + C + ' before using this tools please login via chrome to avoid checkpoints!\n')
			print(W + '[' + G + '#' + W + '] LOGIN FACEBOOK ACCOUNT ' + W + '[' + G + '#' + W + ']')
			style = Style.from_dict({'': '#00FF00','1': '#FFFFFF','2': '#00FF00','3': '#FFFFFF','4': '#FFFFFF'})
			msg = [('class:1', '['),('class:2', '•'),('class:3', ']'),('class:4', ' Password : ')]
			id = input(W + '['+ G + '•' + W +'] Username : ' + G);pw = prompt(msg,style=style,is_password=True);Log()
			br.open('https://mbasic.facebook.com/login.php')
			br._factory.is_html = True
			br.select_form(nr = 0)
			br.form['email'] = id
			br.form['pass'] = pw
			sub = br.submit().read()
			if 'save-device' in str(sub) or 'logout.php' in str(sub):
				try:
					cj.save();sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pw+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pw,"return_ssl_resources":"0","v":"1.0"};x = hashlib.new("md5");x.update(sig.encode("utf-8"));data.update({'sig':x.hexdigest()})
					js = requests.get("https://api.facebook.com/restserver.php",params=data,headers=HD)
					r = json.loads(js.text)
					e = open('log/token','w')
					e.write(r['access_token'])
					e.close()
					import data.ChangeL #//
					for anu in ['Login successfully','                  ','Login successfully','                  ','Login successfully','                  ','Login successfully','                  ','Login successfully','                  ','Login successfully']:
						sys.stdout.write('\r' + W + '[' + G + '•' + W + '] ' + anu);sys.stdout.flush();time.sleep(0.3)
				except KeyError:
					print(W + '\r[' + R + '!' + W + '] ' + R + 'Failed when generate access token!')
					exit()
			elif 'checkpoint' in str(sub):
				print(W + '\r[' + Y + '!' + W + '] ' + Y + 'Login failed, checkpoint!')
				print(W + '[' + Y + '!' + W + '] ' + Y + 'Please verify your account in the browser and try again!')
				exit()
			else:
				print(W + '\r[' + R + '!' + W + '] ' + R + 'Login failed!              ')
				print(W + '[' + R + '!' + W + '] ' + R + 'Check your username or password!')
				exit()
		except (requests.exceptions.ConnectionError,mechanize.URLError):
			print(W + '\r[' + R + '!' + W + '] ' + R + 'Login failed!              ')
			print(W + '[' + R + '!' + W + '] ' + R + 'Check your connections!')
			exit()
			
try:
	Clr.Clr()
	banner()
	token = open('log/token').read()
	z = requests.get('https://graph.facebook.com/me?access_token=' + token, headers = HD)
	ver = requests.get('https://raw.githubusercontent.com/dz-id/facebook-toolskit/master/version.txt').text
	s = json.loads(z.text)
	name = s['name']
	try:
		userid = s['username']
	except: userid = s['id']
	if up == str(ver):
		print(Y + ' available new version',str(up))
	print(W + "\n  {" + G + "+" + W + "} version 2.0")
	print(W + "  {" + G + "+" + W + "} type 'rm' for remove access token")
	print(W + '  {' + G + '+' + W + '} Active User : ' + G + name + W + ' (' + G + userid + W + ')')
	print(W + '\n  {' + G + '01' + W + '} Multi Brute Force')
	print(W + '  {' + G + '02' + W + '} Dump Id/Email/Phone Numbers')
	print(W + '  {' + G + '03' + W + '} Yahoo Email Cloner')
	print(W + '  {' + G + '04' + W + '} Friends Information')
	print(W + '  {' + G + '05' + W + '} Delete All Messages')
	print(W + '  {' + G + '06' + W + '} Delete Posts')
	print(W + '  {' + G + '07' + W + '} Delete Albums')
	print(W + '  {' + G + '08' + W + '} Delete All Photo Albums')
	print(W + '  {' + G + '09' + W + '} Accept Or Reject Friends Requests')
	print(W + '  {' + G + '10' + W + '} Mass Unfriends')
	print(W + '  {' + G + '11' + W + '} Mass Block Friends')
	print(W + '  {' + G + '12' + W + '} Unblock')
	print(W + '  {' + G + '13' + W + '} Leave Groups')
	print(W + '  {' + G + '14' + W + '} Stop Following All Friends')
	print(W + '  {' + G + '15' + W + '} Untag Posts')
	print(W + '  {' + G + '16' + W + '} Hide Posts')
	print(W + '  {' + G + '17' + W + '} Auto Pokes')
	print(W + '  {' + G + '18' + W + '} Auto Reactions')
	print(W + '  {' + G + '19' + W + '} Auto Comments')
	print(W + '  {' + G + '20' + W + '} Auto Chat')
	print(W + '  {' + G + '21' + W + '} Auto Posting Status')
	print(W + '  {' + G + '22' + W + '} Auto Add Friends')
	print(W + '  {' + G + '23' + W + '} Auto Reporting')
	print(W + '  {' + G + '24' + W + '} Auto Riset Password')
	print(W + '  {' + G + '25' + W + '} Auto Invite Friends To Join Groups')
	print(W + '  {' + G + '26' + W + '} Auto Invite Friends To Like Your Page')
	print(W + '  {' + G + '27' + W + '} Auto Follow By Account Lists')
	print(W + '  {' + G + '28' + W + '} Photos Messages Downloader')
	print(W + '  {' + G + '29' + W + '} Photos Albums Downloader')
	print(W + '  {' + G + '30' + W + '} Checkpoints Detector')
	print(W + '  {' + G + '31' + W + '} FB Video Downloader')
	print(W + '  {' + G + '32' + W + '} Auto Join Groups With Search Name')
	print(W + '  {' + G + '33' + W + '} Groups Public Detector By Search Name')
	print(W + '  {' + G + '34' + W + '} Groups Lists')
	print(W + '  {' + G + '35' + W + '} Check Bind Apps')
	print(W + '  {' + G + '36' + W + '} Block All Admin Groups')
	print(W + '  {' + G + '37' + W + '} Cancel Requests Sent.')
	print(W + '  {' + G + '38' + W + '} Profile Picture Guard')
	print(W + '  {' + G + '39' + W + '} FB Overload Account')
	print(W + '  {' + G + '40' + W + '} Unlike Page')
	print(W + '  {' + G + '41' + W + '} Change Your Passsword')
	print(W + '  {' + G + '42' + W + '} Change Your Bio')
	print(W + '  {' + G + '43' + W + '} Edit Profile Picture')
	print(W + '  {' + G + '44' + W + '} Edit Cover Photo')
	print(W + '  {' + G + '45' + W + '} Check Update')
	print(W + '  {' + G + '46' + W + '} About')
	
	cek = input(W + '\n[ ' + R + 'Dz' + W +' ]•> ' + G)
	if cek in ['1','01']:
		import data.bruteForce
		sys.exit()
	elif cek in ['2','02']:
		import data.dumpID
		sys.exit()
	elif cek in ['3','03']:
		import data.yahooCloner
		sys.exit()
	elif cek in ['4','04']:
		import data.friendsInfo
		sys.exit()
	elif cek in ['5','05']:
		import data.delMsg
		sys.exit()
	elif cek in ['6','06']:
		import data.delPosts
		sys.exit()
	elif cek in ['7','07']:
		import data.delAlbums
		sys.exit()
	elif cek in ['8','08']:
		import data.delPhoto
		sys.exit()
	elif cek in ['9','09']:
		import data.friendsReq
		sys.exit()
	elif cek in ['10']:
		import data.Unfriends
		sys.exit()
	elif cek in ['11']:
		import data.blockFriends
		sys.exit()
	elif cek in ['12']:
		import data.Unblock
		sys.exit()
	elif cek in ['13']:
		import data.Lgroups
		sys.exit()
	elif cek in ['14']:
		import data.Unfollow
		sys.exit()
	elif cek in ['15']:
		import data.Untag
		sys.exit()
	elif cek in ['16']:
		import data.Hide
		sys.exit()
	elif cek in ['17']:
		import data.Pokes
		sys.exit()
	elif cek in ['18']:
		import data.Reactions
		sys.exit()
	elif cek in ['19']:
		import data.Comment
		sys.exit()
	elif cek in ['20']:
		import data.Chat
		sys.exit()
	elif cek in ['21']:
		import data.Posting
		sys.exit()
	elif cek in ['22']:
		import data.Add
		sys.exit()
	elif cek in ['23']:
		import data.Report
	elif cek in ['24']:
		import data.Repass
		sys.exit()
	elif cek in ['25']:
		import data.IFriendsGroups
		sys.exit()
	elif cek in ['26']:
		import data.IFriendsPage
		sys.exit()
	elif cek in ['27']:
		import data.Follow
		sys.exit()
	elif cek in ['28']:
		import data.GPhotoMess
		sys.exit()
	elif cek in ['29']:
		import data.GPhotoAlbum
		sys.exit()
	elif cek in ['30']:
		import data.CheckpointDetector
		sys.exit()
	elif cek in ['31']:
		import data.FbVidDown
		sys.exit()
	elif cek in ['32']:
		import data.JoinGroup
		sys.exit()
	elif cek in ['33']:
		import data.GPDetec
		sys.exit()
	elif cek in ['34']:
		import data.GroupsList
		sys.exit()
	elif cek in ['35']:
		import data.CekApp
		sys.exit()
	elif cek in ['36']:
		import data.BadminG
		sys.exit()
	elif cek in ['37']:
		import data.UnAdd
		sys.exit()
	elif cek in ['38']:
		import data.PGuard
		sys.exit()
	elif cek in ['39']:
		import data.Overload
		sys.exit()
	elif cek in ['40']:
		import data.UnPage
		sys.exit()
	elif cek in ['41']:
		import data.ChangePw
		sys.exit()
	elif cek in ['42']:
		import data.ChangeBio
		sys.exit()
	elif cek in ['43']:
		import data.EditProfilePict
		sys.exit()
	elif cek in ['44']:
		import data.EditCoverPict
		sys.exit()
	elif cek in ['45']:
		update()
		sys.exit()
	elif cek in ['46']:
		Clr.Clr()
		banner()
		import data.About
		sys.exit()
	elif cek in ['rm']:
		y = input(W + '\n[' + G + '?'+ W + '] are you sure to remove access token? [y/n] : '+G)
		if y.lower() == 'y':
			os.remove('log/token')
			print(W + '[' + G + '*' + W + '] success removed.')
			sys.exit()
		else:
			print(W + '[' + G + '*' + W + '] canceling.')
			sys.exit()
	else:
		exit(W + '[' + R + '!' + W + '] ' + R + 'stuppid!')
except KeyError:
	print(W + '\n[' + R + '!' + W + '] Your access token is invalids. please login again!')
	input(W + '[' + R + '!' + W + '] Press ' + G + 'ENTER ' + W + 'to login ')
	os.remove('log/token')
	os.system('python Fb.py')
except requests.exceptions.ConnectionError:
	print(W + '\n[' + R + '!' + W + '] ' + R + 'Check your connections!')
	sys.exit()
except KeyboardInterrupt:
	sys.exit()