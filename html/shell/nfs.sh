#!/usr/bin/python2
import commands
commands.getoutput("mkdir /mnt/st2")
commands.getoutput("mount 192.168.43.14:/share_info/st2 /mnt/st2")
commands.getoutput("chmod 777 /mnt/st2")
commands.getoutput("mkdir /mnt/st2/newdir")
