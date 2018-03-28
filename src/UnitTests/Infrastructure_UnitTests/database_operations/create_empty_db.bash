#!/bin/bash

#author : Kade Cooper kaco0964@colorado.edu
#name : create_empty_db.bash
#purpose : Use SQLite3 to create an empty db
#date : 2018.03.26
#version: 1.0.10

CURRENTDIR=`pwd | sed 's/\(src\).*/\1/g'`
PATHTODB='/UnitTests/Infrastructure_UnitTests/database_operations/SUPERFREQ_Test.db'
#Concatenate the two strings
FULLPATH=$CURRENTDIR$PATHTODB

#Run SQLite3 to create an empty database 
sqlite3 $FULLPATH ".databases"

#Check status code to be passed on
if [ $? -eq 0 ]; then
	exit 0
else
	exit 1
fi