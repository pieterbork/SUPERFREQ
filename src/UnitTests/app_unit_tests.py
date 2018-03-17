#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : app_unit_tests.py
#purpose : Run automated tests for terminal and flask environments. REWORK in progress
#date : 2018.03.16
#version: 1.5.0
#version notes (latest): Compatible w/ python2

import unittest
import subprocess
import lib_for_unit_tests


class TestNetworkDevices(unittest.TestCase):

    def test_if_system_wireless_on(self):
        #DB info
        rowid = int(2)
        test = 'wifi_onboard'

        #Run Test and record within the database
        test_directory = "./Network_Devices_UnitTests/wifi_status.bash"
        return_code = subprocess.call(test_directory)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False

    def test_if_wireless_external_devices_exist(self):
        #DB info
        rowid = int(3)
        test = 'wifi_external_devices'

        #Run Test and record within the database
        test_directory = "./Network_Devices_UnitTests/wifi_nearby_devices.bash"
        return_code = subprocess.call(test_directory)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False
        

    def test_if_system_bluetooth_on(self):
        #DB info
        rowid = int(4)
        test = 'bluetooth_onboard'

        #Run Test and record within the database
        test_directory = "./Network_Devices_UnitTests/bluetooth_status.bash"
        return_code = subprocess.call(test_directory)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False

    def test_if_bluetooth_external_devices_exist(self):
        #DB info
        rowid = int(5)
        test = 'bluetooth_external_devices'

        #Run Test and record within the database
        test_directory = "./Network_Devices_UnitTests/bluetooth_nearby_devices.bash"
        return_code = subprocess.call(test_directory)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False

    def test_if_system_zigbee_on(self):
        #DB info
        rowid = int(6)
        test = 'zigbee_onboard'
        
        #TODO
        pass

    #Note zigbee and xbee devices are virtually the same
    def test_if_zigbee_external_devices_exist(self):
        #DB info
        rowid = int(7)
        test = 'zigbee_external_devices'
        
        #TODO
        pass

    def test_if_system_lte_on(self):
        #DB info
        rowid = int(8)
        test = 'lte_onboard'
        
        #TODO
        pass

    def test_if_lte_external_devices_exist(self):
        #DB info
        rowid = int(9)
        test = 'lte_external_devices'
        
        #TODO
        pass

    def test_internet_connectivity(self):
        #DB info
        rowid = int(10)
        test = 'ww_internet'

        #Run Test and record within the database
        test_directory = "./Network_Devices_UnitTests/internet_status.bash"
        return_code = subprocess.call(test_directory)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False
    
class TestSdrHardware(unittest.TestCase):

    def test_hackrf_usb(self):
        #DB info
        rowid = int(1)
        test = 'hackrf_usb'

        #Run Test and record within the database
        test_directory = "./SDR_UnitTests/usb_status.bash"
        return_code = subprocess.call(test_directory)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False

    #Will include a script to save output
    def test_sdr_rx(self):
        #DB info
        rowid = int(11)
        test = 'hackrf_rx'
        pass

    #Will include a script to save output
    def test_sdr_tx(self):
        #DB info
        rowid = int(12)
        test = 'hackrf_tx'
        pass

class TestInternalSystems(unittest.TestCase):

    def test_read_csv(self):
        #DB info
        rowid = int(12)
        test = 'read_csv'
        pass

    def test_copy_delete_csv(self):
        #DB info
        rowid = int(13)
        test = 'copy_delete_csv'
        pass

    def test_filter_csv(self):
        #DB info
        rowid = int(14)
        test = 'filter_csv'
        pass

    def test_generate_graph(self):
        #DB info
        rowid = int(15)
        test = 'generate_graph'
        pass

    def test_create_db(self):
        #DB info
        rowid = int(16)
        test = 'create_db'
        
        #Run Test and record within the database
        test_directory = "./Infrastructure_UnitTests/database_operations/create_empty_db.bash"
        return_code = subprocess.call(test_directory)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False

    def test_create_table_in_db(self):
        #DB info
        rowid = int(17)
        test = 'create_table_in_db'

        #Run Test and record within the database
        test_directory = "./Infrastructure_UnitTests/database_operations/create_table_in_db.py"
        return_code = subprocess.call(test_directory)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False

    def test_query_db(self):
        #DB info
        rowid = int(18)
        test = 'query_db'

        #Run Test and record within the database
        test_directory = "./Infrastructure_UnitTests/database_operations/query_db.py"
        return_code = subprocess.call(test_directory)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False

    def test_import_csv_to_db(self):
        #DB info
        rowid = int(19)
        test = 'import_csv_to_db'
        pass

    def test_export_csv_from_db(self):
        #DB info
        rowid = int(20)
        test = 'export_csv_from_db'
        pass

    def test_tkinter(self):
        #DB info
        rowid = int(21)
        test = 'tkinter'
        pass

    def test_flask(self):
        #DB info
        rowid = int(22)
        test = 'flask'
        #See here for more test cases: https://damyanon.net/post/flask-series-testing/
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

    #Run cleanup function
    lib_for_unit_tests.cleanUpTestDir()

#For handling multiple classes see: https://stackoverflow.com/questions/5360833/how-to-run-multiple-classes-in-single-test-suite-in-python-unit-testing
       
