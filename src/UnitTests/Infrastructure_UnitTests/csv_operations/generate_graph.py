#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : generate_graph.py
#purpose : Test numpy and matplotlib libraries for Python2
#date : 2018.03.28
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
#labels=[]
#perc=[]

xaxis=[]
yaxis=[]

#Format of csv: Duration,Frame Control,Subtype,SSID,seq nr,mac 1, mac occurence
#Color scheme
a = np.random.random(40)
cs = cm.Set1(np.arange(40)/40.)

sample_csv = cp_rm.src_file

"""
#Check csv file
if not os.path.isfile(sample_csv):
    print("\n The MCP has derezzed the file!\n")
    sys.exit()
else:
    counter = 0
    with open(sample_csv) as csvFile:
        #Use csv parser
        reader = csv.reader(csvFile, delimiter=',')
        for row in reader:
            if counter < 10:
                labels.append(row[3]+"-"+row[8])
                perc.append(float(row[9]))
            counter += 1
            
    #Add data to plot
    plt.pie(perc, labels=labels, autopct='%1.1f%%', colors=cs, shadow=True, startangle=90)

"""
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
    plt.savefig('test_data.png', bbox_inches='tight')
