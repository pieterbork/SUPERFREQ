#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : terminalFunctions.py
#purpose : File for all teammember to put in modular code. As the file grows we can separate the longer functions into separate files
#date : 2018.02.07
#version: 1.0.5
#version notes (latest): Compatible w/ python2


import subprocess
#This will alert the end tester that the build environment for the hackrf is not present
try:
    from sdr_modules.wifi_rx_rftap import tuneWifi
except ImportError:
    print ("The GnuRadio dependencies are not present in this app! Talk to Pieter/Carlos...")

#tuneRadio Logic Call

""" 1. Tune Radio - Ensure our antenna is RX Data """

def tuneRadio():
    print("\t Hello World of Radio's \n")
    try:
        tuneWifi.main()
    except:
        print("tuneRadio: You didn't say the magic words!!!")
    

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

def sdrWifiTests():
    wifi_return_code = subprocess.checkoutput("")
    #If wifi_return_code is true than a wireless service has been turned off
    if (wifi_return_code):
        print("\t Wifi: {} \n".format(passedCheck))
    else:
        passedCheck="On"
        print("\t Wifi: {} \n".format(passedCheck))

def sdrBluetoothTests():
    print("\t BlueTooth: {} \n".format(passedCheck))


def testSummary():

    passedCheck = "Off"
    
    print("SDR Hardware Check: \n")
    sdrWifiTests(passedCheck)
    sdrBluetoothTests(passedCheck)
    print("\t ZigBee: {} \n".format(passedCheck))
    print("\t GSM: {} \n".format(passedCheck))
    print("Systems Check: \n")
    print("\t Antenna RX: {} \n".format(passedCheck))
    print("\t Antenna TX: {} \n".format(passedCheck))
    print("\t Sample Packet Decode: {} \n".format(passedCheck))
    

    print("System Hardware Check: \n")
    print("\t Wifi: {} \n".format(passedCheck))
    print("\t Bluetooth: {} \n".format(passedCheck))
    print("\t Database: {} \n".format(passedCheck))
    
""" 6. Settings Page - Save user preferences & configurations for network data manipulation """

def settingsPage():
    print("\t ;)  \n")
