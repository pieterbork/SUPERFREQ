import subprocess
import signal
import time
import os

write_file = "bt_out.txt"

def get_num_recs(fp):
	if not os.path.isfile(fp):
		open(fp, 'a').close()
		
	num = None
	fh = open(fp, 'r')
	lines = fh.readlines()
	fh.close()
	for line in lines:
		if "Pkt" not in line:
			continue
		parts = line.split()	
		if len(parts) > 3:
			num = parts[1][-2:]
	
	return num

#List of channels, int for time - run_bt_scan([37], 10)
def run_bt_scan(channels, duration):
	for channel in channels:
		#THIS WILL ERASE EVERYTHING IN THE FILE FOR THE PREVIOUS CHANNEL
		cmd = "timeout " + str(duration) + " btle_rx -c " + str(channel) + " > " + write_file
		p = subprocess.Popen(cmd, shell=True)
		while not p.poll():
			try:
				print(get_num_recs(write_file))
				time.sleep(0.5)
			except:
				p.terminate()
		#IF YOU WANT TO SAVE DATA, EXPORT IT HERE
		print(get_num_recs(write_file))
	
run_bt_scan([37], 10)	
