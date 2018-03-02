#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : csv_operations.py
#purpose : Allow the user to easily traverse our app structure and have options in relation to csv data. May or may not merge with database file
#date : 2018.03.01
#version: 1.0.25
#version notes (latest): Compatible w/ python2


import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
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

def getSelectedDir(directory_list):

    #Set loop variables
    dir_number = 0
    dir_list = []
    dir_loop_on = True

    print("\t Listing Available Data Directories to Choose From... \n")
    
    #List contents of directory
    for dirs_in_dir in os.listdir(directory_list):
        print str(dir_number) + ". " + dirs_in_dir
        #Pass in lists (arrays)
        number_and_dir = [str(dir_number), dirs_in_dir]
        dir_list.append(number_and_dir)
        dir_number+=1

    #Turn our list into an Ordered dictionary (hastable)
    dir_list = OrderedDict(dir_list)

    while dir_loop_on:
        try:
            #Get user string
            user_key_input = raw_input('\nEnter number or (Q) to Quit: ').upper()
            if user_key_input in dir_list:
                folder_to_open = dir_list[user_key_input]
                return folder_to_open
            elif user_key_input == 'Q':
                return
            else:
                print '\nUnknown User Input! Try Again!\n'
        except:
            return


def getSelectedFile(directory_list):

    #Set loop variables
    file_number = 0
    file_list = []
    file_loop_on = True
    
    #List contents of directory
    for file_in_dir in os.listdir(directory_list):
        print str(file_number) + ". " + file_in_dir
        number_and_file = [str(file_number), file_in_dir]
        file_list.append(number_and_file)
        file_number+=1

    #Turn our list into an Ordered dictionary (hastable)
    file_list = OrderedDict(file_list)

    while file_loop_on:
        try:
            #Get user string
            user_key_input = raw_input('\nEnter number or (Q) to Quit: ').upper()
            if user_key_input in file_list:
                file_selected = file_list[user_key_input]
                return file_selected
            elif user_key_input == 'Q':
                break
            else:
                print '\nUnknown User Input! Try Again!\n'
        except:
            break

def displayCsvOptions(userCSV):

    def exitNetworkOptions():
        csvOperations()

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

    #User Loop
    display_on = True

    #Available number options to execute commands

    options = OrderedDict((('0', partial(readCsvFile, userCSV)),
                           ('1', partial(createGraph, userCSV)),
                           ('2', partial(removeCsvFile, userCSV)),
                           ('Q', exitNetworkOptions)))
                           

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
                            print '\nUnknown User Input! Try Again!\n'
            except:
                    break


def readCsvFile(file_path):

    #Temp fix for anyone running it...need to think about production
    #dir = os.path.dirname(__file__)
    #csvPathToFile = os.path.join(dir, 'network_scan_output', 'hackRFTestOutput.csv')
    #print(csvFile)
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



""" 2. Display Network Data - Interactive Graphs & Statistics """

def csvOperations():

    """ LOCAL VARIABLES FOR DIRECTORY LISTING """
    #"Locate" our data directory from anywhere
    directory_list = getSourceDir()
    
    #Add path to file we wish to execute
    directory_list += 'src/infrastructure/network_scan_output/'

    """ """
    

    """ LET USER CHOOSE DIRECTORY """
    
    #Call our directory lister
    folder_user_opened = getSelectedDir(directory_list)
    
    
    #Append folder to full path, so files in the path can be listed
    try:
        directory_list += folder_user_opened
    except:
        return

    """ """


    """ LET USER CHOOSE FILE TO GET ADDITIONAL OPTIONS """
    #Call our file lister
    file_user_chose = getSelectedFile(directory_list)


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
