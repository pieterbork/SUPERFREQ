#!/bin/bash

#author : Kade Cooper kaco0964@colorado.edu
#name : create_empty_db.bash
#purpose : Use SQLite3 to create an empty db
#date : 2018.03.19
#version: 1.0.1

#Run SQLite3 to create an empty database 
sqlite3 SUPERFREQ_Test.db ".databases"

#Check status code to be passed on
if [ $? -eq 0 ]; then
	exit 0
else
	exit 1
fi