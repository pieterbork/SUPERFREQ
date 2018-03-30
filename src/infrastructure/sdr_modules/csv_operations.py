#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : csv_operations.py
#purpose : Allow the user to easily traverse our app structure and have options in relation to csv data. May or may not merge with database file
#date : 2018.03.30
#version: 1.0.30
#version notes (latest): Compatible w/ python2

import sys
import os
import csv
import system_module_operations
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from functools import partial
from collections import OrderedDict


def readCsvFile(file_path):

    if not os.path.isfile(file_path):
        print("\n The MCP has derezzed the file!\n")
        sys.exit()
    else:
        with open(file_path) as csvFile:
            #Use csv parser
            reader = csv.reader(csvFile, delimiter=',')
            for row in reader:
                print(row)


def removeCsvFile(file_path):
    if not os.path.isfile(file_path):
        print("\n The MCP has derezzed the file!\n")
        sys.exit()
    else:
        os.remove(file_path)
        

def createGraphFromCsv(userSelectedCSV):

    #Create lists
    labels=[]
    perc=[]

    #Format of csv: Duration,Frame Control,Subtype,SSID,seq nr,mac 1, mac occurence
    #Color scheme
    a = np.random.random(40)
    cs = cm.Set1(np.arange(40)/40.)

    #Check csv file
    if not os.path.isfile(userSelectedCSV):
        print("\n The MCP has derezzed the file!\n")
        sys.exit()
    else:
        with open(userSelectedCSV) as csvFile:
            #Use csv parser
            reader = csv.reader(csvFile, delimiter=',')
            for row in reader:
                labels.append(row[3]+"-"+row[6])
                perc.append(float(row[7]))
                
        #Add data to plot
        plt.pie(perc, labels=labels, autopct='%1.1f%%', colors=cs, shadow=True, startangle=90)

        #Use for changing font colors
        """   _, _, autotexts = plt.pie(perc, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        for autotext in autotexts:
            autotext.set_color('grey')
        """

        #Rounds plot
        plt.axis('equal')
        plt.title("Frequency of MAC Addresses\n")

        #Create Image
        plt.show()

def displayCsvOptions(userCSV):

    list_commands = """
    ############################################
    ####### CSV FILE OPTIONS ####################
    ############################################\n
    File Selected: %s\n
    Program commands:\n
    \t 0. Read CSV - Output the raw contents of the CSV file \n
    \t 1. Generate Graph - Take the data held within the csv to create a graph. This graph will automatically pop up in a separate window \n
    \t 2. Remove CSV File - Remove the selected file\n
    \t (Q)uit - Quit this screen \n
    """ % (userCSV)

    terminal_commands = """
    ############################################
    ####### SUPERFREQ Terminal Interface #######
    ####### Version: 1.2.15 #####################
    ############################################\n
    List of program commands:\n
    \t 0. Help - Reprint (this) command prompt \n
    \t 1. Scan Options - Choose different radio frequencies (e.g. wifi) to capture packets that will automatically be saved to a csv file(s) \n
    \t 2. CSV Operations - Choose to read, remove or generate graphs from csv files \n        
    \t 3. Database Operations - Import CSV's into the DB or just view all saved data \n
    \t 4. Automated Test Summary - Provide quick network/system checks in an easy to read format \n
    \t 5. Settings Page - Save user preferences & configurations for network data manipulation \n
    \t (Q)uit - Quits the program \n
    \n
    """

    #User Loop
    display_on = True

    #Available number options to execute commands

    options = OrderedDict((('0', partial(readCsvFile, userCSV)),
                           ('1', partial(createGraphFromCsv, userCSV)),
                           ('2', partial(removeCsvFile, userCSV))))
                           

    #Mandatory First print out of commands
    print list_commands

    #Main Program Loop
    while display_on:
            try:
                    #Get user string
                    user_key_input = raw_input('Enter a number or (Q) to Quit: ').upper()
                    if user_key_input in options:
                        action = options[user_key_input]
                        action()
                    elif (user_key_input == 'Q' or user_key_input =='q'):
                        display_on = False
                        print terminal_commands
                    else:
                        print '\nUnknown User Input! Try Again!\n'
            except:
                    break


""" 2. Display Network Data - Interactive Graphs & Statistics """

def csvOperations():

    """ LOCAL VARIABLES FOR DIRECTORY LISTING """
    #"Locate" our data directory from anywhere
    directory_list = system_module_operations.getSourceDir()
    
    #Add path to file we wish to execute
    directory_list += 'src/infrastructure/network_scan_output/'

    """ """
    

    """ LET USER CHOOSE DIRECTORY """
    
    #Call our directory lister
    folder_user_opened = system_module_operations.getSelectedDir(directory_list)
    
    
    #Append folder to full path, so files in the path can be listed
    try:
        directory_list += folder_user_opened
    except:
        return

    """ """


    """ LET USER CHOOSE FILE TO GET ADDITIONAL OPTIONS """
    #Call our file lister
    file_user_chose = system_module_operations.getSelectedFile(directory_list)


    """ DISPLAY OPTIONS ON USER SELECTED FILE """
    try:
        #Add file to full directory path
        directory_list = ''.join((directory_list,'/', file_user_chose))
    except:
        return
    
    #See if user wants to output, create a graph or choose a different directory
    displayCsvOptions(directory_list)

    """ """


if __name__ == "__main__":
    csvOperations()
