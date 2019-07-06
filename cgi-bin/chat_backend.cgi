#!/usr/bin/python2

import cgi,cgitb,os,time,subprocess,commands,socket

cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
ip_add=web.getvalue('ip')
person=web.getvalue('person')
port=6001


	print os.system(s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM))

if(person=="receiver")

	print os.system(s.bind((ip_add,port))  )

	while  True:
		print os.system(rec_data=s.recvfrom(100) ) 
		print os.system(print   "data rec from  client :   ",rec_data[0] )
    	print os.system(rply=raw_input("enter your rply  :   ") )
		print os.system(s.sendto(rply,rec_data[1]) )

