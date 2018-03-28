#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : export_csv_from_db.py
#purpose : Try to import a csv into our db
#date : 2018.03.26
#version: 1.0.10
#version notes (latest): Compatible w/ python2

import os
import sqlite3
import csv
import create_table_in_db

#Import root path
root_path = create_table_in_db.root_path

#CSV file to export
csv_path = root_path + 'src/UnitTests/Infrastructure_UnitTests/database_operations/export.csv'


#Check if an empty export.csv file exists
if os.path.isfile(csv_path):
    print "Export csv file exists!"
else:
    print "NO import.csv detected! Exiting..."
    sys.exit()

#Database file to use
db_path = create_table_in_db.db_path

#Note when storing boolean values in SQLite they follow these rules: 0 (false) and 1 (true)
try:
    db=sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM Wifi''')

    with open(csv_path, 'wb') as csv_out:
        writer = csv.writer(csv_out)
        writer.writerow([ i[0] for i in cursor.description ]) # heading row
        writer.writerows(cursor.fetchall())

    db.close()
    print "Export from DB Done!"
    
except:
    print "Error when exporting from Wifi Table in SUPERFREQ_Test.db"
