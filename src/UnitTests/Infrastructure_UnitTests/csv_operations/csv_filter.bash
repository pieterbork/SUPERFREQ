#!/bin/bash

#author : Kade Cooper kaco0964@colorado.edu
#name : csv_filter.bash
#purpose : Filter csv files to help generate graphs from the terminal application
#date : 2018.03.17
#version: 1.0.0

#Find number of occurences for each line.
sort unfiltered.csv | uniq --count | sort -nr

#Find total number of lines. VERIFIED!
wc -l unfiltered.csv | awk '{print $1}'

#Remove duplicate lines
awk '!a[$0]++' unfiltered.csv