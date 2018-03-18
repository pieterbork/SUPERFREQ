#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : create_table_in_db.py
#purpose : Create table in db for testing
#date : 2018.03.16
#version: 1.0.1
#version notes (latest): Compatible w/ python2

import sys
import os
import sqlite3

#Set various paths used for testing
#Tell the system where we currently are
cwd = os.getcwd()
#print cwd
#Tell the system the root of our app is before 'src'
separator= 'src/'

#root path setup
root_path = cwd.split(separator, 1)[0]

db_path = root_path + 'src/UnitTests/Infrastructure_UnitTests/database_operations/SUPERFREQ_Test.db'

#Note when storing boolean values in SQLite they follow these rules: 0 (false) and 1 (true)
try:
    db=sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS TestsSummary(id INTEGER PRIMARY KEY, test VARCHAR(30), status INTEGER(1))''')
    db.commit()
    db.close()
    print "Table successfully created!"
except:
    print "Error when creating the TestsSummary Table"

"""
try:
    db=sqlite3.connect('./SUPERFREQ.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Directories(id INTEGER PRIMARY KEY, directory_name VARCHAR(15))''')
    db.commit()

except:
    print "Error when creating the Directories Table (Parent)"

try:
    db=sqlite3.connect('./SUPERFREQ.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Files(id INTEGER PRIMARY KEY, directory_id INTEGER, file_name VARCHAR(128), FOREIGN KEY(directory_id) REFERENCES Directories(id))''')
    #Need some way to grab all the files in the directory
    db.commit()

except:
    print "Error when creating the Files Table (Child)"

#Problems with approach...user has to input the file name to be added everytime.
try:
    db=sqlite3.connect('./SUPERFREQ.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Data(id INTEGER PRIMARY KEY, file_name VARCHAR(128), duration CHAR(6), frame_control CHAR(6), subtype CHAR(20), ssid CHAR(50), seq_nr CHAR(6), mac CHAR(20), freq CHAR(20), percentage REAL(10) FOREIGN KEY(file_name) REFERENCES Files(id))''')
    with open('./2018-02-18_00:00:00_wifi_unfiltered.csv', 'rb') as fin:
        #csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # comma is default delimiter
        to_db = [(i['id'], i['file_name'], i['duration'], i['frame_control'], i['subtype'], i['ssid'], i['seq_nr'], i['mac'], i['freq'], i['percentage']]) for i in dr]
    cursor.executemany("INSERT INTO Data (id, file_name, duration, frame_control, subtype, ssid, seq_nr, mac, freq, percentage) VALUES (?,?,?,?,?,?,?,?,?,?);", to_db)
    db.commit()
    db.close()

except:
    print "Error when creating the Data Table (Grandchild)"

"""
