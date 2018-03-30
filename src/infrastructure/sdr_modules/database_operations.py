#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : database_operations.py
#purpose : Allow user interaction with SQlite Database
#date : 2018.03.30
#version: 1.0.15
#version notes (latest): Compatible w/ python2

import os 
import sqlite3
import csv
import traceback
import system_module_operations
from functools import partial
from collections import OrderedDict

#Hacky for right now...setup path to the database (final DB and its path to be determined later)
db_path = system_module_operations.getSourceDir()
db_path += 'src/infrastructure/database/SUPERFREQ.db'
#print db_path

#SQLite3 Shortcuts: https://sqlite.org/cli.html

def importWifiCSV(csv_path):
    
    #Run our import code
    try:
        db = sqlite3.connect(db_path)
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Wifi(duration VARCHAR(6), frame VARCHAR(6), subtype VARCHAR(20), ssid VARCHAR(30), seq_nr VARCHAR(10), mac_address_1 VARCHAR(120), mac_address_2 VARCHAR(120), mac_address_3 VARCHAR(120), frequency VARCHAR(10), occurrence REAL(10))''')

        with open(csv_path,'rb') as wifi_table:
            dr = csv.DictReader(wifi_table, delimiter=',') #comma is default delimiter
            to_db = [(i['duration'], i['frame'], i['subtype'], i['ssid'], i['seq_nr'], i['mac_address_1'], i['mac_address_2'], i['mac_address_3'], i['frequency'], i['occurrence']) for i in dr]

        cursor.executemany('''INSERT OR IGNORE INTO Wifi(duration, frame, subtype, ssid, seq_nr, mac_address_1, mac_address_2, mac_address_3, frequency, occurrence) VALUES(?,?,?,?,?,?,?,?,?,?)''', to_db)
        db.commit()
        db.close()
        print "Table content from CSV successfully imported!"

    except:
        traceback.print_exc()
        #Import CSV contents into a database
        return

def importBtCSV(csv_path):
    return

def importXbeeCSV(csv_path):
    return


def exportCsv(csv_path):
    
    #Export CSV contents out of a database
    #Note when storing boolean values in SQLite they follow these rules: 0 (false) and 1 (true)
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

    #See which directory the user choice
    end_dir = os.path.basename(os.path.normpath(directory_list))

    #Create a string based off of end dir
    if (end_dir == 'wifi'):
        chosen_export_table_string = '''SELECT * FROM Wifi'''
        export_file_directory = db_path + 'src/infrastructure/network_scan_output/wifi/wifi_table_export.csv'
    elif (end_dir == 'bluetooth'):
        chosen_export_table_string = '''SELECT * FROM Bluetooth'''
        export_file_directory = db_path + 'src/infrastructure/network_scan_output/bluetooth/bluetooth_table_export.csv'
    elif (end_dir == 'zigbee'):
        chosen_export_table_string = '''SELECT * FROM Xbee'''
        export_file_directory = db_path + 'src/infrastructure/network_scan_output/zigbee/zigbee_table_export.csv'
    
    try:
        db=sqlite3.connect(db_path)
        cursor = db.cursor()
        cursor.execute(chosen_export_table_string)

        with open(export_file_directory, 'wb') as csv_out:
            writer = csv.writer(csv_out)
            writer.writerow([ i[0] for i in cursor.description ]) # heading row
            writer.writerows(cursor.fetchall())

        db.close()
        print "Export from DB Done!"

    except:
        print "Error when exporting from Wifi Table in SUPERFREQ_Test.db"
        return

def displayTables(userSignalTable):

    #Note when storing boolean values in SQLite they follow these rules: 0 (false) and 1 (true)
    try:
        db=sqlite3.connect(db_path)
        cursor = db.cursor()
        cursor.execute(userSignalTable)

        rows = cursor.fetchall()

        for row in rows:
            print(row)
            db.close()

    except:
        print "Error when querying TestsSummary: \n"
        traceback.print_exc()


""" 3. Database Operations - Import, Export, and save CSV data between app sessions """
    

def displayDatabaseOptions():


    list_commands = """
    ############################################
    ####### DATABASE OPTIONS ####################
    ############################################\n
    File Selected: %s\n
    Program commands:\n
    \t 0. Export CSV from Database - Take the data held within the csv to create a graph. This graph will automatically pop up in a separate window \n
    \t 1. Display Tests Table - Show all content held within Tests Table\n
    \t 2. Display Wifi Table - Show all content held within Wifi Table\n
    \t 3. Display Bluetooth Table - Show all content held within BlueTooth Table\n
    \t 4. Display Xbee Table - Show all content held within Xbee Table\n
    \t (Q)uit - Quit this screen \n
    """

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

    options = OrderedDict((('0', exportCsv),
                           ('1', partial(displayTables,'''SELECT * FROM TestsSummary''')),
                           ('2', partial(displayTables,'''SELECT * FROM Wifi''')),
                           ('3', partial(displayTables,'''SELECT * FROM Bluetooth''')),
                           ('4', partial(displayTables,'''SELECT * FROM Xbee'''))))
                           

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


##

if __name__ == "__main__":
    displayDatabaseOptions()
