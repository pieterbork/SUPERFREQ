#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : terminal.py
#purpose : Foundation for terminal commands and possible GUI linkage
#date : 2018.02.03
#version: 1.0.2
#version notes (latest): Compatible w/ python2


import os
import sys
import terminalFunctions
#from multiprocessing import Process

#For multiprocessing docs: https://docs.python.org/3/library/multiprocessing.html

##########      System Level Section (SOME PARTS NOT IMPLEMENTED)  ###########


def CheckInputFile():
        #Check that the file exists. If so open the file and check for longest length
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
        

##########      User Input/Display Section      ############

def getUserInput():
        #Get user string
        try:
                user_key_input = raw_input('Enter number or (Q) to Quit: ').lower()
                return user_key_input
        except:
                print("Sorry, input could not be parsed.")


def printHelp():
        print("############################################")
        print("####### SUPERFREQ Terminal Interface #######\n############################################")
        print("####### Version: 1.0.5 #####################\n############################################\n")
        print("List of program commands:\n")
        print("\t 0. Help - Reprint (this) command prompt \n")
        print("\t 1. Tune Radio - Ensure our antenna is RX Data \n")
        print("\t 2. Display Network Data - Interactive Graphs & Statistics \n")
        print("\t 3. Decode Network Data - Scan, capture, parse various network protocols \n")
        print("\t 4. View Database - View saved network data  \n")
        print("\t 5. Test Summary - Provide quick network/system checks in an easy to read format \n")
        print("\t 6. Settings Page - Save user preferences & configurations for network data manipulation \n")
        print("\t (Q)uit - Quits the program \n")
        print("\n")
                

##########      Main Section    #######################
        
def runTerminalMain():

        #Mandatory First print out of commands
        printHelp()

        #User Loop
        terminal_on = True

        #Main Program Loop
        while terminal_on:
                user_input = getUserInput()

                #User Choice Handle Cases..may want to use dictionary later
                if(user_input == '0'):
                        printHelp()
                elif(user_input == '1'):
                        terminalFunctions.tuneRadio()
                elif(user_input == '2'):
                        terminalFunctions.displayNetworkData()
                elif(user_input == '3'):
                        terminalFunctions.decodeNetworkData()
                elif(user_input == '4'):
                        terminalFunctions.viewDatabase()
                elif(user_input == '5'):
                        terminalFunctions.testSummary()
                elif(user_input == '6'):
                        terminalFunctions.settingsPage()
                elif(user_input == 'q' or user_input == 'quit'):
                        print("Goodbye!\n")
                        #Perform a clean exit
                        sys.exit()
                else:
                        continue
##

if __name__ == "__main__":
        runTerminalMain()
        """
        p = Process(target=runTerminalMain)
        p.start()
        p.join()
        """
