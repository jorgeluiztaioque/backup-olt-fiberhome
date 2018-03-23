#!/usr/bin/python
#-------------------------------------
#by Jorge Luiz Taioque
#jorgeluiztaioque at gmail dot com
#www.networktips.com.br
#-------------------------------------
#backup OLTs and ONUs fiberhome
#Usage 
#./bk-olt-fiberhome.py IP_ADDRESS


import sys,pexpect
import getpass
import time
import arrow

HOST = sys.argv[1]

#configure here all variables following you system 
#=======================================================================
user = 'GEPON'
password = 'GEPON'
FTPSERVER = '200.200.200.200'
ftpuser = 'user'
ftppassword = '123456'
ftpdirectory = '/backups'
#=======================================================================


child = pexpect.spawn ('telnet '+HOST) #option needs to be a list
child.timeout = 150
child.logfile = sys.stdout #display progress on screen

#logging in OLT IP
time.sleep(2)
child.expect ('Login: ') #waiting for login
child.sendline (user) #sending login name
child.expect('Password:') #waiting for password
child.sendline (password) #sending password
child.expect('>')

time.sleep(3)

#go up enable configuration
child.sendline ('EN'+'\r') #going to ENABLE configuration
child.expect('Password:') #waiting enable password
child.sendline (password) #sending enable password 
time.sleep(3)
child.expect('#')


#defining the actual date to be add to the filename
mydate = arrow.now().format('YYYY-MM-DD')


#sending commando to copy configuration file to remote FTP server
child.sendline ('upload ftp config '+FTPSERVER+' '+ftpuser+' '+ftppassword+' '+ftpdirectory+'/bk-olt-'+HOST+'-'+mydate+'.cfg')
time.sleep(10)

#exiting connection
child.expect('#')
child.sendline ('exit \r')
child.sendline ('exit \r')
