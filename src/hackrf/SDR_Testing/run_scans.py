#!/usr/bin/python

import argparse,time,atexit

parser = argparse.ArgumentParser(description="Run different SUPERFREQ scans")
parser.add_argument("-w", action="store_true", default=False, help="Run wifi scan")
parser.add_argument("-z", action="store_true", default=False, help="Run zigbee scan")
parser.add_argument("-t", default="30", help="Total scan run time in seconds")
args = parser.parse_args()

print(args.w, args.z, args.t)

if args.w:
	from wifi_rx_rftap_nox import wifi_rx_rftap_nox
	doteleven_channels = [2.412e9, 2.417e9, 2.422e9, 2.427e9, 2.432e9, 2.437e9, 2.442e9, 2.447e9, 2.452e9, 2.457e9, 2.462e9, 5.035e9, 5.040e9, 5.045e9, 5.055e9, 5.060e9, 5.080e9, 5.170e9, 5.180e9, 5.190e9, 5.200e9, 5.210e9, 5.220e9, 5.230e9, 5.240e9, 5.250e9, 5.260e9, 5.270e9, 5.280e9, 5.290e9, 5.300e9, 5.310e9, 5.320e9, 5.500e9, 5.510e9, 5.520e9, 5.530e9, 5.540e9, 5.550e9, 5.560e9, 5.570e9, 5.580e9, 5.590e9, 5.600e9, 5.610e9, 5.620e9, 5.630e9, 5.640e9, 5.660e9, 5.670e9, 5.680e9, 5.690e9, 5.700e9, 5.710e9, 5.720e9, 5.745e9, 5.755e9, 5.765e9, 5.775e9, 5.785e9, 5.795e9, 5.805e9, 5.825e9]
	tb = wifi_rx_rftap_nox()
	tb.start()
	for freq in doteleven_channels:
		print("\nSetting frequency to {} GHz".format(freq/1e9))
		tb.set_freq(freq)
		time.sleep(float(args.t)/len(doteleven_channels))
	tb.stop()
	tb.wait()

if args.z:
	from zigbee_rftap_nox import zigbee_rftap_nox
	zb_channels = [1000000 * (2400 + 5 * (i - 10)) for i in range(11, 27)]
	tb = zigbee_rftap_nox()
	tb.start()
	for freq in zb_channels:
		print("\nSetting frequency to {} GHz".format(freq/1e9))
		tb.set_freq(freq)
		time.sleep(float(args.t)/len(zb_channels))
	tb.stop()
	tb.wait()


def cleanup():
	tb.stop()
	tb.wait()

atexit.register(cleanup)
