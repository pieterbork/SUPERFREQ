import os
import sys
import csv

def chart():
    print("\t Reading CSV File and Generating Graph... \n")
    #Create lists
    labels=[]
    values=[]

    #Check csv file
    if not os.path.isfile('WifiTest.csv'):
        print("\n The MCP has derezzed the file!\n")
  
    with open('WifiTest.csv') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        for row in reader:
            labels.append(row[3]+"-"+row[6])
            values.append(float(row[7]))
        print(labels)

chart()