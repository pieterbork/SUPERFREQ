#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : testTerminalFunctions.py
#purpose :
"""
Stage Functions for testing before implementing into terminalFunctions.py.
All functions which are successfully working here can be integrated into the "main flow"
Comment out sections that are no longer needing to be tested.
Clean this file after all terminal functions are done.
"""
#date : 2018.02.26
#version : 1.0.0
#version notes (latest): Compatible w/ python2.
import os
#import pkg_resources
#import subprocess
#import shlex
#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib import cm
#from functools import partial
from collections import OrderedDict

#print pkg_resources.resource_filename('src.infrastructure', 'terminal.py')

fileNumber = 0

file_list = []

#List contents of directory
for file_in_dir in os.listdir("."):
    print str(fileNumber) + ". " + file_in_dir
    #myOrderedDictionary = OrderDict((fileNumber,file_in_dir) for file_in_dir in files)
    #print myOrderedDictionary
    numberAndFile = {str(fileNumber): file_in_dir}
    file_list.append(numberAndFile)
    fileNumber+=1
    #Get user input...

print file_list

"""

#Tell the system where we currently are
cwd = os.getcwd()
print cwd
#Tell the system the root of our app is before 'src'
separator= 'src/'
#Remove everything after and including 'src/'
rootPath = cwd.split(separator, 1)[0]
print rootPath
#Add path to file we wish to execute
rootPath += 'src/infrastructure/'
print rootPath
os.chdir(rootPath)
print os.getcwd()

"""

"""
dir = os.path.dirname(__file__)
print (dir)
"""

"""
#Ping Common (8.8.8.8; Google) Network address
#Can be automated or we pass in user input
try:
    subprocess.call(["ping", '-c', '5', '8.8.8.8'])
    #If successful test is marked successful
    print("Internet Connection Established!")
except:
    #Mark test a failure
    print("FAILED to establish an Internet Connection!")

#Ping the first Bluetooth device detected
try:
    #Need to fix this function
    #User input in dotted hex notation. Need to check user input
    hexVar = '01:02:03:ab:cd:ef'
    blueArgs=shlex.split('l2ping -c 5 {}'.format(hexVar))
    subprocess.call(blueArgs)
    print("Connected to {}".format(hexVar))
except:
    #Mark test a failure
    print("FAILED to connect to {}".format(hexVar))

"""
