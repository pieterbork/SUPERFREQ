from flask import Flask,render_template
from flask_socketio import SocketIO,emit
from wifi_rx_rftap_nox import run_wifi_scan
import thread

app = Flask(__name__)
socketio = SocketIO(app, host="0.0.0.0")

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/scan')
def scan():
	#thread.start_new_thread(run_wifi_scan, (), {"socketio":socketio,"send_updates":True})
	return render_template("scan.html")
	
