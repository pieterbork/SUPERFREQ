#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : lib_for_unit_test.py
#purpose : Custom library used solely for unit tests
#date : 2018.03.19
#version: 1.0.15
#version notes (latest): Compatible w/ python2

import os
import sqlite3


""" Global Constants here for simple testing """

#Set various paths used for testing
#Tell the system where we currently are
cwd = os.getcwd()
#print cwd
#Tell the system the root of our app is before 'src'
separator= 'src/'

#root path setup
root_path = cwd.split(separator, 1)[0]


#Standard test files that are checked within their respective tests:
# 1. to_copy.csv
# 2. unfiltered.csv
# 3. import.csv
# 4. export.csv

def fileCheckListCaller():

    """ Below Constants are called in app_unit_tests to ensure working availability anywhere in the app. Used Joins as they are usually faster"""

    #Network File Constants
    wifi_onboard_path = ''.join([root_path,'src/UnitTests/Network_Devices_UnitTests/wifi_status.bash'])
    wifi_external_devices_path = ''.join([root_path,'src/UnitTests/Network_Devices_UnitTests/wifi_nearby_devices.bash'])
    bluetooth_onboard_path = ''.join([root_path,'src/UnitTests/Network_Devices_UnitTests/bluetooth_status.bash'])
    bluetooth_external_devices_path = ''.join([root_path,'src/UnitTests/Network_Devices_UnitTests/bluetooth_nearby_devices.bash'])
    #zigbee_onboard_path = ''.join([root_path,'src/UnitTests/Network_Devices_UnitTests/'])
    #zigbee_external_devices_path = ''.join([root_path,'src/UnitTests/Network_Devices_UnitTests/'])
    #lte_onboard_path = ''.join([root_path,'src/UnitTests/Network_Devices_UnitTests/'])
    #lte_external_devices_path = ''.join([root_path,'src/UnitTests/Network_Devices_UnitTests/'])
    ww_internet_path = ''.join([root_path,'src/UnitTests/Network_Devices_UnitTests/internet_status.bash'])

    #Network File List of Paths
    network_file_paths_list = [wifi_onboard_path, wifi_external_devices_path, bluetooth_onboard_path, bluetooth_external_devices_path, ww_internet_path]

    """ """
    
    #SDR File Constants
    hackrf_usb_path = ''.join([root_path,'src/UnitTests/SDR_UnitTests/usb_status.bash'])
    #hackrf_rx_path = ''.join([root_path,'src/UnitTests/SDR_UnitTests/'])
    #hackrf_tx_path = ''.join([root_path,'src/UnitTests/SDR_UnitTests/'])

    #SDR File List of Paths
    sdr_file_paths_list = [hackrf_usb_path]


    """ """


    #Internal System File Constants

    #####   CSV Operations  ####
    read_csv_path = ''.join([root_path,'src/UnitTests/Infrastructure_UnitTests/csv_operations/read_csv.py'])
    copy_delete_csv_path = ''.join([root_path,'src/UnitTests/Infrastructure_UnitTests/csv_operations/cp_rm.py'])
    csv_filter_path = ''.join([root_path,'src/UnitTests/Infrastructure_UnitTests/csv_operations/csv_filter.bash'])
    generate_graph_path = ''.join(['src/UnitTests/Infrastructure_UnitTests/csv_operations/generate_graph.py'])

    #CSV File List of Paths
    csv_internal_file_paths_list = [read_csv_path, copy_delete_csv_path, csv_filter_path, generate_graph_path]

    #####   DB Operations  #####

    create_empty_db_path = ''.join([root_path,'src/UnitTests/Infrastructure_UnitTests/database_operations/create_empty_db.bash'])
    create_table_in_db_path = ''.join([root_path,'src/UnitTests/Infrastructure_UnitTests/database_operations/create_table_in_db.py'])
    query_db_path = ''.join([root_path,'src/UnitTests/Infrastructure_UnitTests/database_operations/query_db.py'])
    import_csv_to_db_path = ''.join([root_path,'src/UnitTests/Infrastructure_UnitTests/database_operations/import_csv_to_db.py'])
    export_csv_from_db_path = ''.join([root_path,'src/UnitTests/Infrastructure_UnitTests/database_operations/export_csv_from_db.py'])

    #DB File List of Paths
    db_internal_file_paths_list = [create_empty_db_path, create_table_in_db_path, query_db_path, import_csv_to_db_path, export_csv_from_db_path]


    """ """

    
    ##### GUI Operations ####

    tkinter_run_path = ''.join([root_path,'src/UnitTests/Infrastructure_UnitTests/tkinter_run.py'])
    flask_run_path = ''.join([root_path,'src/UnitTests/Infrastructure_UnitTests/flask_run.py'])


    #GUI File List of Paths
    gui_file_paths_list = [tkinter_run_path, flask_run_path]


    """ """

    #Use fileCheck to see if the paths in the above lists do indeed exist. This is here for ease of control for turning on and off
    fileCheck(network_file_paths_list)
    fileCheck(sdr_file_paths_list)
    fileCheck(csv_internal_file_paths_list)
    fileCheck(db_internal_file_paths_list)
    fileCheck(gui_file_paths_list)

#Check to ensure each file exists otherwise, we cannot test
def fileCheck(file_paths_list):
    try:
        for path in file_paths_list:
            if os.path.isfile(path):
                #print("\n {} Exists!\n").format(path)
    except:
        print "File does not exist in system path!"

#Not optimized yet (opens and closes per test right now)
def statusTest(rowid, test, boolean_value):
    try:
        #Needs to call "main" database in SUPERFREQ/src/infrastructure/database. Will not work right now
        db_path = root_path + 'src/infrastructure/database/SUPERFREQ.db'
        db=sqlite3.connect(db_path)
        cursor = db.cursor()
        cursor.execute('''INSERT OR REPLACE INTO TestsSummary(id, test, status) VALUES(?,?,?)''', (rowid, test, boolean_value) )
        db.commit()
        db.close()
    except:
        print "Error when inserting/updating values into table"

#Remove listed files below after every test
def cleanUpTestDir():

    """ Define constants for files to be removed """
    filter_csv_output_path = ''.join([root_path,'src/UnitTests/Infrastructure_UnitTests/csv_operations/filtered.csv'
    testdata_csv_output_path = ''.join([root_path,'src/UnitTests/Infrastructure_UnitTests/csv_operations/test_data.png'
    superfreqtest_db_path = ''.join([root_path,'src/UnitTests/Infrastructure_UnitTests/database_operations/SUPERFREQ_Test.db']

    
    #Cleanup locally defined constants
    files_to_remove = [filter_csv_output_path, testdata_csv_output_path, superfreqtest_db_path]
    if all([os.path.isfile(f) for f in files_to_remove]):
        os.remove(f)
    else:
        print "Could not remove test files!"


#Call individual functions here
#fileCheckListCaller()
    
