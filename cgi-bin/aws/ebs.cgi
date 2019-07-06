#!/usr/bin/python2

import  cgi,cgitb,os,commands,time,subprocess
cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
os_ami=web.getvalue('ami')
os_sg=web.getvalue('sg')
os_availzone=web.getvalue('availzone')

commands.getoutput('sudo aws ec2 create-security-group --group-name '+os_sg+' --description "Security group" ')

commands.getoutput('sudo aws ec2 run-instances --image-id '+os_ami+'--count 1 --instance-type t2.micro --key-name Annlovesred --security-group '+os_sg' --subnet-id subnet-6e7f829e')

