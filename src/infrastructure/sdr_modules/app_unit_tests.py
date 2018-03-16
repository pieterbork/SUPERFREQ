#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : app_unit_tests.py
#purpose : Run automated tests for terminal and flask environments. REWORK in progress
#date : 2018.03.15
#version: 1.5.0
#version notes (latest): Compatible w/ python2

import unittest
import subprocess
import database_operations


class TestNetworkDevices(unittest.TestCase):

    def test_if_system_wireless_on(self):
        #DB info
        rowid = int(2)
        signal = 'wifi_system'

        #Run Test and record within the database
        test_directory = "./Shell_UnitTests/wifi_status.bash"
        return_code = subprocess.call(test_directory)
        if return_code == 0:
            boolean_value = int(1)
            database_operations.statusTest(rowid, signal, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            database_operations.statusTest(rowid, signal, boolean_value)
            assert False

    def test_if_wireless_external_devices_exist(self):
        #DB info
        rowid = int(3)
        signal = 'wifi_devices'

        #Run Test and record within the database
        test_directory = "./Shell_UnitTests/wifi_nearby_devices.bash"
        return_code = subprocess.call(test_directory)
        if return_code == 0:
            boolean_value = int(1)
            database_operations.statusTest(rowid, signal, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            database_operations.statusTest(rowid, signal, boolean_value)
            assert False
        

    def test_if_system_bluetooth_on(self):
        #DB info
        rowid = int(4)
        signal = 'bluetooth_system'

        #Run Test and record within the database
        test_directory = "./Shell_UnitTests/bluetooth_status.bash"
        return_code = subprocess.call(test_directory)
        if return_code == 0:
            boolean_value = int(1)
            database_operations.statusTest(rowid, signal, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            database_operations.statusTest(rowid, signal, boolean_value)
            assert False

    def test_if_bluetooth_external_devices_exist(self):
        #DB info
        rowid = int(5)
        signal = 'bluetooth_devices'

        #Run Test and record within the database
        test_directory = "./Shell_UnitTests/bluetooth_nearby_devices.bash"
        return_code = subprocess.call(test_directory)
        if return_code == 0:
            boolean_value = int(1)
            database_operations.statusTest(rowid, signal, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            database_operations.statusTest(rowid, signal, boolean_value)
            assert False

    #Note zigbee and xbee devices are virtually the same
    def test_if_zigbee_external_devices_exist(self):
        #TODO
        pass

    def test_if_lte_external_devices_exist(self):
        #TODO
        pass

    def test_internet_connectivity(self):
        #DB info
        rowid = int(8)
        signal = 'ww_internet'

        #Run Test and record within the database
        test_directory = "./Shell_UnitTests/internet_status.bash"
        return_code = subprocess.call(test_directory)
        if return_code == 0:
            boolean_value = int(1)
            database_operations.statusTest(rowid, signal, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            database_operations.statusTest(rowid, signal, boolean_value)
            assert False
    
class TestSdrHardware(unittest.TestCase):

    def test_usb(self):
        #DB info
        rowid = int(1)
        signal = 'HackRF'

        #Run Test and record within the database
        test_directory = "./Shell_UnitTests/usb_status.bash"
        return_code = subprocess.call(test_directory)
        if return_code == 0:
            boolean_value = int(1)
            database_operations.statusTest(rowid, signal, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            database_operations.statusTest(rowid, signal, boolean_value)
            assert False

    def test_sdr_rx(self):
        pass

class TestInternalSystems(unittest.TestCase):

    def test_read_csv(self):
        pass

    def test_flask(self):
        #See here for more test cases: https://damyanon.net/post/flask-series-testing/
        pass

    def test_db(self):
        pass

    def test_import(self):
        pass


"""
#Python library unittest will go here

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
"""

""" 4. Automated Test Summary - Provide quick network/system checks in an easy to read format. Calls functions in sdr_module to increase file clarity """

"""
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

##
"""
if __name__ == '__main__':
    # Run only the tests in the specified classes

    test_classes_to_run = [TestInternalSystems, TestSdrHardware, TestNetworkDevices]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(big_suite)

#For handling multiple classes see: https://stackoverflow.com/questions/5360833/how-to-run-multiple-classes-in-single-test-suite-in-python-unit-testing
       
