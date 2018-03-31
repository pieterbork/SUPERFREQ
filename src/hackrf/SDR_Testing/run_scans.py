#!/usr/bin/python

from time import sleep
from wifi_rx_rftap_nox import run_wifi_scan
from zigbee_rftap_nox import run_zigbee_scan
from bluetooth_scan import run_bt_scan
from db_lib import *

wifi_options = {"user_channels": []}
zigbee_options = {"user_channels": []}
bluetooth_options = {"user_channels": []}

def scan_manager(scan_name, wifi_options=wifi_options, zigbee_options=zigbee_options, bluetooth_options=bluetooth_options, scan_time=60, socketio=None, send_updates=False):
	total_scan_time = 0
	if (send_updates):		#allows time for pretty animations
		sleep(4)
	num_scans = len(wifi_options['user_channels']) + len(zigbee_options['user_channels']) + len(bluetooth_options['user_channels'])
	if num_scans > 0:
		### Set up the database
		create_wifi_table()
		create_zb_table()
		create_bt_table()
		create_job_table()
		insert_job(scan_name)
		job_id = get_job_id(scan_name)

		### Run the Scans, parsing data after each scan
		scan_time = float(scan_time)/float(num_scans)
		if len(wifi_options['user_channels']) > 0:
			run_wifi_scan(user_channels=wifi_options['user_channels'],
										scan_time=scan_time*len(wifi_options['user_channels']),
										socketio=socketio,
										send_updates=send_updates,
										elapsed_time=total_scan_time)
			total_scan_time += scan_time*len(wifi_options['user_channels'])
			records = parse_wifi_records(job_id)
			insert_wifi_records(records)

		if len(zigbee_options['user_channels']) > 0:
			run_zigbee_scan(user_channels=zigbee_options['user_channels'],
										scan_time=scan_time*len(zigbee_options['user_channels']),
										socketio=socketio,
										send_updates=send_updates,
										elapsed_time=total_scan_time)
			total_scan_time += scan_time*len(zigbee_options['user_channels'])
			records = parse_bt_records(job_id)
			insert_bt_records(records)

		if len(bluetooth_options['user_channels']) > 0:
			run_bt_scan(user_channels=bluetooth_options['user_channels'],
										scan_time=scan_time*len(bluetooth_options['user_channels']),
										socketio=socketio,
										send_updates=send_updates,
										elapsed_time=total_scan_time)
			total_scan_time += scan_time*len(bluetooth_options['user_channels'])
			records = parse_zb_records(job_id)
			insert_zb_records(records)

		if (send_updates):
			socketio.emit('progress', {'msg': total_scan_time})
			socketio.emit('update', {'msg':"Done"})

	else:
		socketio.emit('update', {'msg':"No Scan"})
