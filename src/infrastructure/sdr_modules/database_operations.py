#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : database_operations.py
#purpose : Allow user interaction with SQlite Database
#date : 2018.03.14
#version: 1.0.0
#version notes (latest): Compatible w/ python2
import sqlite3
import csv_operations

#Hacky for right now...setup path to the database (final DB and its path to be determined later)
db_path = csv_operations.getSourceDir()
db_path += 'src/infrastructure/database/SUPERFREQ.db'
print db_path

#SQLITe3 Shortcuts: https://sqlite.org/cli.html

""" 3. Database Operations - Import, Export, and save CSV data between app sessions """

def importCSV():
    #Import CSV contents into a database
    return

#This function may be phased out
def exportCSV():
    #Export CSV contents out of a database
    return

#Not optimized yet (opens and closes per test right now)
def statusTest(rowid, signal, boolean_value):
    try:
        db=sqlite3.connect(db_path)
        cursor = db.cursor()
        cursor.execute('''INSERT OR REPLACE INTO DeviceStatus(id, signal, status) VALUES(?,?,?)''', (rowid, signal, boolean_value) )
        db.commit()
        db.close()
    except:
        print "Error when inserting/updating values into table"


def databaseOperations():
    return


##

if __name__ == "__main__":
        databaseOperations()
