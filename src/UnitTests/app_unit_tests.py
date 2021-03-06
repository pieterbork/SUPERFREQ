#!/usr/bin/env python2


#author : Kade Cooper kaco0964@colorado.edu
#name : app_unit_tests.py
#purpose : Run automated tests for terminal and flask environments. REWORK in progress
#date : 2018.03.29
#version: 1.5.12
#version notes (latest): Compatible w/ python2

import os
import unittest
import subprocess
import lib_for_unit_tests


class TestNetworkDevices(unittest.TestCase):

    def test_if_system_wireless_on(self):
        #DB info
        rowid = int(2)
        test = 'wifi_onboard'

        #Run Test and record within the database
        test_file = lib_for_unit_tests.wifi_onboard_path
        return_code = subprocess.call(test_file)
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
        test_file = lib_for_unit_tests.wifi_external_devices_path
        return_code = subprocess.call(test_file)
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
        test_file = lib_for_unit_tests.bluetooth_onboard_path
        return_code = subprocess.call(test_file)
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
        test_file = lib_for_unit_tests.bluetooth_external_devices_path
        return_code = subprocess.call(test_file)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False

    """ STRETCH GOAL WHICH REQUIRES SPECIAL HARDWARE AND COMMANDS NOT WIDELY AVAILABLE. MAYBE ONE DAY...

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

    """

    def test_internet_connectivity(self):
        #DB info
        rowid = int(10)
        test = 'ww_internet'

        #Run Test and record within the database
        test_file = lib_for_unit_tests.ww_internet_path
        return_code = subprocess.call(test_file)
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
        test_file = lib_for_unit_tests.hackrf_usb_path
        return_code = subprocess.call(test_file)
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

class TestInternalSystems(unittest.TestCase):

    def test_read_csv(self):
        #DB info
        rowid = int(12)
        test = 'read_csv'

        #Run Test and record within the database
        test_file = lib_for_unit_tests.read_csv_path
        return_code = subprocess.call(test_file)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False


    def test_copy_delete_csv(self):
        #DB info
        rowid = int(13)
        test = 'copy_delete_csv'

        #Run Test and record within the database
        test_file = lib_for_unit_tests.copy_delete_csv_path
        return_code = subprocess.call(test_file)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False

    def test_filter_csv(self):
        #DB info
        rowid = int(14)
        #This only tests Wifi...the most common test to be performed
        test = 'filter_csv'

        #Run Test and record within the database
        test_file = lib_for_unit_tests.csv_filter_path
        return_code = subprocess.call(test_file)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False


    def test_generate_graph(self):
        #DB info
        rowid = int(15)
        test = 'generate_graph'

        #Run Test and record within the database
        test_file = lib_for_unit_tests.generate_graph_path
        return_code = subprocess.call(test_file)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False

    def test_create_db(self):
        #DB info
        rowid = int(16)
        test = 'create_db'
        
        #Run Test and record within the database
        test_file = lib_for_unit_tests.create_empty_db_path
        return_code = subprocess.call(test_file)
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
        test_file = lib_for_unit_tests.create_table_in_db_path
        return_code = subprocess.call(test_file)
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
        test_file = lib_for_unit_tests.query_db_path
        return_code = subprocess.call(test_file)
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

        #Run Test and record within the database
        test_file = lib_for_unit_tests.import_csv_to_db_path
        return_code = subprocess.call(test_file)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False

    def test_export_csv_from_db(self):
        #DB info
        rowid = int(20)
        test = 'export_csv_from_db'

        #Run Test and record within the database
        test_file = lib_for_unit_tests.export_csv_from_db_path
        return_code = subprocess.call(test_file)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False

""" TESTS TO ADD FOR COMPLETE COVERAGE AT A LATER DATE

    def test_tkinter(self):
        #DB info
        rowid = int(21)
        test = 'tkinter'

        #Run Test and record within the database
        test_file = lib_for_unit_tests.tkinter_run_path
        return_code = subprocess.call(test_file)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False

    def test_flask(self):
        #DB info
        rowid = int(22)
        test = 'flask'
        #See here for more test cases: https://damyanon.net/post/flask-series-testing/

        #Run Test and record within the database
        test_file = lib_for_unit_tests.flask_run_path
        return_code = subprocess.call(test_file)
        if return_code == 0:
            boolean_value = int(1)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert True
        else:
            boolean_value = int(0)
            lib_for_unit_tests.statusTest(rowid, test, boolean_value)
            assert False
"""

""" 4. Automated Test Summary - Provide quick network/system checks in an easy to read format. Calls functions in sdr_module to increase file clarity """


def unitTestSummary():

    #21/23 Tests cases done!

    #First check if every bash, python file exists!
    lib_for_unit_tests.fileCheckListCaller()

    #Run our unit tests
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

##

if __name__ == '__main__':
    unitTestSummary()
    

#For handling multiple classes see: https://stackoverflow.com/questions/5360833/how-to-run-multiple-classes-in-single-test-suite-in-python-unit-testing
       
