#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : system_module_operations.py
#purpose : Allow all other module files call this for options logic. Do not reference functions from other files in here. This is self-contained
#date : 2018.03.20
#version: 1.0.45
#version notes (latest): Compatible w/ python2

import sys
import os
from functools import partial
from collections import OrderedDict

def getSourceDir():

    """ This function exists to help others call the files from anywhere"""
    
    #Tell the system where we currently are
    cwd = os.getcwd()
    #print cwd
    #Tell the system the root of our app is before 'src'
    separator= 'src/'
    #Remove everything after and including 'src/'
    rootPath = cwd.split(separator, 1)[0]
    #print rootPath
    return rootPath

def runTerminalInfraDir():

    infra_dir = getSourceDir()
    infra_dir += 'src/infrastructure/'
    sys.path.insert(0, infra_dir)
    import terminal
    terminal.runTerminal()
    

def getSelectedDir(directory_list):

    #Set loop variables
    dir_number = 0
    dir_list = []
    dir_loop_on = True

    print("\n\tListing Available Data Directories to Choose From... \n")
    
    #List contents of directory
    for dirs_in_dir in os.listdir(directory_list):
        print "\t\t" + str(dir_number) + ". " + dirs_in_dir
        #Pass in lists (arrays)
        number_and_dir = [str(dir_number), dirs_in_dir]
        dir_list.append(number_and_dir)
        dir_number+=1

    #Turn our list into an Ordered dictionary (hastable)
    dir_list = OrderedDict(dir_list)

    while dir_loop_on:
        try:
            #Get user string
            user_key_input = raw_input('\nEnter a number or (Q) to Quit: ').upper()
            if user_key_input in dir_list:
                folder_to_open = dir_list[user_key_input]
                return folder_to_open
            elif user_key_input == 'Q':
                dir_loop_on = False
                runTerminalInfraDir()
            else:
                print '\n\nUnknown User Input! Try Again!\n'
        except:
            break

def getSelectedFile(directory_list):

    #Set loop variables
    file_number = 0
    file_list = []
    file_loop_on = True

    print("\n\tListing Available Files to Choose From... \n")
    
    #List contents of directory
    for file_in_dir in os.listdir(directory_list):
        print "\t\t" + str(file_number) + ". " + file_in_dir
        number_and_file = [str(file_number), file_in_dir]
        file_list.append(number_and_file)
        file_number+=1

    #Turn our list into an Ordered dictionary (hastable)
    file_list = OrderedDict(file_list)

    while file_loop_on:
        try:
            #Get user string
            user_key_input = raw_input('\nEnter a number or (Q) to Quit: ').upper()
            if user_key_input in file_list:
                file_selected = file_list[user_key_input]
                return file_selected
            elif user_key_input == 'Q':
                file_loop_on = False
            else:
                print '\n\nUnknown User Input! Try Again!\n'
        except:
            break
