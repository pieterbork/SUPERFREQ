#!/usr/bin/python

from time import sleep
from wifi_rx_rftap_nox import run_wifi_scan
from zigbee_rftap_nox import run_zigbee_scan

wifi_options = {"user_channels": []}
zigbee_options = {"user_channels": []}

def scan_manager(wifi_options=wifi_options, zigbee_options=zigbee_options, scan_time=60, socketio=None, send_updates=False):
	if (send_updates):		#allows time for pretty animations
		sleep(4)
	if (len(wifi_options['user_channels']) and len(zigbee_options['user_channels'])):
		scan_time /= 2
	if len(wifi_options['user_channels']) > 0:
		run_wifi_scan(user_channels=wifi_options['user_channels'],
									scan_time=scan_time,
									socketio=socketio,
									send_updates=send_updates)
	if len(zigbee_options['user_channels']) > 0:
		run_zigbee_scan(user_channels=zigbee_options['user_channels'],
									scan_time=scan_time,
									socketio=socketio,
									send_updates=send_updates)
	if (send_updates):
		socketio.emit('update', {'msg':"Done"})



#run_wifi_scan(user_channels=["1", "2", "3"], scan_time=60)
#run_zigbee_scan(user_channels=["11", "13", "15"], scan_time=47)
