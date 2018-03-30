from flask import Flask,render_template,request
from flask_socketio import SocketIO,emit
from wifi_rx_rftap_nox import default_wifi_freqs
from zigbee_rftap_nox import default_zigbee_freqs
from bluetooth_scan import default_bt_freqs
from run_scans import scan_manager
import thread

app = Flask(__name__)
socketio = SocketIO(app, host="0.0.0.0")

@app.route('/scan', methods=["GET", "POST"])
def scan():
	if (request.method == "POST"):
		scan_time = 60
		try:
			scan_time = int(request.form['time'])
			if scan_time < 0:
				scan_time = 0
		except ValueError:
			pass
		kwargs = {"socketio":socketio,
							"send_updates": True,
							"scan_time": scan_time}
		user_wifi_channels = []
		user_zigbee_channels = []
		user_bt_channels = []
		if request.form['all_wifi'] == "1":
			user_wifi_channels = default_wifi_freqs.keys()
		else:
			form_wifi_freq_list = request.form.getlist('wifi_freq')
			form_wifi_freq_list.pop(0)		#to get rid of the placeholder that prevents flask errors
			for freq in form_wifi_freq_list:
				user_wifi_channels.append(freq)
		if request.form['all_zigbee'] == "1":
			user_zigbee_channels = default_zigbee_freqs.keys()
		else:
			form_zigbee_freq_list = request.form.getlist('zigbee_freq')
			form_zigbee_freq_list.pop(0)		#to get rid of the placeholder that prevents flask errors
			for freq in form_zigbee_freq_list:
				user_zigbee_channels.append(freq)
		if request.form['all_bt'] == "1":
			user_bt_channels = default_bt_freqs.keys()
		else:
			form_bt_freq_list = request.form.getlist('bt_freq')
			form_bt_freq_list.pop(0)		#to get rid of the placeholder that prevents flask errors
			for freq in form_bt_freq_list:
				user_bt_channels.append(freq)
		if len(user_wifi_channels) > 0:
			kwargs['wifi_options'] = {"user_channels":user_wifi_channels}
		if len(user_zigbee_channels) > 0:
			kwargs['zigbee_options'] = {"user_channels":user_zigbee_channels}
		if len(user_bt_channels) > 0:
			kwargs['bluetooth_options'] = {"user_channels":user_bt_channels}
		thread.start_new_thread(scan_manager, (), kwargs)
		return render_template("run_scan.html", scan_time=kwargs['scan_time'])
	elif (request.method == "GET"):
		return render_template("show_scan.html", default_wifi_freqs=default_wifi_freqs, default_zigbee_freqs=default_zigbee_freqs, default_bt_freqs=default_bt_freqs)

@app.route('/results')
def results():
	return render_template("results.html")

if __name__ == '__main__':
    app.run("0.0.0.0")	
