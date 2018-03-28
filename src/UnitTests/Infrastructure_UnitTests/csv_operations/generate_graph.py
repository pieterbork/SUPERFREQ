#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : generate_graph.py
#purpose : Test numpy and matplotlib libraries for Python2
#date : 2018.03.18
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
labels=[]
perc=[]

#Format of csv: Duration,Frame Control,Subtype,SSID,seq nr,mac 1, mac occurence
#Color scheme
a = np.random.random(40)
cs = cm.Set1(np.arange(40)/40.)

sample_csv = cp_rm.src_file
print sample_csv

#Check csv file
if not os.path.isfile(sample_csv):
    print("\n The MCP has derezzed the file!\n")
    sys.exit()
else:
    with open(sample_csv) as csvFile:
        #Use csv parser
        reader = csv.reader(csvFile, delimiter=',')
        for row in reader:
            labels.append(row[3]+"-"+row[6])
            perc.append(float(row[7]))
            
    #Add data to plot
    plt.pie(perc, labels=labels, autopct='%1.1f%%', colors=cs, shadow=True, startangle=90)

    #Use for changing font colors
    """   _, _, autotexts = plt.pie(perc, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    for autotext in autotexts:
        autotext.set_color('grey')
    """

    #Rounds plot
    plt.axis('equal')
    plt.title("Frequency of MAC Addresses\n")

    #Save Image
    plt.savefig('test_data.png', bbox_inches='tight')
