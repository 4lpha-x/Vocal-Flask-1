try:
	import requests
except ImportError:
	print('Requests Module Not Found !!')
	imp = input('Do You Want To Install Requests? y/n ')
	if imp=='y' or 'Y':
		import os
		os.system('pip install requests')
		os.system('clear')
		os.system('clear')
		os.system('clear')
		print('Installation Completed!')
		print('Now Checking Flask Module')
try:
	from flask import Flask
	print('Program Starting..... ')
	import os
	import time
	time.sleep(.45)
	os.system('clear')
except ImportError:
	print('Flask Module Not Found ')
	imp = input('Do You Want To Install Flask? y/n ')
	if imp=='y' or 'Y':
		import os
		os.system('pip install flask')
		os.system('clear')
		os.system('clear')
		os.system('clear')
		print('Installation Completed')
	else:
		exit();
#Importing
import time
col = '\033[1;31;40m'
def logo():
	a = '''
┏┓╋┏┓╋╋╋╋╋╋╋╋╋╋┏━━┓╋╋╋┏━┳┓
┃┗┳┛┣━┳━┳━┓┏┳━━┫━┳┫┏━┓┃━┫┣┓
┗┓┃┏┫╋┃━┫╋┗┫┗┳━┫┏┫┗┫╋┗╋━┃━┫
╋┗━┛┗━┻━┻━━┻━┛╋┗┛┗━┻━━┻━┻┻┛'''
	print(a)
	print(col + ':::::::::::::Coded By Rc:::::::::::::')
	print(':::::This Program Is Created For Testing Purposes Dont Use It For Any Illegal Purposes:::::')
time.sleep(1)
os.system('clear')
time.sleep(1)
os.system('clear')
print('\n>>>>>>>>>>>>>>>>Welcome To Vocal-Flask!!!<<<<<<<<<<<<<<<<<')

logo()
print('')

site = input('Enter Website URL Here : ')
try:
	req = requests.get(site)
	src = req.text
	time.sleep(.34)
	print('Getting Websites Source Code')
except:
	print('Url Not Found Or Your Internet Is Not Available')
	exit();
with open('src.html', 'w') as sorc:
	r = sorc.write(src)
time.sleep(.65)
print('Saving Source Code As src.txt')
time.sleep(.23)
print('Moving The File To Template Folder ')
os.system('mv -f src.html templates')
time.sleep(.65)
print('File Moved Successfully!')
time.sleep(.45)
os.system('clear')
logo()
print("")
vol= '\033[3;37;40m'
print('Starting LocalHost At Port 5000')
print(vol + 'Localhost Started At Port Number 5000\nOpen 127.0.0.1/5000 In Your Browser To See Website')
print('\n')
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('src.html')

app.run()
os.system('clear')
logo()
print('')
