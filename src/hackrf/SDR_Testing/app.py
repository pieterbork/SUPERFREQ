from flask import Flask,render_template,request
from flask_socketio import SocketIO,emit
from run_scans import scan_manager
import thread
from time import time,strftime
import db_lib
from random import randrange
import datetime
from collections import OrderedDict

app = Flask(__name__)
socketio = SocketIO(app, host="0.0.0.0")

default_wifi_freqs = OrderedDict([("1", 2.412e9), ("2", 2.417e9), ("3", 2.422e9), ("4", 2.427e9), ("5", 2.432e9), ("6", 2.437e9), ("7_24", 2.442e9), ("8_24", 2.447e9), ("9_24", 2.452e9), ("10", 2.457e9), ("11_24", 2.462e9), ("7_5", 5.035e9), ("8_5", 5.040e9), ("9_5", 5.045e9), ("11_5", 5.055e9), ("12", 5.060e9), ("16", 5.080e9), ("34", 5.170e9), ("36", 5.180e9), ("38", 5.190e9), ("40", 5.200e9), ("42", 5.210e9), ("44", 5.220e9), ("46", 5.230e9), ("48", 5.240e9), ("50", 5.250e9), ("52", 5.260e9), ("54", 5.270e9), ("56", 5.280e9), ("58", 5.290e9), ("60", 5.300e9), ("62", 5.310e9), ("64", 5.320e9), ("100", 5.500e9), ("102", 5.510e9), ("104", 5.520e9), ("106", 5.530e9), ("108", 5.540e9), ("110", 5.550e9), ("112", 5.560e9), ("114", 5.570e9), ("116", 5.580e9), ("118", 5.590e9), ("120", 5.600e9), ("122", 5.610e9), ("124", 5.620e9), ("126", 5.630e9), ("128", 5.640e9), ("132", 5.660e9), ("134", 5.670e9), ("136", 5.680e9), ("138", 5.690e9), ("140", 5.700e9), ("142", 5.710e9), ("144", 5.720e9), ("149", 5.745e9), ("151", 5.755e9), ("153", 5.765e9), ("155", 5.775e9), ("157", 5.785e9), ("159", 5.795e9), ("161", 5.805e9), ("165", 5.825e9)])
all_wifi_freqs = {"2.4": [("1", 2.412e9), ("2", 2.417e9), ("3", 2.422e9), ("4", 2.427e9), ("5", 2.432e9), ("6", 2.437e9), ("7", 2.442e9), ("8", 2.447e9), ("9", 2.452e9), ("10", 2.457e9), ("11", 2.462e9)], "5": [("7", 5.035e9), ("8", 5.040e9), ("9", 5.045e9), ("11", 5.055e9), ("12", 5.060e9), ("16", 5.080e9), ("34", 5.170e9), ("36", 5.180e9), ("38", 5.190e9), ("40", 5.200e9), ("42", 5.210e9), ("44", 5.220e9), ("46", 5.230e9), ("48", 5.240e9), ("50", 5.250e9), ("52", 5.260e9), ("54", 5.270e9), ("56", 5.280e9), ("58", 5.290e9), ("60", 5.300e9), ("62", 5.310e9), ("64", 5.320e9), ("100", 5.500e9), ("102", 5.510e9), ("104", 5.520e9), ("106", 5.530e9), ("108", 5.540e9), ("110", 5.550e9), ("112", 5.560e9), ("114", 5.570e9), ("116", 5.580e9), ("118", 5.590e9), ("120", 5.600e9), ("122", 5.610e9), ("124", 5.620e9), ("126", 5.630e9), ("128", 5.640e9), ("132", 5.660e9), ("134", 5.670e9), ("136", 5.680e9), ("138", 5.690e9), ("140", 5.700e9), ("142", 5.710e9), ("144", 5.720e9), ("149", 5.745e9), ("151", 5.755e9), ("153", 5.765e9), ("155", 5.775e9), ("157", 5.785e9), ("159", 5.795e9), ("161", 5.805e9), ("165", 5.825e9)]}
default_zigbee_freqs = OrderedDict([("11", 2.405e9), ("12", 2.410e9), ("13", 2.415e9), ("14", 2.420e9), ("15", 2.425e9), ("16", 2.430e9), ("17", 2.435e9), ("18", 2.440e9), ("19", 2.445e9), ("20", 2.450e9), ("21", 2.455e9), ("22", 2.460e9), ("23", 2.465e9), ("24", 2.470e9), ("25", 2.475e9), ("26", 2.480e9)])
default_bt_freqs = OrderedDict([("0", 2.40e9), ("1", 2.42e9), ("2", 2.44e9), ("3", 2.46e9), ("4", 2.48e9), ("5", 2.410e9), ("6", 2.412e9), ("7", 2.414e9), ("8", 2.416e9), ("9", 2.418e9), ("10", 2.420e9), ("11", 2.40e9), ("12", 2.42e9), ("13", 2.44e9), ("14", 2.46e9), ("15", 2.48e9), ("16", 2.410e9), ("17", 2.412e9), ("18", 2.414e9), ("19", 2.416e9), ("20", 2.418e9), ("21", 2.420e9), ("22", 2.422e9), ("23", 2.424e9), ("24", 2.426e9), ("25", 2.428e9), ("26", 2.430e9), ("27", 2.432e9), ("28", 2.434e9), ("29", 2.436e9), ("30", 2.438e9), ("31", 2.440e9), ("32", 2.442e9), ("33", 2.444e9), ("34", 2.446e9), ("35", 2.448e9), ("36", 2.450e9), ("37", 2.402e9), ("38", 2.426e9), ("39", 2.480e9)])


@app.route('/', methods=["GET"])
def dash():
	jobs = db_lib.get_records_from_table("Jobs")
	
	return render_template("dashboard.html", jobs=jobs)

@app.route('/scan', methods=["GET", "POST"])
def scan():
	if (request.method == "POST"):
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
