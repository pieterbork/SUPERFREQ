#!/usr/bin/env python3


#author : Kade Cooper kaco0964@colorado.edu
#name : terminal.py
#purpose : Foundation for terminal commands and possible GUI linkage
#date : 2018.02.02
#version: 1.0.2
#version notes (latest): Optimized for python2/3


import os
import sys
from multiprocessing import Process

#For multiprocessing docs: https://docs.python.org/3/library/multiprocessing.html

#Check that the file exists. If so open the file and check for longest length
def CheckInputFile():
        if not os.path.isfile(sys.argv[1]):
                print("\nThe MCP has derezzed the file!\n")
                sys.exit()
        else:
                print ("\nLongest string is: ")
                Long_string = (max(open(sys.argv[1], 'r'), key=len))
                print (Long_string)
                print ("Number of characters in string is: " + str(len(Long_string)) )
                
                #This is enabled if you want output to a CMD from the command line
                #time.sleep(10)
                

def CheckIfRunnable():
        if len(sys.argv) !=2:
                print("ERROR: Must supply 1 argument \nUsage: " + sys.argv[0] + " [name of file to be checked]")
                sys.exit()
                return sys.argv[1]
        else:
                CheckInputFile()
                

##########      Main Section  #######################
def runTerminalMain():
        print("############################################")
        print("####### SUPERFREQ Terminal Interface #######\n############################################")
        print("####### Version: 1.0.0 #####################\n############################################\n")
        print("List of common commands:\n")
        print("\t Echo - Returns another Echo \n")
        print("\t Quit - Quits the program \n")
        print("\n")
        while True:
                try:
                        #Get user string
                        userKeywordInput = input('Enter keyword: ')
                        if(userKeywordInput == 'Echo'):
                                print("Echo!\n")
                                continue
                        if(userKeywordInput == 'Quit'):
                                print("Goodbye!\n")
                        
                except ValueError:
                        print("Sorry, input could not be parsed.")
                        #Re-ask the user for their input
                        continue
                else:
                        #String successfuly parsed
                        #Ready to break the loop
                        break
##

if __name__ == "__main__":
        runTerminalMain()
        """
        p = Process(target=runTerminalMain)
        p.start()
        p.join()
        """


