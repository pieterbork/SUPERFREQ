#!/usr/bin/python
from random import sample
from collections import OrderedDict

default_wifi_freqs = OrderedDict([("1", 2.412e9), ("2", 2.417e9), ("3", 2.422e9), ("4", 2.427e9), ("5", 2.432e9), ("6", 2.437e9), ("7_24", 2.442e9), ("8_24", 2.447e9), ("9_24", 2.452e9), ("10", 2.457e9), ("11_24", 2.462e9), ("7_5", 5.035e9), ("8_5", 5.040e9), ("9_5", 5.045e9), ("11_5", 5.055e9), ("12", 5.060e9), ("16", 5.080e9), ("34", 5.170e9), ("36", 5.180e9), ("38", 5.190e9), ("40", 5.200e9), ("42", 5.210e9), ("44", 5.220e9), ("46", 5.230e9), ("48", 5.240e9), ("50", 5.250e9), ("52", 5.260e9), ("54", 5.270e9), ("56", 5.280e9), ("58", 5.290e9), ("60", 5.300e9), ("62", 5.310e9), ("64", 5.320e9), ("100", 5.500e9), ("102", 5.510e9), ("104", 5.520e9), ("106", 5.530e9), ("108", 5.540e9), ("110", 5.550e9), ("112", 5.560e9), ("114", 5.570e9), ("116", 5.580e9), ("118", 5.590e9), ("120", 5.600e9), ("122", 5.610e9), ("124", 5.620e9), ("126", 5.630e9), ("128", 5.640e9), ("132", 5.660e9), ("134", 5.670e9), ("136", 5.680e9), ("138", 5.690e9), ("140", 5.700e9), ("142", 5.710e9), ("144", 5.720e9), ("149", 5.745e9), ("151", 5.755e9), ("153", 5.765e9), ("155", 5.775e9), ("157", 5.785e9), ("159", 5.795e9), ("161", 5.805e9), ("165", 5.825e9)])
default_wifi_freqs_rev = OrderedDict([(2400000000.0, '0'), (2412000000.0, '1'), (2417000000.0, '2'), (2422000000.0, '3'), (2427000000.0, '4'), (2432000000.0, '5'), (2437000000.0, '6'), (2442000000.0, '7_24'), (2447000000.0, '8_24'), (2452000000.0, '9_24'), (2457000000.0, '10'), (2462000000.0, '11_24'), (5035000000.0, '7_5'), (5040000000.0, '8_5'), (5045000000.0, '9_5'), (5055000000.0, '11_5'), (5060000000.0, '12'), (5080000000.0, '16'), (5170000000.0, '34'), (5180000000.0, '36'), (5190000000.0, '38'), (5200000000.0, '40'), (5210000000.0, '42'), (5220000000.0, '44'), (5230000000.0, '46'), (5240000000.0, '48'), (5250000000.0, '50'), (5260000000.0, '52'), (5270000000.0, '54'), (5280000000.0, '56'), (5290000000.0, '58'), (5300000000.0, '60'), (5310000000.0, '62'), (5320000000.0, '64'), (5500000000.0, '100'), (5510000000.0, '102'), (5520000000.0, '104'), (5530000000.0, '106'), (5540000000.0, '108'), (5550000000.0, '110'), (5560000000.0, '112'), (5570000000.0, '114'), (5580000000.0, '116'), (5590000000.0, '118'), (5600000000.0, '120'), (5610000000.0, '122'), (5620000000.0, '124'), (5630000000.0, '126'), (5640000000.0, '128'), (5660000000.0, '132'), (5670000000.0, '134'), (5680000000.0, '136'), (5690000000.0, '138'), (5700000000.0, '140'), (5710000000.0, '142'), (5720000000.0, '144'), (5745000000.0, '149'), (5755000000.0, '151'), (5765000000.0, '153'), (5775000000.0, '155'), (5785000000.0, '157'), (5795000000.0, '159'), (5805000000.0, '161'), (5825000000.0, '165')])
all_wifi_freqs = {"2.4": [("1", 2.412e9), ("2", 2.417e9), ("3", 2.422e9), ("4", 2.427e9), ("5", 2.432e9), ("6", 2.437e9), ("7", 2.442e9), ("8", 2.447e9), ("9", 2.452e9), ("10", 2.457e9), ("11", 2.462e9)], "5": [("7", 5.035e9), ("8", 5.040e9), ("9", 5.045e9), ("11", 5.055e9), ("12", 5.060e9), ("16", 5.080e9), ("34", 5.170e9), ("36", 5.180e9), ("38", 5.190e9), ("40", 5.200e9), ("42", 5.210e9), ("44", 5.220e9), ("46", 5.230e9), ("48", 5.240e9), ("50", 5.250e9), ("52", 5.260e9), ("54", 5.270e9), ("56", 5.280e9), ("58", 5.290e9), ("60", 5.300e9), ("62", 5.310e9), ("64", 5.320e9), ("100", 5.500e9), ("102", 5.510e9), ("104", 5.520e9), ("106", 5.530e9), ("108", 5.540e9), ("110", 5.550e9), ("112", 5.560e9), ("114", 5.570e9), ("116", 5.580e9), ("118", 5.590e9), ("120", 5.600e9), ("122", 5.610e9), ("124", 5.620e9), ("126", 5.630e9), ("128", 5.640e9), ("132", 5.660e9), ("134", 5.670e9), ("136", 5.680e9), ("138", 5.690e9), ("140", 5.700e9), ("142", 5.710e9), ("144", 5.720e9), ("149", 5.745e9), ("151", 5.755e9), ("153", 5.765e9), ("155", 5.775e9), ("157", 5.785e9), ("159", 5.795e9), ("161", 5.805e9), ("165", 5.825e9)]}
default_zigbee_freqs = OrderedDict([("11", 2.405e9), ("12", 2.410e9), ("13", 2.415e9), ("14", 2.420e9), ("15", 2.425e9), ("16", 2.430e9), ("17", 2.435e9), ("18", 2.440e9), ("19", 2.445e9), ("20", 2.450e9), ("21", 2.455e9), ("22", 2.460e9), ("23", 2.465e9), ("24", 2.470e9), ("25", 2.475e9), ("26", 2.480e9)])
default_bt_freqs = OrderedDict([("0", 2.40e9), ("1", 2.42e9), ("2", 2.44e9), ("3", 2.46e9), ("4", 2.48e9), ("5", 2.410e9), ("6", 2.412e9), ("7", 2.414e9), ("8", 2.416e9), ("9", 2.418e9), ("10", 2.420e9), ("11", 2.40e9), ("12", 2.42e9), ("13", 2.44e9), ("14", 2.46e9), ("15", 2.48e9), ("16", 2.410e9), ("17", 2.412e9), ("18", 2.414e9), ("19", 2.416e9), ("20", 2.418e9), ("21", 2.420e9), ("22", 2.422e9), ("23", 2.424e9), ("24", 2.426e9), ("25", 2.428e9), ("26", 2.430e9), ("27", 2.432e9), ("28", 2.434e9), ("29", 2.436e9), ("30", 2.438e9), ("31", 2.440e9), ("32", 2.442e9), ("33", 2.444e9), ("34", 2.446e9), ("35", 2.448e9), ("36", 2.450e9), ("37", 2.402e9), ("38", 2.426e9), ("39", 2.480e9)])
colors_array = ["rgb(0,0,100)", "rgb(0,0,200)", "rgb(0,0,255)", "rgb(0,100,0)", "rgb(0,100,100)", "rgb(0,100,200)", "rgb(0,100,255)", "rgb(0,200,0)", "rgb(0,200,100)", "rgb(0,200,200)", "rgb(0,200,255)", "rgb(0,255,0)", "rgb(0,255,100)", "rgb(0,255,200)", "rgb(0,255,255)", "rgb(100,0,0)", "rgb(100,0,100)", "rgb(100,0,200)", "rgb(100,0,255)", "rgb(100,100,0)", "rgb(100,100,100)", "rgb(100,100,200)", "rgb(100,100,255)", "rgb(100,200,0)", "rgb(100,200,100)", "rgb(100,200,200)", "rgb(100,200,255)", "rgb(100,255,0)", "rgb(100,255,100)", "rgb(100,255,200)", "rgb(100,255,255)", "rgb(200,0,0)", "rgb(200,0,100)", "rgb(200,0,200)", "rgb(200,0,255)", "rgb(200,100,0)", "rgb(200,100,100)", "rgb(200,100,200)", "rgb(200,100,255)", "rgb(200,200,0)", "rgb(200,200,100)", "rgb(200,200,200)", "rgb(200,200,255)", "rgb(200,255,0)", "rgb(200,255,100)", "rgb(200,255,200)", "rgb(200,255,255)", "rgb(255,0,0)", "rgb(255,0,100)", "rgb(255,0,200)", "rgb(255,0,255)", "rgb(255,100,0)", "rgb(255,100,100)", "rgb(255,100,200)", "rgb(255,100,255)", "rgb(255,200,0)", "rgb(255,200,100)", "rgb(255,200,200)", "rgb(255,200,255)", "rgb(255,255,0)", "rgb(255,255,100)", "rgb(255,255,200)"]

