#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : network_operations.py
#purpose : Let users choose the following frequencies they wish to capture packets from: wifi, zigbee, bluetooth, lte?
#date : 2018.03.10
#version: 1.1.09
#version notes (latest): Compatible w/ python2

import sys
import time
import csv_operations
from multiprocessing import Process
from functools import partial
from collections import OrderedDict

#This will alert the end tester that the build environment for the hackrf is not present
#This may or may not be used...haven't had best of luck with something that should be working
try:
    from wifi.wifi_rx_rftap import captureWifi
    #from bluetooth.bluetooth_rx_rftap import captureBlu
    #from zigbee.zigbee_rx_rftap import captureZigbee
    #from lte.lte_rx_rftap import captureLte
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

""" Network Scans """

def wifiScan(frequency_options):

    frequency_options += '/wifi/wifi_rx_rftap.py'
    scan_string = "WIFI"
    scanOperations(frequency_options, scan_string)

#TO DO
def bluScan(frequency_options):

    frequency_options += '/bluetooth/'
    scan_string = "BLUETOOTH"
    scanOperations(frequency_options, scan_string)

def zigbeeScan(frequency_options):

    frequency_options += '/zigbee/'
    scan_string = "ZIGBEE"
    scanOperations(frequency_options, scan_string)

#TO DO
def lteScan(frequency_options):

    frequency_options += '/lte/'
    scan_string = "LTE"
    scanOperations(frequency_options, scan_string)

def scanOperations(function_path, scan_string):

    print("\n\t Running %s Scan w/ HackRF... \n") %scan_string
    print("\n\t If you wish to quit, press Ctrl C or ^C... \n")
    try:
        #Below is the actual function to run the HackRF. target=captureWifi function
        scan_process = Process(target=function_path)
        cli_process = Process(target=cliProgress, args=(101, 20))
        cli_process.start()
        scan_process.start()
        #Wait until finished
        scan_process.join()
        cli_process.join()
        
        print("\n\t Results saved locally! Can be accessed by Option 2 on the command line... \n")
    except KeyboardInterrupt:
        print("\nscanNetwork: User stopped scan!!! Partial Data saved. Press enter to return to main program.")


def displayNetworkOptions(frequency_options):

    def exitNetworkOptions():
        display_on = False
        csv_operations.runTerminalInfraDir()
        #networkOptions()

    list_commands = """
    ############################################
    ####### FREQUENCY OPTIONS ##################
    ############################################\n
    Program commands:\n
    \t 0. Wifi (802.11 a/b/c/g/n/ac) - Scan a variety of wireless frequencies. \n
    \t 1. Bluetooth - Scan for nearby Bluetooth devices. Effective up to X meters. \n
    \t 2. Zigbee (802.15.4) - Scan for nearby Zigbee devices. Effective up to X meters. \n
    \t 3. LTE/GSM - Scan for wireless carrier devices. Effective up to X meters. \n
    \t (Q)uit - Quit this screen \n
    """

    #User Loop
    display_on = True

    #Available number options to execute commands

    options = OrderedDict((('0', partial(wifiScan, frequency_options)),
                           ('1', partial(bluScan, frequency_options)),
                           ('2', partial(zigbeeScan, frequency_options)),
                           ('3', partial(lteScan, frequency_options)),
                           ('Q', exitNetworkOptions),
                           ('q', exitNetworkOptions)))
                           

    #Mandatory First print out of commands
    print list_commands

    #Main Program Loop
    while display_on:
            try:
                    #Get user string
                    user_key_input = raw_input('Enter a number or (Q) to Quit: ').upper()
                    if user_key_input in options:
                            action = options[user_key_input]
                            action()
                    else:
                            print '\nUnknown User Input! Try Again!\n'
            except:
                    break


""" 1. Scan Network - Allow user to choose which frequencies they wish to scan """

def networkOptions():

    #Setup our "root" directory so anyone can call it
    frequency_options = csv_operations.getSourceDir()
    frequency_options += 'src/infrastructure/sdr_modules'

    print("\n\tChoose From the List of Available Frequencies... \n")

    #Call our ordered dictionary logic
    displayNetworkOptions(frequency_options)

    

    #csv_operations.runTerminalInfraDir()
    
if __name__ == "__main__":
    networkOptions()
