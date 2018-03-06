#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : network_operations.py
#purpose : Let users choose the following frequencies they wish to capture packets from: wifi, zigbee, bluetooth, lte?
#date : 2018.03.01
#version: 1.0.01
#version notes (latest): Compatible w/ python2

import sys
import time
import csv_operations
from multiprocessing import Process

#This will alert the end tester that the build environment for the hackrf is not present
try:
    from wifi.wifi_rx_rftap import captureWifi
except ImportError:
    print ("The GnuRadio dependencies are not present in this app! Talk to Pieter/Carlos...")

""" Special Functions for Network Operations """

def cliProgress(end_val, bar_length):
    for i in xrange(0, end_val):
        percent = float(i) / end_val
        hashes = '#' * int(round(percent * bar_length))
        spaces = ' ' * (bar_length - len(hashes))
        #Emulate progress...
        time.sleep(0.1)
        sys.stdout.write("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
        sys.stdout.flush()
    print("\n")


""" 1. Scan Network - Ensure our antenna can RX Data """

def hello():
    print "Hello, World!"

def networkOptions():

    #Emulate Scan Function
    print("\n\t Running Network Scan w/ HackRF... \n")
    print("\n\t If you wish to quit, press Ctrl C or ^C... \n")
    try:
        #Below is the actual function to run the HackRF. target=captureWifi function
        scan_process = Process(target=hello)
        cli_process = Process(target=cliProgress, args=(101, 20))
        cli_process.start()
        scan_process.start()
        #Wait until finished
        scan_process.join()
        cli_process.join()
        
        print("\n\t Results saved locally! Can be accessed by Option 2 on the command line... \n")
    except KeyboardInterrupt:
        print("\nscanNetwork: User stopped scan!!! Partial Data saved. Press enter to return to main program.")

    csv_operations.runTerminalInfraDir()
    
if __name__ == "__main__":
    networkOptions()
