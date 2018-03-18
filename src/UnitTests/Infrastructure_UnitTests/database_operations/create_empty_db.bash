#!/bin/bash

#author : Kade Cooper kaco0964@colorado.edu
#name : create_empty_db.bash
#purpose : Use SQLite3 to create an empty db
#date : 2018.03.16
#version: 1.0.0

#Run SQLite3 create database command..TO BE Verified!
sqlite3 SUPERFREQ_Test.db ".empty"

#Check status code to be passed on
if [ $? -eq 0 ]; then
	exit 0
else
	exit 1
fi