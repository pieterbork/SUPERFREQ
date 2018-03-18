#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : cp_rm.py
#purpose : Show case on how to copy and remove files using Python native code
#date : 2018.03.17
#version: 1.0.0
#version notes (latest): Compatible w/ python2

import sys
import os
import shutil
import time

#Note shutil.copytree() and shutil.rmtree() copy delete recursively

#Set various paths used for testing
#Tell the system where we currently are
cwd = os.getcwd()
#print cwd
#Tell the system the root of our app is before 'src'
separator= 'src/'

#root path setup
root_path = cwd.split(separator, 1)[0]

src_file = root_path + 'src/UnitTests/Infrastructure_UnitTests/csv_operations/to_copy.csv'
dst = root_path + 'src/UnitTests/Infrastructure_UnitTests/csv_operations/to_remove.csv' 

if not os.path.isfile(src_file):
    print("\n The MCP has derezzed the file!\n")
    sys.exit()
else:
    #copy our file
    shutil.copyfile(src_file, dst)
    #Now delete
    if os.path.isfile(dst):
        #Below value can change
        time.sleep(5)
        os.remove(dst)
        
