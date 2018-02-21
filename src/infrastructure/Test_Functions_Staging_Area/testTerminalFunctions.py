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
#date : 2018.02.20
#version : 1.0.0
#version notes (latest): Compatible w/ python2.
import os
import subprocess
import shlex
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

dir = os.path.dirname(__file__)
print (dir)

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
