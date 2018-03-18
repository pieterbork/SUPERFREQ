#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : lib_for_unit_test.py
#purpose : Custom library used solely for unit tests
#date : 2018.03.18
#version: 1.0.10
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

#Needs to call "main" database in SUPERFREQ/src/infrastructure/database. Will not work right now
db_path = root_path + 'src/infrastructure/database/SUPERFREQ.db'

""" Below Constants are called in app_unit_tests to ensure working availability anywhere in the app"""

#Network File Constants
wifi_onboard_path = root_path + 'src/UnitTests/Network_Devices_UnitTests/wifi_status.bash'
wifi_external_devices_path = root_path + 'src/UnitTests/Network_Devices_UnitTests/wifi_nearby_devices.bash'
bluetooth_onboard_path = root_path + 'src/UnitTests/Network_Devices_UnitTests/bluetooth_status.bash'
bluetooth_external_devices_path = root_path + 'src/UnitTests/Network_Devices_UnitTests/bluetooth_nearby_devices.bash'
#zigbee_onboard_path = root_path + 'src/UnitTests/Network_Devices_UnitTests/'
#zigbee_external_devices_path = root_path + 'src/UnitTests/Network_Devices_UnitTests/'
#lte_onboard_path = root_path = 'src/UnitTests/Network_Devices_UnitTests/'
#lte_external_devices_path = root_path + 'src/UnitTests/Network_Devices_UnitTests/'
ww_internet_path = root_path + 'src/UnitTests/Network_Devices_UnitTests/internet_status.bash'

#SDR File Constants
hackrf_usb_path = root_path + 'src/UnitTests/SDR_UnitTests/usb_status.bash'
#hackrf_rx_path = root_path + 'src/UnitTests/SDR_UnitTests/'
#hackrf_tx_path = root_path + 'src/UnitTests/SDR_UnitTests/'


#Internal System File Constants

#####   CSV Operations  ####
read_csv_path = root_path + 'src/UnitTests/Infrastructure_UnitTests/csv_operations/read_csv.py'
copy_delete_csv_path = root_path + 'src/UnitTests/Infrastructure_UnitTests/csv_operations/cp_rm.py'
csv_filter_path = root_path + 'src/UnitTests/Infrastructure_UnitTests/csv_operations/csv_filter.bash'
generate_graph_path = root_path + 'src/UnitTests/Infrastructure_UnitTests/csv_operations/generate_graph.py'

#####   DB Operations  #####

create_empty_db_path = root_path + 'src/UnitTests/Infrastructure_UnitTests/database_operations/create_empty_db.bash'
create_table_in_db_path = root_path + 'src/UnitTests/Infrastructure_UnitTests/database_operations/create_table_in_db.py'
query_db_path = root_path + 'src/UnitTests/Infrastructure_UnitTests/database_operations/query_db.py'
import_csv_to_db_path = root_path + 'src/UnitTests/Infrastructure_UnitTests/database_operations/import_csv_to_db.py'
export_csv_from_db_path = root_path + 'src/UnitTests/Infrastructure_UnitTests/database_operations/export_csv_from_db.py'

##### GUI Operations ####

tkinter_run_path = root_path + 'src/UnitTests/Infrastructure_UnitTests/tkinter_run.py'
flask_run_path = root_path + 'src/UnitTests/Infrastructure_UnitTests/flask_run.py'

#Standard test files
standard_csv_output_path = root_path + 'src/UnitTests/Infrastructure_UnitTests/csv_operations/to_copy.csv'
#graph_output_path = root_path + ''

#Define constants for files to be removed

#Check to ensure each file exists otherwise, we cannot test
def fileCheck():
    try:
    except:
        print "File does not exist in system path!"

#Not optimized yet (opens and closes per test right now)
def statusTest(rowid, test, boolean_value):
    try:
        db=sqlite3.connect(db_path)
        cursor = db.cursor()
        cursor.execute('''INSERT OR REPLACE INTO TestsSummary(id, test, status) VALUES(?,?,?)''', (rowid, test, boolean_value) )
        db.commit()
        db.close()
    except:
        print "Error when inserting/updating values into table"

#Remove listed files below after every test
def cleanUpTestDir():
    
    #Cleanup globally defined variables
    files_to_remove = []
    if all([os.path.isfile(f) for f in files_to_remove]):
        os.remove(f)
    else:
        print "Could not remove test files!"
    
