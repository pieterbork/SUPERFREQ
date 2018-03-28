#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : read_csv.py
#purpose : Check our read csv function
#date : 2018.03.24
#version: 1.0.0
#version notes (latest): Compatible w/ python2
import sys
import os
import csv
import cp_rm

src_file = cp_rm.root_path + "src/UnitTests/Infrastructure_UnitTests/csv_operations/filtered.csv"

if not os.path.isfile(src_file):
    print("\n The MCP has derezzed the file!\n")
    sys.exit()
else:
    with open(src_file) as csvFile:
        #Use csv parser
        reader = csv.reader(csvFile, delimiter=',')
        for row in reader:
            print(row)
