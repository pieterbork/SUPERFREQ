#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : lib_for_unit_test.py
#purpose : Custom library used solely for unit tests
#date : 2018.03.16
#version: 1.0.0
#version notes (latest): Compatible w/ python2
import os
import sqlite3

""" Global Variables here for simple testing """

#Set various paths used for testing
#Tell the system where we currently are
cwd = os.getcwd()
#print cwd
#Tell the system the root of our app is before 'src'
separator= 'src/'

#db path setup
db_path = cwd.split(separator, 1)[0]
#Needs to call "main" database in SUPERFREQ/src/infrastructure/database. Will not work right now
db_path += 'src/infrastructure/database/SUPERFREQ.db'

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
    return
