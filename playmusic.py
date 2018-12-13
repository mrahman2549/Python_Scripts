#!/usr/bin/python3
import subprocess as sb
import random as rand
import time as t

print("This is cool!")

list=sb.check_output("ls /home/pi/Music/",shell=True).decode('ascii')

print(list)
rang=len(list.splitlines())
print(rang)
y=0
randint=0

while True:
	x=1
	randint=rand.randint(1,rang+1)

	for l in list.splitlines():
		print("Random number %d"%randint)
#		t.sleep(4)
		if x==randint and y!=randint:
			print("Playing %d %s" %(x,l))
			cmd="omxplayer -o local --vol 150 \"/home/pi/Music/"+l+"\""
			sb.call(cmd,shell=True)
			y=randint
		print("Value of Random is %d,Value of x is %d and Value of y is %d"%(randint,x,y))
		x+=1
		print("################")
#		t.sleep(1)
