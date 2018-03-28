from flask import Flask,render_template,request
from flask_socketio import SocketIO,emit
from wifi_rx_rftap_nox import run_wifi_scan,default_wifi_freqs
import thread

app = Flask(__name__)
socketio = SocketIO(app, host="0.0.0.0")

@app.route('/')
def index():
	return render_template("index.html", default_wifi_freqs=default_wifi_freqs)

@app.route('/scan', methods=["POST"])
def scan():
	user_wifi_channels = []
	for freq in request.form.getlist('wifi_freq'):
		user_wifi_channels.append(freq)
	if len(user_wifi_channels) > 0:
		kwargs = {"socketio":socketio,
							"send_updates":True,
							"user_channels":user_wifi_channels,
							"scan_time":request.form['time']}
		thread.start_new_thread(run_wifi_scan, (), kwargs)
	return render_template("scan.html")

@app.route('/results')
def results():
	return render_template("results.html")
	
