#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : query_db.py
#purpose : Query for testing
#date : 2018.03.16
#version: 1.0.1
#version notes (latest): Compatible w/ python2

import sys
import os
import sqlite3
import create_table_in_db

#Note when storing boolean values in SQLite they follow these rules: 0 (false) and 1 (true)
try:
    db=sqlite3.connect(create_table_in_db.db_path)
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM TestsSummary''')

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    db.close()
    print "Query Done!"
    
except:
    print "Error when querying TestsSummary"
