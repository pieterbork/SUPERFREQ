#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : terminalFunctions.py
#purpose : File for all teammember to put in modular code. As the file grows we can separate the longer functions into separate files
#date : 2018.02.26
#version: 1.0.15
#version notes (latest): Compatible w/ python2

#Native Python Modules
import os
import sys
import time
#import thread
import subprocess
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from multiprocessing import Process
from functools import partial


#This will alert the end tester that the build environment for the hackrf is not present
try:
    from sdr_modules.wifi_rx_rftap import tuneWifi
except ImportError:
    print ("The GnuRadio dependencies are not present in this app! Talk to Pieter/Carlos...")


""" 1. Scan Network - Ensure our antenna can RX Data """

def scanNetwork():

    #Emulate Scan Function
    print("\n\t Running Network Scan w/ HackRF... \n")
    print("\n\t If you wish to quit, press Ctrl C or ^C... \n")
    try:
        #Below is the actual function to run the HackRF
        #tuneWifi.main()
        #Replace checkCsvFile with tuneWifi.main
        cli_process = Process(target=cliProgress, args=(101, 20))
        cli_process.start()
        scan_process = Process(target=readCsvFile)
        scan_process.start()
        #Wait until finished
        cli_process.join()
        scan_process.join()
        
        print("\n\t Results saved locally! Can be accessed by Option 2 on the command line... \n")
    except KeyboardInterrupt:
        print("\nscanNetwork: User stopped scan!!! Partial Data saved. Press enter to return to main program.")
    

""" 2. Display Network Data - Interactive Graphs & Statistics """

def displayNetworkData():

    #dir = os.path.dirname(__file__)
    #csvPathToFile = os.path.join(dir, 'network_scan_output', 'hackRFTestOutput.csv')

    """ LOCAL VARIABLE """
    #"Locate" our data directory from anywhere
    directory_List = getSourceDir()
    
    #Add path to file we wish to execute
    directory_List += 'src/infrastructure/network_scan_output/'

    #Set loop variables
    dir_Number = 0
    dir_list = []

    """ """
    
    print("\t Listing Available Data Directories to Choose From... \n")
    
    #List contents of directory
    for dirs_in_dir in os.listdir(directory_List):
        print str(dir_Number) + ". " + dirs_in_dir
        numberAndDir = {str(dir_Number): dirs_in_dir}
        dir_list.append(numberAndDir)
        dir_Number+=1
        print dir_list
        #Get user input...and assign it to selectedDir
        files_in_user_chosen_dir = directory_List += selectedDir

    #Allow user to select from list of files within the chosen directory
    userDesiredCSV = chooseFile(files_in_user_chosen_dir)


    #See if user wants to output, create a graph or choose a different directory
    displayNetworkGraphOptions(userDesiredCSV)
    
       


""" 3. View Database - View saved network data """

def viewDatabase():
    print("\t MySQL \n")

""" 4. Test Summary - Provide quick network/system checks in an easy to read format """

def sdrWifiTests():
    wifi_return_code = subprocess.checkoutput("")
    #If wifi_return_code is true than a wireless service has been turned off
    if (wifi_return_code):
        print("\t Wifi: {} \n".format(passedCheck))
    else:
        passedCheck="On"
        print("\t Wifi: {} \n".format(passedCheck))

def sdrBluetoothTests():
    print("\t BlueTooth: {} \n".format(passedCheck))


def testSummary():

    passedCheck = "Off"
    
    print("SDR Hardware Check: \n")
    sdrWifiTests(passedCheck)
    sdrBluetoothTests(passedCheck)
    print("\t ZigBee: {} \n".format(passedCheck))
    print("\t GSM: {} \n".format(passedCheck))
    print("Systems Check: \n")
    print("\t Antenna RX: {} \n".format(passedCheck))
    print("\t Antenna TX: {} \n".format(passedCheck))
    print("\t Sample Packet Decode: {} \n".format(passedCheck))
    

    print("System Hardware Check: \n")
    print("\t Wifi: {} \n".format(passedCheck))
    print("\t Bluetooth: {} \n".format(passedCheck))
    print("\t Database: {} \n".format(passedCheck))
    
""" 5. Settings Page - Save user preferences & configurations for network data manipulation """

def settingsPage():
    print("\t ;)  \n")

"""###########################################
########## PYTHON LIB SECTION ##########
###############################################"""

def createGraph(userSelectedCSV):

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
        with open(csvPathToFile) as csvFile:
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

def importCSV():

def exportCSV():


"""
###########################################
########## SYSTEM OUTPUT SECTION ##########
###########################################
"""

def displayNetworkGraphOptions(userCSV):

    def clearDisplayScreen():
        display_on = False

    list_commands = """
    ############################################
    ####### DISPLAY OPTIONS ####################
    ############################################
    File Selected: %s
    Program commands:\n
    \t 0. Read CSV - Output the raw contents of the CSV file \n
    \t 1. Generate Graph - Take the data held within the csv to create a graph. This graph will automatically pop up in a separate window \n
    \t (Q)uit - Quit this screen \n
    \n
    """ % (userCSV)

    #User Loop
    display_on = True

    #Available number options to execute commands

    options = OrderedDict((('0', partial(readCsvFile, userCSV)),
                           ('1', partial(createGraph, userCSV)),
                           ('Q', clearDisplayScreen)))
                           

    #Mandatory First print out of commands
    print list_commands

    #Main Program Loop
    while display_on:
            try:
                    #Get user string
                    user_key_input = raw_input('Enter number or (Q) to Quit: ').upper()
                    if user_key_input in options:
                            action = options[user_key_input]
                            action()
                    else:
                            print 'Unknown User Input! Try Again!'
            except:
                    break

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


def chooseFile(files_in_user_chosen_dir):

    fileNumber = 0
    
    #List contents of directory
    for file_in_dir in os.listdir(files_in_user_chosen_dir):
        print str(fileNumber) + ". " + file_in_dir
        fileNumber+=1
        #Get user input...

    #return user_file


def readCsvFile(userSelectedFile):

    #Temp fix for anyone running it...need to think about production
    #dir = os.path.dirname(__file__)
    #csvPathToFile = os.path.join(dir, 'network_scan_output', 'hackRFTestOutput.csv')
    #print(csvFile)
    csvPathToFile = chooseDir()
    csvPathToFile += '/src/infrastructure/network_scan_output/' + userSelectedFile
    if not os.path.isfile(csvPathToFile):
        print("\n The MCP has derezzed the file!\n")
        sys.exit()
    else:
        with open(csvPathToFile) as csvFile:
            #Use csv parser
            reader = csv.reader(csvFile, delimiter=',')
            for row in reader:
                print(row)

def cliProgress(end_val, bar_length):
    for i in xrange(0, end_val):
        percent = float(i) / end_val
        hashes = '#' * int(round(percent * bar_length))
        spaces = ' ' * (bar_length - len(hashes))
        #Emulate progress...
        time.sleep(0.1)
        sys.stdout.write("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
        sys.stdout.flush()
    print("\n")

"""
#Toggle on and off as necessary
if __name__ == "__main__":
        runTerminalMain()
"""
