#!/usr/bin/python

from time import sleep
from wifi_rx_rftap_nox import run_wifi_scan
from zigbee_rftap_nox import run_zigbee_scan
from bluetooth_scan import run_bt_scan
from db_lib import *
from os import remove

wifi_24_options = {"user_channels": []}
wifi_5_options = {"user_channels": []}
zigbee_options = {"user_channels": []}
bluetooth_options = {"user_channels": []}

def scan_manager(scan_name, wifi_24_options=wifi_24_options, wifi_5_options=wifi_5_options, zigbee_options=zigbee_options, bluetooth_options=bluetooth_options, scan_time=60, socketio=None, send_updates=False):
	total_scan_time = 0
	if (send_updates):		#allows time for pretty animations
		sleep(4)
	num_scans = len(wifi_24_options['user_channels']) + len(wifi_5_options['user_channels']) + len(zigbee_options['user_channels']) + len(bluetooth_options['user_channels']) 
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
		if len(wifi_24_options['user_channels']) > 0:
			try:		#remove previous scans
				remove("/tmp/out_frames")
			except OSError:
				pass
			run_wifi_scan(user_channels=wifi_24_options['user_channels'],
										scan_time=scan_time*len(wifi_24_options['user_channels']),
										socketio=socketio,
										send_updates=send_updates,
										elapsed_time=total_scan_time)
			total_scan_time += scan_time*len(wifi_24_options['user_channels'])
			records = parse_wifi_records(job_id)
			insert_wifi_records(records)

		if len(wifi_5_options['user_channels']) > 0:
			try:		#remove previous scans
				remove("/tmp/out_frames")
			except OSError:
				pass
			run_wifi_scan(user_channels=wifi_5_options['user_channels'],
										scan_time=scan_time*len(wifi_5_options['user_channels']),
										socketio=socketio,
										send_updates=send_updates,
										elapsed_time=total_scan_time)
			total_scan_time += scan_time*len(wifi_5_options['user_channels'])
			records = parse_wifi_records(job_id)
			insert_wifi_records(records)

		if len(zigbee_options['user_channels']) > 0:
			try:		#remove previous scans
				remove("/tmp/zigbee_out.txt")
				remove("/tmp/zigbee.pcap")
			except OSError:
				pass
			run_zigbee_scan(user_channels=zigbee_options['user_channels'],
										scan_time=scan_time*len(zigbee_options['user_channels']),
										socketio=socketio,
										send_updates=send_updates,
										elapsed_time=total_scan_time)
			total_scan_time += scan_time*len(zigbee_options['user_channels'])
			records = parse_zb_records(job_id)
			insert_zb_records(records)

		if len(bluetooth_options['user_channels']) > 0:
			try:		#remove previous scans
				remove("/tmp/bt_out.txt")
			except OSError:
				pass
			run_bt_scan(user_channels=bluetooth_options['user_channels'],
										scan_time=scan_time*len(bluetooth_options['user_channels']),
										socketio=socketio,
										send_updates=send_updates,
										elapsed_time=total_scan_time)
			total_scan_time += scan_time*len(bluetooth_options['user_channels'])
			records = parse_bt_records(job_id)
			insert_bt_records(records)

		if (send_updates):
			socketio.emit('progress', {'msg': total_scan_time})
			socketio.emit('update', {'msg':"Done"})

	else:
		socketio.emit('update', {'msg':"No Scan"})
