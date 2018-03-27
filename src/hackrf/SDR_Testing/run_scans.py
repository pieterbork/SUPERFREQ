#!/usr/bin/python

from wifi_rx_rftap_nox import run_wifi_scan
from zigbee_rftap_nox import run_zigbee_scan

run_wifi_scan(user_channels=["1", "2", "3"], scan_time=60)
run_zigbee_scan(user_channels=["11", "13", "15"], scan_time=47)
