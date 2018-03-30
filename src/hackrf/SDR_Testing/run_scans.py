#!/usr/bin/python

from time import sleep
from wifi_rx_rftap_nox import run_wifi_scan
from zigbee_rftap_nox import run_zigbee_scan
from bluetooth_scan import run_bt_scan

wifi_options = {"user_channels": []}
zigbee_options = {"user_channels": []}
bluetooth_options = {"user_channels": []}

def scan_manager(wifi_options=wifi_options, zigbee_options=zigbee_options, bluetooth_options=bluetooth_options, scan_time=60, socketio=None, send_updates=False, scan_name):
	total_scan_time = 0
	if (send_updates):		#allows time for pretty animations
		sleep(4)
	num_scans = len(wifi_options['user_channels']) + len(zigbee_options['user_channels']) + len(bluetooth_options['user_channels'])
	if num_scans > 0:
		scan_time /= num_scans
		if len(wifi_options['user_channels']) > 0:
			run_wifi_scan(user_channels=wifi_options['user_channels'],
										scan_time=scan_time*len(wifi_options['user_channels']),
										socketio=socketio,
										send_updates=send_updates,
										elapsed_time=total_scan_time)
			total_scan_time += scan_time*len(wifi_options['user_channels'])

		if len(zigbee_options['user_channels']) > 0:
			run_zigbee_scan(user_channels=zigbee_options['user_channels'],
										scan_time=scan_time*len(zigbee_options['user_channels']),
										socketio=socketio,
										send_updates=send_updates,
										elapsed_time=total_scan_time)
			total_scan_time += scan_time*len(zigbee_options['user_channels'])

		if len(bluetooth_options['user_channels']) > 0:
			print(bluetooth_options['user_channels'],scan_time,total_scan_time)
			run_bt_scan(user_channels=bluetooth_options['user_channels'],
										scan_time=scan_time*len(bluetooth_options['user_channels']),
										socketio=socketio,
										send_updates=send_updates,
										elapsed_time=total_scan_time)
			total_scan_time += scan_time*len(bluetooth_options['user_channels'])

		if (send_updates):
			socketio.emit('progress', {'msg': total_scan_time})
			socketio.emit('update', {'msg':"Done"})
	else:
		socketio.emit('update', {'msg':"No Scan"})
