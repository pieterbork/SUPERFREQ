#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : create_table_in_db.py
#purpose : Create table in db for testing
#date : 2018.03.24
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