def parse_wifi_channel(ch):
	if "_" in ch:
		ch_arr = ch.split("_")
		if ch_arr[1] == "5":
			return ch_arr[0] + " (5 GHz)"
		elif ch_arr[1] == "24":
			return ch_arr[0] + " (2.4 GHz)"
		else:
			return ch
	else:
		return ch

def generate_colors(length):
	return sample(colors_array, length)

def build_chart_js(type, records):
	if (type == "ssids_per_channel"):
		pie_chart = {}
		collect_counts = {}
		pie_chart['colors'], pie_chart['channel_names'], pie_chart['counts'] = [], [], []
		for record in records:
			freq = default_wifi_freqs_rev[float(record[5])*1e9]
			ssid = str(record[1])
			if freq in collect_counts:
				if ssid != "" and ssid != "N/A":
					collect_counts[freq].add(ssid)
			else:
				if ssid != "" and ssid != "N/A":
					collect_counts[freq] = set([ssid])
		for key in sorted(collect_counts.keys(), key=lambda x: int(x.split("_")[0])):
			pie_chart['channel_names'].append("Channel " + parse_wifi_channel(key))
			pie_chart['counts'].append(len(collect_counts[key]))
		pie_chart['colors'] = generate_colors(len(pie_chart['counts']))
		return pie_chart
	elif (type == "packets_per_channel"):
		bar_chart = {}
		collect_counts = {}
		bar_chart['colors'], bar_chart['channel_names'], bar_chart['counts'] = [], [], []
		for record in records:
			freq = default_wifi_freqs_rev[float(record[5])*1e9]
			count = int(record[6])
			try:
				collect_counts[freq] += count
			except KeyError:
				collect_counts[freq] = count
		for key in sorted(collect_counts.keys(), key=lambda x: int(x.split("_")[0])):
			bar_chart['channel_names'].append("Channel " + parse_wifi_channel(key))
			bar_chart['counts'].append(collect_counts[key])
		bar_chart['colors'] = generate_colors(len(bar_chart['counts']))
		return bar_chart

