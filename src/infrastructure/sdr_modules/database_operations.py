#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : database_operations.py
#purpose : Allow user interaction with SQlite Database
#date : 2018.03.29
#version: 1.0.10
#version notes (latest): Compatible w/ python2

import sqlite3
import csv
import traceback
import system_module_operations

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

#This function may be phased out
def exportCsv(csv_path):
    #Export CSV contents out of a database
    #Note when storing boolean values in SQLite they follow these rules: 0 (false) and 1 (true)
    try:
        db=sqlite3.connect(db_path)
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM Wifi''')

        with open('export.csv', 'wb') as csv_out:
            writer = csv.writer(csv_out)
            writer.writerow([ i[0] for i in cursor.description ]) # heading row
            writer.writerows(cursor.fetchall())

        db.close()
        print "Export from DB Done!"

    except:
        print "Error when exporting from Wifi Table in SUPERFREQ_Test.db"
        return

def displayTable():

    #Note when storing boolean values in SQLite they follow these rules: 0 (false) and 1 (true)
    try:
        db=sqlite3.connect(create_table_in_db.db_path)
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM TestsSummary''')

        rows = cursor.fetchall()

        for row in rows:
            print(row)
            db.close()

    except:
        print "Error when querying TestsSummary"
    

def displayDatabaseOptions(userCSV):
    
    def exitCsvOptions():
        display_on = False
        databaseOperations()

    list_commands = """
    ############################################
    ####### DATABASE OPTIONS ####################
    ############################################\n
    File Selected: %s\n
    Program commands:\n
    \t 0. Export CSV from Database - Take the data held within the csv to create a graph. This graph will automatically pop up in a separate window \n
    \t 1. Display Table - Show all content held within user chosen Table\n
    \t (Q)uit - Quit this screen \n
    """ % (userCSV)

    #User Loop
    display_on = True

    #Available number options to execute commands

    options = OrderedDict((('0', partial(exportCsv, userCSV)),
                           ('1', displayTable),
                           ('Q', exitCsvOptions),
                           ('q', exitCsvOptions)))
                           

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
                    else:
                            print '\nUnknown User Input! Try Again!\n'
            except:
                    break


""" 3. Database Operations - Import, Export, and save CSV data between app sessions """


def databaseOperations():

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
    displayDatabaseOptions(directory_list)


##

if __name__ == "__main__":
        #databaseOperations()
    #Hard code test
    importWifiCSV('/home/pi/Capstone/SUPERFREQ/src/infrastructure/network_scan_output/wifi/wifi_data_graph_ready.csv')
