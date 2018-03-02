#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : terminal.py
#purpose : Foundation for terminal commands and possible GUI linkage
#date : 2018.03.01
#version: 1.2.05
#version notes (latest): Compatible w/ python2


import os
import sys
from collections import OrderedDict

#SDR Module Calls
from .sdr_modules.network_operations import netOps
from .sdr_modules.csv_operations import csvOps
from .sdr_modules.database_operations import databaseOps
from .sdr_modules.app_unit_tests import testCases
from .sdr_modules.settings import settingConfigs

#For multiprocessing docs: https://docs.python.org/3/library/multiprocessing.html

##########      System Level Section (SOME PARTS NOT IMPLEMENTED)  ###########

def quitTerminal():
        #Perform a clean exit
        sys.exit()

##########      User Input/Display Section      ############


def printHelp():
        list_commands = """
        ############################################
        ####### SUPERFREQ Terminal Interface #######
        ####### Version: 1.2.05 #####################
        ############################################
        List of program commands:\n
        \t 0. Help - Reprint (this) command prompt \n
        \t 1. Radio Options - Choose different radio frequencies (e.g. wifi) to capture packets that will automatically be saved to a csv file(s) \n
        \t 2. CSV Operations - Choose to read, remove or generate graphs from csv files \n        
        \t 3. Database Operations - Import CSV's into the DB or just view all saved data \n
        \t 4. Automated Test Summary - Provide quick network/system checks in an easy to read format \n
        \t 5. Settings Page - Save user preferences & configurations for network data manipulation \n
        \t (Q)uit - Quits the program \n
        \n
        """
        print list_commands
                

##########      Main Section    #######################
        
def runTerminal():

        #User Loop
        terminal_on = True

        #Available number options to execute commands

        options = OrderedDict((('0', printHelp),
                               ('1', netOps),
                               ('2', csvOps),
                               ('3', databaseOps),
                               ('4', testCases),
                               ('5', settingConfigs),
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
        runTerminal()
