#!/usr/bin/env python2

#author : Jing Guo jing.guo@colorado.edu
#name : Flask.py
#purpose :  The friendly GUI for novice users
#date : 2018.02.14
#version : 1.0.1
#version notes (latest): Compatible w/ python2. 

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import os
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from multiprocessing import Process

app = Flask(__name__)

"""
cwd = os.getcwd()
separator = 'src/'
root_path = cwd.split(separator, 1)[0]
"""
#Unit Test Database
#DATABASE = root_path + "src/infrastructure/database/SUPERFREQ.db"


#Create a User home page and check our app flask is operational
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan')
def scanNetwork():
    return render_template('scan.html')

@app.route('/image')
def scanImage():
    return render_template('image.html')

@app.route('/database')
def viewDatabase():
    return render_template('database.html')

app.route('/importCSV')
def importCSV():
    return render_template('importCSV.html')

app.route('/tests')
def runTests():
    return render_template('tests.html')

@app.route('/images')
def images():
    fig=displayNetworkData()
    img = StringIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')

""" 2. Display Network Data - Interactive Graphs & Statistics 

def displayNetworkData():
    print("\t Reading CSV File and Generating Graph... \n")

    
    """Below is for testing...."""
    #Original File Output is based off of - out.csv

    #Create lists
    labels=[]
    perc=[]

    #Format of csv: Duration,Frame Control,Subtype,SSID,seq nr,mac 1, mac occurence
    #Color scheme
    a = np.random.random(40)
    cs = cm.Set1(np.arange(40)/40.)

    #Check csv file
    if not os.path.isfile('WifiTest.csv'):
        print("\n The MCP has derezzed the file!\n")
        sys.exit()
    else:
        with open('WifiTest.csv') as csvFile:
            #Use csv parser
            reader = csv.reader(csvFile, delimiter=',')
            for row in reader:
                labels.append(row[4]+"-"+row[7])
                perc.append(float(row[8]))
                
        #Add data to plot
        plt.pie(perc, labels=labels, autopct='%1.1f%%', colors=cs, shadow=True, startangle=90)

        #Use for changing font colors
        #   _, _, autotexts = plt.pie(perc, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        #for autotext in autotexts:
        #    autotext.set_color('grey')
        

        #Rounds plot
        plt.axis('equal')
        plt.title("Frequency of MAC Addresses\n")

        #Create Image
        plt.show()  
"""

"""3.Using Chartjs"""
def chartjs():
    #Check csv file
    if not os.path.isfile('WifiTest.csv'):
        print("\n The MCP has derezzed the file!\n")
        sys.exit()
    else:
        with open('WifiTest.csv') as csvFile:
            #Use csv parser
            reader = csv.reader(csvFile, delimiter=',')
            for row in reader:
                labels.append(row[3]+"-"+row[6])
                perc.append(float(row[7]))



#Error handling function
@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def errorpage(e):
    return("something going wrong here")

    #Run main program
if __name__ == '__main__':
    app.debug = True
    try:
        app.run(host='127.0.0.1', port=7721)
    except:
        print("Host on 127.0.0.1, Port: 7721, is currently unavailable.")