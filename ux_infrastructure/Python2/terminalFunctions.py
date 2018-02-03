#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : terminalFunctions.py
#purpose : File for all teammember to put in modular code. As the file grows we can separate the longer functions into separate files
#date : 2018.02.03
#version: 1.0.0
#version notes (latest): Compatible w/ python2


""" 1. Tune Radio - Ensure our antenna is RX Data """

def tuneRadio():
    print("\t Hello World of Radio's \n")

""" 2. Display Network Data - Interactive Graphs & Statistics """

def displayNetworkData():
    print("\t Graphs Here \n")

""" 3. Decode Network Data - Scan, capture, parse various network protocols """

def decodeNetworkData():
    print("\t BeepBoopBeep\n")

""" 4. View Database - View saved network data """

def viewDatabase():
    print("\t MySQL \n")

""" 5. Test Summary - Provide quick network/system checks in an easy to read format """

def testSummary():

    passedCheck = "On"
    
    print("Network Check: \n")
    print("\t Wifi: {} \n".format(passedCheck))
    print("\t BlueTooth: {} \n".format(passedCheck))
    print("\t ZigBee: {} \n".format(passedCheck))
    print("\t GSM: {} \n".format(passedCheck))
    print("Systems Check: \n")
    print("\t Antenna RX: {} \n".format(passedCheck))
    print("\t Antenna TX: {} \n".format(passedCheck))
    print("\t Sample Packet Decode: {} \n".format(passedCheck))
    print("\t Database Running: {} \n".format(passedCheck))
    
""" 6. Settings Page - Save user preferences & configurations for network data manipulation """

def settingsPage():
    print("\t ;)  \n")
