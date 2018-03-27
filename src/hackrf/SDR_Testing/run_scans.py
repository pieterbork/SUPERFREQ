#!/usr/bin/python

import argparse,time,atexit
from collections import OrderedDict

default_wifi_freqs = OrderedDict([("1", 2.412e9), ("2", 2.417e9), ("3", 2.422e9), ("4", 2.427e9), ("5", 2.432e9), ("6", 2.437e9), ("7_24", 2.442e9), ("8_24", 2.447e9), ("9_24", 2.452e9), ("10", 2.457e9), ("11_24", 2.462e9), ("7_5", 5.035e9), ("8_5", 5.040e9), ("9_5", 5.045e9), ("11_5", 5.055e9), ("12", 5.060e9), ("16", 5.080e9), ("34", 5.170e9), ("36", 5.180e9), ("38", 5.190e9), ("40", 5.200e9), ("42", 5.210e9), ("44", 5.220e9), ("46", 5.230e9), ("48", 5.240e9), ("50", 5.250e9), ("52", 5.260e9), ("54", 5.270e9), ("56", 5.280e9), ("58", 5.290e9), ("60", 5.300e9), ("62", 5.310e9), ("64", 5.320e9), ("100", 5.500e9), ("102", 5.510e9), ("104", 5.520e9), ("106", 5.530e9), ("108", 5.540e9), ("110", 5.550e9), ("112", 5.560e9), ("114", 5.570e9), ("116", 5.580e9), ("118", 5.590e9), ("120", 5.600e9), ("122", 5.610e9), ("124", 5.620e9), ("126", 5.630e9), ("128", 5.640e9), ("132", 5.660e9), ("134", 5.670e9), ("136", 5.680e9), ("138", 5.690e9), ("140", 5.700e9), ("142", 5.710e9), ("144", 5.720e9), ("149", 5.745e9), ("151", 5.755e9), ("153", 5.765e9), ("155", 5.775e9), ("157", 5.785e9), ("159", 5.795e9), ("161", 5.805e9), ("165", 5.825e9)])

default_zigbee_freqs = OrderedDict([("11", 2.405e9), ("12", 2.410e9), ("13", 2.415e9), ("14", 2.420e9), ("15", 2.425e9), ("16", 2.430e9), ("17", 2.435e9), ("18", 2.440e9), ("19", 2.445e9), ("20", 2.450e9), ("21", 2.455e9), ("22", 2.460e9), ("23", 2.465e9), ("2.4", 2.470e9), ("25", 2.475e9), ("26", 2.480e9)])

parser = argparse.ArgumentParser(description="Run different SUPERFREQ scans")
parser.add_argument("-w", action="store_true", default=False, help="Run wifi scan")
parser.add_argument("--wch", default="", help="A comma separated list of wifi channel numbers, default is all channels, channels 7,8,9,&11 must be differentiated between 2.4 and 5 GHz (e.g. 7_24 for 2.4 GHz channel 7 and 7_5 for 5 GHz channel 7), unknown channels will be ignored")
parser.add_argument("-z", action="store_true", default=False, help="Run zigbee scan")
parser.add_argument("--zch", default="", help="A comma separated list of zigbee channel numbers, default is all channels, unknown channels will be ignored")
parser.add_argument("-t", default=30, type=float, help="Total scan time in seconds, default is 30 seconds")
args = parser.parse_args()

if (args.w and args.z):
	args.t /= 2

def display_wifi_channel(ch):
	ghz = ""
	channel_num = ""
	if "_" in ch:
		tmp = ch.split("_")
		if (tmp[1] == "24"):
			channel_num = tmp[0]
			ghz = "2.4"
		elif (tmp[1] == "5"):
			channel_num = tmp[0]
			ghz = "5"
		else:
			return "error - {}".format(ch)
	elif (int(ch) < 11):
		channel_num = ch
		ghz = "2.4"
	elif (int(ch) > 11):
		channel_num = ch
		ghz = "5"
	else:
		return "error - {}".format(ch)
	return "WiFi - {0} GHz Channel {1}".format(ghz, channel_num)

if args.w:
	from wifi_rx_rftap_nox import wifi_rx_rftap_nox		#import must be here to reset SDR for multiple scans
	scan_channels = OrderedDict()
	if(args.wch == ""):
		scan_channels = default_wifi_freqs
	else:
		for ch in args.wch.split(","):
			try:
				scan_channels[ch] = default_wifi_freqs[ch]
			except KeyError:
				pass
	if(len(scan_channels) > 0):
		wifi_tb = wifi_rx_rftap_nox()
		wifi_tb.start()
		for ch in scan_channels:
			print("\n\nSetting radio to {}".format(display_wifi_channel(ch)))
			wifi_tb.set_freq(scan_channels[ch])
			time.sleep(float(args.t)/len(scan_channels))
		wifi_tb.stop()
		wifi_tb.wait()

if args.z:
	from zigbee_rftap_nox import zigbee_rftap_nox		#import must be here to reset SDR for multiple scans
	from zigbee_lib import parse_zigbee_scan
	scan_channels = OrderedDict()
	if (args.zch == ""):
		scan_channels = default_zigbee_freqs
	else:
		for ch in args.zch.split(","):
			try:
				scan_channels[ch] = default_zigbee_freqs[ch]
			except:
				pass
	if(len(scan_channels) > 0):
		zb_tb = zigbee_rftap_nox()
		zb_tb.start()
		for ch in scan_channels:
			print("\nSetting radio to Zigbee - Ch {} GHz".format(ch))
			zb_tb.set_freq(scan_channels[ch])
			time.sleep(float(args.t)/len(scan_channels))
		zb_tb.stop()
		zb_tb.wait()
		parse_zigbee_scan()

