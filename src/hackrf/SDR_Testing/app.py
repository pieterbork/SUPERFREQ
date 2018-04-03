from flask import Flask,render_template,request
from flask_socketio import SocketIO,emit
from run_scans import scan_manager
import thread
from time import time,strftime
import db_lib
from random import randrange
import datetime

app = Flask(__name__)
socketio = SocketIO(app, host="0.0.0.0")


@app.route('/', methods=["GET"])
def dash():
	jobs = db_lib.get_records_from_table("Jobs")
	
	return render_template("dashboard.html", jobs=jobs)

@app.route('/scan', methods=["GET", "POST"])
def scan():
	if (request.method == "POST"):
		print(request.form)
		user_wifi_24_channels = []
		user_wifi_5_channels = []
		user_zigbee_channels = []
		user_bt_channels = []
		scan_time = 60
		try:
			scan_time = int(request.form['scan_time'])
			if scan_time < 0:
				scan_time = 0
		except ValueError:
			pass
		job_name = strftime("%Y-%m-%d_%H:%M:%S")
		if request.form['scan_name'] != "":
			job_name = str(request.form['scan_name'])	#TODO: sanitize this

		kwargs = {"socketio":socketio,
							"send_updates": True,
							"scan_time": scan_time,
							"scan_name": job_name}

		form_wifi_24_freq_list = request.form.getlist('wifi_select_24')
		form_wifi_24_freq_list.pop(0)		#to get rid of the placeholder that prevents flask errors
		for freq in form_wifi_24_freq_list:
			user_wifi_24_channels.append(freq)

		form_wifi_5_freq_list = request.form.getlist('wifi_select_5')
		form_wifi_5_freq_list.pop(0)		#to get rid of the placeholder that prevents flask errors
		for freq in form_wifi_5_freq_list:
			user_wifi_5_channels.append(freq)

		form_zigbee_freq_list = request.form.getlist('zigbee_select_24')
		form_zigbee_freq_list.pop(0)		#to get rid of the placeholder that prevents flask errors
		for freq in form_zigbee_freq_list:
			user_zigbee_channels.append(freq)

		form_bt_freq_list = request.form.getlist('bluetooth_select_24')
		form_bt_freq_list.pop(0)		#to get rid of the placeholder that prevents flask errors
		for freq in form_bt_freq_list:
			user_bt_channels.append(freq)

		if len(user_wifi_24_channels) > 0:
			kwargs['wifi_24_options'] = {"user_channels":user_wifi_24_channels}
		if len(user_wifi_5_channels) > 0:
			kwargs['wifi_5_options'] = {"user_channels":user_wifi_5_channels}
		if len(user_zigbee_channels) > 0:
			kwargs['zigbee_options'] = {"user_channels":user_zigbee_channels}
		if len(user_bt_channels) > 0:
			kwargs['bluetooth_options'] = {"user_channels":user_bt_channels}

		thread.start_new_thread(scan_manager, (), kwargs)
		return render_template("run_scan.html", 
					scan_time=kwargs['scan_time'],
					job=job_name)

	elif (request.method == "GET"):
		defaults = {
			"scan_name": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
			"scan_time": 60,
			"Wifi2.4": [1, 6, 11],
			"Wifi5": [],
			"Bluetooth2.4": [37],
			"Zigbee2.4": [15, 20, 25, 26]
		}
		default_other_freqs = {
			"Zigbee": default_zigbee_freqs,
			"Bluetooth": default_bt_freqs
		}
		protocols = [("Wifi", "2.4", "wifi_select_24"), 
					 ("Wifi", "5", "wifi_select_5"), 
					 ("Bluetooth", "2.4", "bluetooth_select_24"), 
					 ("Zigbee", "2.4", "zigbee_select_24")]
		return render_template("show_scan.html", 
					default_bt_freqs=default_bt_freqs,
					all_wifi_freqs=all_wifi_freqs,
					default_other_freqs=default_other_freqs,
					defaults=defaults,
					protocols=protocols)

@app.route('/results/<job>')
def results(job):
	job_id = db_lib.get_job_id(job)
	wifi_records = db_lib.get_records_from_table("Wifi", job_id)	
	zigbee_records = db_lib.get_records_from_table("Zigbee", job_id)	
	bt_records = db_lib.get_records_from_table("Bluetooth", job_id)	
	channels = {}
	for record in wifi_records:
		try:
			channels[default_wifi_freqs_rev[float(record[5])*1e9]] += 1
		except KeyError:
			channels[default_wifi_freqs_rev[float(record[5])*1e9]] = 1
	channel_names = ["Channel " + key for key in channels.keys()]
	channel_colors = []
	for i in range(0, len(channel_names)):
		channel_colors.append("rgb({0}, {1}, {2})".format(randrange(0, 255), randrange(0, 255), randrange(0, 255)))
	
	return render_template("results.html", 
				records={
					"Wifi":sorted(wifi_records, key=lambda x: x[6], reverse=True),
					"Wifi_fields": ["SSID", "MAC 1", "MAC 2", "MAC 3", "Frequency", "Count"],
					"Zigbee":sorted(zigbee_records, key=lambda x: x[7], reverse=True), 
					"Zigbee_fields": ["Source", "Destination", "Ext Source", "Ext Dest", "Sec Source", "Sec Dest", "Count"],
					"Bluetooth":sorted(bt_records, key=lambda x: x[3], reverse=True),
					"Bluetooth_fields": ["Channel", "MAC", "Count"],
					"protocols": ["Wifi", "Zigbee", "Bluetooth"]
				}, 
				channels=channel_names, 
				channel_counts=channels.values(), 
				channel_colors=channel_colors,
				job=job)

if __name__ == '__main__':
    app.run("0.0.0.0")	
