#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : import_csv_to_db.py
#purpose : Try to import a csv into our db
#date : 2018.03.19
#version: 1.0.1
#version notes (latest): Compatible w/ python2

import os
import sys
import sqlite3
import csv
import create_table_in_db

#Import root path
root_path = create_table_in_db.root_path

#CSV file to import
csv_path = root_path + 'src/UnitTests/Infrastructure_UnitTests/database_operations/import.csv'

#Check that import.csv exists
if os.path.isfile(csv_path):
    print "Import csv file exists!"
else:
    print "NO import.csv detected! Exiting..."
    sys.exit()
    
#Database file to use
db_path = create_table_in_db.db_path


#Run our import code
try:
    db=sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Wifi(id INTEGER PRIMARY KEY, ssid VARCHAR(30), latency INTEGER(6), mac_address VARCHAR(120), frequency VARCHAR(10), percentage REAL(10))''')

    with open(csv_path,'rb') as wifi_table:
        dr = csv.DictReader(wifi_table, delimiter=',') #comma is default delimiter
        to_db = [(i['ssid'], i['latency'], i['mac_address'], i['frequency'], i['percentage']) for i in dr]

    cursor.executemany('''INSERT INTO Wifi(ssid, latency, mac_address, frequency, percentage) VALUES(?,?,?,?,?)''', to_db)
    db.commit()
    db.close()
    print "Table content from CSV successfully imported!"
    
except:
    print "Error when importing the CSV"