def build_unique_ssids_table(records):
	ssids = {}
	for record in records:
		if record[1] != "" and record[1] != "N/A" and not(((record[1], parse_wifi_channel(default_wifi_freqs_rev[float(record[5])*1e9])) in ssids)):
			try:
				ssids[str(record[1])].add(parse_wifi_channel(default_wifi_freqs_rev[float(record[5])*1e9]))
			except:
				ssids[str(record[1])] = set([parse_wifi_channel(default_wifi_freqs_rev[float(record[5])*1e9])])
	for ssid in ssids:
		ssids[ssid] = ", ".join(sorted(ssids[ssid], key=lambda x: int(x.split()[0])))
	return ssids

def build_top_talkers_table(records):
	top_talkers = {}
	for record in records:
		freq = default_wifi_freqs_rev[float(record[5])*1e9]
		macs = [str(record[2]), str(record[3]), str(record[4])]
		if not(freq in top_talkers):
			top_talkers[freq] = {}
		for mac in macs:
			if mac != "ff:ff:ff:ff:ff:ff" and not("XX" in mac):
				if mac in top_talkers[freq]:
					top_talkers[freq][mac] += record[6]
				else:
					top_talkers[freq][mac] = record[6]
	for ch in top_talkers:
		top_talkers[ch] = [(key, top_talkers[ch][key]) for key in sorted(top_talkers[ch].keys(), key=lambda x: top_talkers[ch][x], reverse=True)]
	ordered_talkers_list = [(ch, "Ch " + parse_wifi_channel(ch), top_talkers[ch]) for ch in sorted(top_talkers.keys(), key=lambda x: int(x.split("_")[0]))]
	return ordered_talkers_list

