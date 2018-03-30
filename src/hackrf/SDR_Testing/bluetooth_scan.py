import subprocess
import signal
import os
from collections import OrderedDict
from time import sleep

write_file = "/tmp/bt_out.txt"
default_bt_freqs = OrderedDict([("0", 2.40e9), ("1", 2.42e9), ("2", 2.44e9), ("3", 2.46e9), ("4", 2.48e9), ("5", 2.410e9), ("6", 2.412e9), ("7", 2.414e9), ("8", 2.416e9), ("9", 2.418e9), ("10", 2.420e9), ("11", 2.40e9), ("12", 2.42e9), ("13", 2.44e9), ("14", 2.46e9), ("15", 2.48e9), ("16", 2.410e9), ("17", 2.412e9), ("18", 2.414e9), ("19", 2.416e9), ("20", 2.418e9), ("21", 2.420e9), ("22", 2.422e9), ("23", 2.424e9), ("24", 2.426e9), ("25", 2.428e9), ("26", 2.430e9), ("27", 2.432e9), ("28", 2.434e9), ("29", 2.436e9), ("30", 2.438e9), ("31", 2.440e9), ("32", 2.442e9), ("33", 2.444e9), ("34", 2.446e9), ("35", 2.448e9), ("36", 2.450e9), ("37", 2.402e9), ("38", 2.426e9), ("39", 2.480e9)])

def sleep_channel(channel_time, socketio, elapsed_time, total_packets, fp):
	num_updates = int(channel_time) * 2		#send two updates a second
	leftover_time = channel_time - int(channel_time)
	num = 0
	while (True):	#always run the update at least once
		if not os.path.isfile(fp):
			open(fp, 'a').close()
			
		fh = open(fp, 'r')
		lines = fh.readlines()
		fh.close()
		for line in lines:
			if "Pkt" not in line:
				continue
			parts = line.split()	
			if len(parts) > 3:
				num = int(parts[1].replace("Pkt", ""))
		socketio.emit('bt_count', {'msg': total_packets + num})
		socketio.emit('progress', {'msg': elapsed_time})
		if num_updates < 1:
			break
		else:
			elapsed_time += 0.5
			sleep(0.5)
			num_updates -= 1
	elapsed_time += leftover_time
	sleep(leftover_time)
	return elapsed_time, total_packets + num

#List of channels, int for time - run_bt_scan([37], 10)
def run_bt_scan(socketio=None, user_channels=[], send_updates=False, scan_time=120, elapsed_time=0, total_packets=0):
	scan_channels = OrderedDict()
	print(socketio, user_channels, send_updates, scan_time, elapsed_time, total_packets)
	if(len(user_channels) < 1):
		scan_channels = default_bt_freqs
	else:
		for ch in user_channels:
			try:
				scan_channels[ch] = default_bt_freqs[ch]
			except KeyError:
				pass
	if (len(scan_channels) > 0):
		channel_time = float(scan_time)/len(scan_channels)
		for ch in scan_channels:
			#THIS WILL ERASE EVERYTHING IN THE FILE FOR THE PREVIOUS CHANNEL
			cmd = "timeout " + str(channel_time) + " btle_rx -c " + ch + " > " + write_file
			p = subprocess.Popen(cmd, shell=True)
			if send_updates:
				socketio.emit('update', {'msg': "Bluetooth - Ch {}".format(ch)})
				elapsed_time, total_packets = sleep_channel(channel_time, socketio, elapsed_time, total_packets, write_file)
			else:
				print("\nSetting radio to Bluetooth - Ch {}".format(ch))
				sleep(channel_time)
			while not p.poll():
				try:
					sleep(0.5)
				except:
					p.terminate()

#			IF YOU WANT TO SAVE DATA, EXPORT IT HERE
#			with open(write_file) as f:
#				for line in f:
#					print(line.strip("\n"))
	
#run_bt_scan(user_channels=["37"], scan_time=10)	
