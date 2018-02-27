#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : terminal.py
#purpose : Foundation for terminal commands and possible GUI linkage
#date : 2018.02.25
#version: 1.1.03
#version notes (latest): Compatible w/ python2


import os
import sys
import terminalFunctions
#from multiprocessing import Process
from collections import OrderedDict

#For multiprocessing docs: https://docs.python.org/3/library/multiprocessing.html

##########      System Level Section (SOME PARTS NOT IMPLEMENTED)  ###########

def quitTerminal():
        #Perform a clean exit
        sys.exit()

##########      User Input/Display Section      ############


def printHelp():
        list_commands = """
        ############################################
        ####### SUPERFREQ Terminal Interface ###################################################
        ####### Version: 1.1.0 #################################################################
        ############################################
        List of program commands:\n
        \t 0. Help - Reprint (this) command prompt \n
        \t 1. Scan Network - Ensure our antenna can RX (receive) Data \n
        \t 2. Display Network Data - Interactive Graphs & Statistics \n        
        \t 3. View Database - View saved network data  \n
        \t 4. Test Summary - Provide quick network/system checks in an easy to read format \n
        \t 5. Settings Page - Save user preferences & configurations for network data manipulation \n
        \t (Q)uit - Quits the program \n
        \n
        """
        print list_commands
                

##########      Main Section    #######################
        
def runTerminalMain():

        #User Loop
        terminal_on = True

        #Available number options to execute commands

        options = OrderedDict((('0', printHelp),
                               ('1', terminalFunctions.scanNetwork),
                               ('2', terminalFunctions.displayNetworkData),
                               ('3', terminalFunctions.viewDatabase),
                               ('4', terminalFunctions.testSummary),
                               ('5', terminalFunctions.settingsPage),
                               ('Q', quitTerminal)))
                               

        #Mandatory First print out of commands
        printHelp()

        #Main Program Loop
        while terminal_on:
                try:
                        #Get user string
                        user_key_input = raw_input('Enter number or (Q) to Quit: ').upper()
                        if user_key_input in options:
                                action = options[user_key_input]
                                action()
                        else:
                                print 'Unknown User Input! Try Again!'
                except:
                        sys.exit()

                        
##

if __name__ == "__main__":
        runTerminalMain()
        """
        p = Process(target=runTerminalMain)
        p.start()
        p.join()
        """
