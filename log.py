#!/usr/bin/python3

import subprocess as sb
import time as t
import datetime as dt
import os


filename=dt.datetime.now().strftime("%m_%d_%Y")

try:
    os.mkdir("Learning_log")
except:
    print("Learning_log folder already exists!")
while True:
    strnow=dt.datetime.now().strftime("%I:%M %p")
    ask=input("Enter your note that you would like to enter:\n")
    try:
        if(filename not in str(os.listdir("Learning_log"))):
            f=open("Learning_log/"+filename+".txt","a")
            f.write("\n")
            f.write("################################\n")
            f.write("File Name: "+filename+"\n")
            f.write("Created time: "+strnow+"\n")
            f.write("################################\n")
            f.write("\n")
            f.write("\n")
            f.close()
            
        f=open("Learning_log/"+filename+".txt","a")
        f.write(strnow+": "+ask)
        f.write("\n")
        f.write("\n")
        f.close()

    except:
        print("File exists!")


