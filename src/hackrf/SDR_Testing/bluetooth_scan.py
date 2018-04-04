import subprocess
import signal
import os
from collections import OrderedDict
from time import sleep

write_file = "/tmp/bt_out.txt"
default_bt_freqs = [2.40e9, 2.42e9, 2.44e9, 2.46e9, 2.48e9, 2.410e9, 2.412e9, 2.414e9, 2.416e9, 2.418e9, 2.420e9, 2.40e9, 2.42e9, 2.44e9, 2.46e9, 2.48e9, 2.410e9, 2.412e9, 2.414e9, 2.416e9, 2.418e9, 2.420e9, 2.422e9, 2.424e9, 2.426e9, 2.428e9, 2.430e9, 2.432e9, 2.434e9, 2.436e9, 2.438e9, 2.440e9, 2.442e9, 2.444e9, 2.446e9, 2.448e9, 2.450e9, 2.402e9, 2.426e9, 2.480e9]
channel_map = {2400000000.0: "0", 2420000000.0: "1", 2440000000.0: "2", 2460000000.0: "3", 2480000000.0: "4", 2410000000.0: "5", 2412000000.0: "6", 2414000000.0: "7", 2416000000.0: "8", 2418000000.0: "9", 2420000000.0: "10", 2400000000.0: "11", 2420000000.0: "12", 2440000000.0: "13", 2460000000.0: "14", 2480000000.0: "15", 2410000000.0: "16", 2412000000.0: "17", 2414000000.0: "18", 2416000000.0: "19", 2418000000.0: "20", 2420000000.0: "21", 2422000000.0: "22", 2424000000.0: "23", 2426000000.0: "24", 2428000000.0: "25", 2430000000.0: "26", 2432000000.0: "27", 2434000000.0: "28", 2436000000.0: "29", 2438000000.0: "30", 2440000000.0: "31", 2442000000.0: "32", 2444000000.0: "33", 2446000000.0: "34", 2448000000.0: "35", 2450000000.0: "36", 2402000000.0: "37", 2426000000.0: "38", 2480000000.0: "39"}


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
	scan_channels = []
	if(len(user_channels) < 1):
		scan_channels = default_bt_freqs
	else:
		for ch in user_channels:
			if float(ch) in default_bt_freqs:
				scan_channels.append(float(ch))
	if (len(scan_channels) > 0):
		channel_time = float(scan_time)/len(scan_channels)
		for ch in scan_channels:
			#THIS WILL ERASE EVERYTHING IN THE FILE FOR THE PREVIOUS CHANNEL
			cmd = "timeout " + str(channel_time) + " btle_rx -c " + channel_map[ch] + " > " + write_file
			p = subprocess.Popen(cmd, shell=True)
			if send_updates:
				socketio.emit('update', {'msg': "Bluetooth<br>Ch {}".format(channel_map[ch])})
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
