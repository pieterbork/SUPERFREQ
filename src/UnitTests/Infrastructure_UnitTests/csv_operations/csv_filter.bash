#!/bin/bash

#author : Kade Cooper kaco0964@colorado.edu
#name : csv_filter.bash
#purpose : Filter csv files to help generate graphs from the terminal application
#date : 2018.03.20
#version: 1.0.0

#Find number of occurences for each line.
sort unfiltered.csv | uniq --count | sort -nr

#Find total number of lines. VERIFIED!
wc -l unfiltered.csv | awk '{print $1}'

#Remove duplicate lines
awk '!a[$0]++' unfiltered.csv

#After all is said and done, use Vim in Ex mode to add header column to the file for importing into the database
ex -sc '1i|duration,frame,subtype,ssid,seq_nr,mac_address,frequency,percentage' -cx filtered.csv