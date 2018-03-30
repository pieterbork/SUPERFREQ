#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : generate_graph.py
#purpose : Test numpy and matplotlib libraries for Python2
#date : 2018.03.29
#version: 1.0.0
#version notes (latest): Compatible w/ python2

import sys
import os
import csv
import cp_rm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#Create lists

xaxis=[]
yaxis=[]

#Format of csv: Duration,Frame Control,Subtype,SSID,seq nr,mac 1, mac occurence
#Color scheme
a = np.random.random(40)
cs = cm.Set1(np.arange(40)/40.)

sample_csv = cp_rm.src_file

output_png = cp_rm.root_path + 'src/UnitTests/Infrastructure_UnitTests/csv_operations/test_data.png'


#Check csv file
if not os.path.isfile(sample_csv):
    print("\n The MCP has derezzed the file!\n")
    sys.exit()
else:
    ssid_list = list(range(0,20))
    with open(sample_csv) as csvFile:
        #Use csv parser
        reader = csv.reader(csvFile, delimiter=',')
        next(reader, None) #Skip headers
        for row in reader:
            #Check for blank lines
            xaxis.append(row[3]+"-"+row[8].strip())
            yaxis.append(int(row[9]))

    #Add values to chart
    barWidth = 1.0
    plt.bar(ssid_list, yaxis, barWidth, color=cs)
    plt.xticks(ssid_list, xaxis, rotation=(45), fontsize = 10, va='bottom', ha='left')
    
    #Labels
    plt.ylabel("Occurrence(s)")
    plt.xlabel("SSID - Frequency")
    #Rounds plot
    #plt.axis('tight')
    plt.title("Frequency of MAC Addresses\n")

    #Save Image
    plt.savefig(output_png, bbox_inches='tight')
