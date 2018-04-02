#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Wifi Rx Rftap Nox
# Generated: Thu Mar 15 20:12:12 2018
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import ieee802_11
import osmosdr
import rftap

from collections import OrderedDict
from time import sleep


default_wifi_freqs = OrderedDict([("1", 2.412e9), ("2", 2.417e9), ("3", 2.422e9), ("4", 2.427e9), ("5", 2.432e9), ("6", 2.437e9), ("7_24", 2.442e9), ("8_24", 2.447e9), ("9_24", 2.452e9), ("10", 2.457e9), ("11_24", 2.462e9), ("7_5", 5.035e9), ("8_5", 5.040e9), ("9_5", 5.045e9), ("11_5", 5.055e9), ("12", 5.060e9), ("16", 5.080e9), ("34", 5.170e9), ("36", 5.180e9), ("38", 5.190e9), ("40", 5.200e9), ("42", 5.210e9), ("44", 5.220e9), ("46", 5.230e9), ("48", 5.240e9), ("50", 5.250e9), ("52", 5.260e9), ("54", 5.270e9), ("56", 5.280e9), ("58", 5.290e9), ("60", 5.300e9), ("62", 5.310e9), ("64", 5.320e9), ("100", 5.500e9), ("102", 5.510e9), ("104", 5.520e9), ("106", 5.530e9), ("108", 5.540e9), ("110", 5.550e9), ("112", 5.560e9), ("114", 5.570e9), ("116", 5.580e9), ("118", 5.590e9), ("120", 5.600e9), ("122", 5.610e9), ("124", 5.620e9), ("126", 5.630e9), ("128", 5.640e9), ("132", 5.660e9), ("134", 5.670e9), ("136", 5.680e9), ("138", 5.690e9), ("140", 5.700e9), ("142", 5.710e9), ("144", 5.720e9), ("149", 5.745e9), ("151", 5.755e9), ("153", 5.765e9), ("155", 5.775e9), ("157", 5.785e9), ("159", 5.795e9), ("161", 5.805e9), ("165", 5.825e9)])
default_wifi_freqs_rev = OrderedDict([(2400000000.0, '0'), (2412000000.0, '1'), (2417000000.0, '2'), (2422000000.0, '3'), (2427000000.0, '4'), (2432000000.0, '5'), (2437000000.0, '6'), (2442000000.0, '7_24'), (2447000000.0, '8_24'), (2452000000.0, '9_24'), (2457000000.0, '10'), (2462000000.0, '11_24'), (5035000000.0, '7_5'), (5040000000.0, '8_5'), (5045000000.0, '9_5'), (5055000000.0, '11_5'), (5060000000.0, '12'), (5080000000.0, '16'), (5170000000.0, '34'), (5180000000.0, '36'), (5190000000.0, '38'), (5200000000.0, '40'), (5210000000.0, '42'), (5220000000.0, '44'), (5230000000.0, '46'), (5240000000.0, '48'), (5250000000.0, '50'), (5260000000.0, '52'), (5270000000.0, '54'), (5280000000.0, '56'), (5290000000.0, '58'), (5300000000.0, '60'), (5310000000.0, '62'), (5320000000.0, '64'), (5500000000.0, '100'), (5510000000.0, '102'), (5520000000.0, '104'), (5530000000.0, '106'), (5540000000.0, '108'), (5550000000.0, '110'), (5560000000.0, '112'), (5570000000.0, '114'), (5580000000.0, '116'), (5590000000.0, '118'), (5600000000.0, '120'), (5610000000.0, '122'), (5620000000.0, '124'), (5630000000.0, '126'), (5640000000.0, '128'), (5660000000.0, '132'), (5670000000.0, '134'), (5680000000.0, '136'), (5690000000.0, '138'), (5700000000.0, '140'), (5710000000.0, '142'), (5720000000.0, '144'), (5745000000.0, '149'), (5755000000.0, '151'), (5765000000.0, '153'), (5775000000.0, '155'), (5785000000.0, '157'), (5795000000.0, '159'), (5805000000.0, '161'), (5825000000.0, '165')])

all_wifi_freqs = {"2.4": [("1", 2.412e9), ("2", 2.417e9), ("3", 2.422e9), ("4", 2.427e9), ("5", 2.432e9), ("6", 2.437e9), ("7", 2.442e9), ("8", 2.447e9), ("9", 2.452e9), ("10", 2.457e9), ("11", 2.462e9)], "5": [("7", 5.035e9), ("8", 5.040e9), ("9", 5.045e9), ("11", 5.055e9), ("12", 5.060e9), ("16", 5.080e9), ("34", 5.170e9), ("36", 5.180e9), ("38", 5.190e9), ("40", 5.200e9), ("42", 5.210e9), ("44", 5.220e9), ("46", 5.230e9), ("48", 5.240e9), ("50", 5.250e9), ("52", 5.260e9), ("54", 5.270e9), ("56", 5.280e9), ("58", 5.290e9), ("60", 5.300e9), ("62", 5.310e9), ("64", 5.320e9), ("100", 5.500e9), ("102", 5.510e9), ("104", 5.520e9), ("106", 5.530e9), ("108", 5.540e9), ("110", 5.550e9), ("112", 5.560e9), ("114", 5.570e9), ("116", 5.580e9), ("118", 5.590e9), ("120", 5.600e9), ("122", 5.610e9), ("124", 5.620e9), ("126", 5.630e9), ("128", 5.640e9), ("132", 5.660e9), ("134", 5.670e9), ("136", 5.680e9), ("138", 5.690e9), ("140", 5.700e9), ("142", 5.710e9), ("144", 5.720e9), ("149", 5.745e9), ("151", 5.755e9), ("153", 5.765e9), ("155", 5.775e9), ("157", 5.785e9), ("159", 5.795e9), ("161", 5.805e9), ("165", 5.825e9)]}

class wifi_rx_rftap_nox(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Wifi Rx Rftap Nox")

        ##################################################
        # Variables
        ##################################################
        self.window_size = window_size = 48
        self.sync_length = sync_length = 320
        self.samp_rate = samp_rate = 20e6
        self.freq = freq = 2.4e9
        self.chan_est = chan_est = ieee802_11.LMS

        ##################################################
        # Blocks
        ##################################################
        self.rftap_rftap_encap_0 = rftap.rftap_encap(0, -1, "")
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.ieee802_11_sync_short_0 = ieee802_11.sync_short(0.56, 2, False, False)
        self.ieee802_11_sync_long_0 = ieee802_11.sync_long(sync_length, False, False)
        self.ieee802_11_parse_mac_0 = ieee802_11.parse_mac(self.freq, True, False)
        self.ieee802_11_moving_average_xx_1 = ieee802_11.moving_average_ff(window_size + 16)
        self.ieee802_11_moving_average_xx_0 = ieee802_11.moving_average_cc(window_size)
        self.ieee802_11_frame_equalizer_0 = ieee802_11.frame_equalizer(chan_est, freq, samp_rate, False, False)
        self.ieee802_11_decode_mac_0 = ieee802_11.decode_mac(False, False)
        self.fft_vxx_0 = fft.fft_vcc(64, True, (window.rectangular(64)), True, 1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 64)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_CLIENT", "127.0.0.1", "52001", 10000, False)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, 16)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, sync_length)
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.ieee802_11_decode_mac_0, 'out'), (self.ieee802_11_parse_mac_0, 'in'))    
        self.msg_connect((self.ieee802_11_decode_mac_0, 'out'), (self.rftap_rftap_encap_0, 'in'))    
        self.msg_connect((self.rftap_rftap_encap_0, 'out'), (self.blocks_socket_pdu_0, 'pdus'))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_divide_xx_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.ieee802_11_moving_average_xx_1, 0))    
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_delay_0, 0), (self.ieee802_11_sync_long_0, 1))    
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_conjugate_cc_0, 0))    
        self.connect((self.blocks_delay_0_0, 0), (self.ieee802_11_sync_short_0, 0))    
        self.connect((self.blocks_divide_xx_0, 0), (self.ieee802_11_sync_short_0, 2))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.ieee802_11_moving_average_xx_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.ieee802_11_frame_equalizer_0, 0))    
        self.connect((self.ieee802_11_frame_equalizer_0, 0), (self.ieee802_11_decode_mac_0, 0))    
        self.connect((self.ieee802_11_moving_average_xx_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.ieee802_11_moving_average_xx_0, 0), (self.ieee802_11_sync_short_0, 1))    
        self.connect((self.ieee802_11_moving_average_xx_1, 0), (self.blocks_divide_xx_0, 1))    
        self.connect((self.ieee802_11_sync_long_0, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.ieee802_11_sync_short_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.ieee802_11_sync_short_0, 0), (self.ieee802_11_sync_long_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.blocks_delay_0_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 0))    

    def get_window_size(self):
        return self.window_size

    def set_window_size(self, window_size):
        self.window_size = window_size
        self.ieee802_11_moving_average_xx_0.set_length(self.window_size)
        self.ieee802_11_moving_average_xx_1.set_length(self.window_size + 16)

    def get_sync_length(self):
        return self.sync_length

    def set_sync_length(self, sync_length):
        self.sync_length = sync_length
        self.blocks_delay_0.set_dly(self.sync_length)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.ieee802_11_frame_equalizer_0.set_bandwidth(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.ieee802_11_parse_mac_0.set_frequency(self.freq)
        self.ieee802_11_frame_equalizer_0.set_frequency(self.freq)
        self.osmosdr_source_0.set_center_freq(self.freq, 0)

    def get_chan_est(self):
        return self.chan_est

    def set_chan_est(self, chan_est):
        self.chan_est = chan_est
        self.ieee802_11_frame_equalizer_0.set_algorithm(self.chan_est)


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

def sleep_channel(channel_time, socketio, elapsed_time):
	num_updates = int(channel_time)	* 2		#update every half second
	leftover_time = channel_time - int(channel_time)
	while (True):		#always run the update at least once
		line_count = 0
		try:
			with open('/tmp/out_frames', 'r') as f:
				for line in f:
					line_count += 1
		except IOError:
			pass
		socketio.emit('wifi_count', {'msg': line_count})
		socketio.emit('progress', {'msg': elapsed_time})
		if num_updates < 1:
			break
		else:
			elapsed_time += 0.5
			sleep(0.5)
			num_updates -= 1
	elapsed_time += leftover_time
	sleep(leftover_time)
	return elapsed_time


def run_wifi_scan(socketio=None, user_channels=[], send_updates=False, scan_time=120, elapsed_time=0):
	scan_channels = OrderedDict()
	if(len(user_channels) < 1):
		scan_channels = default_wifi_freqs
	else:
		for ch in user_channels:
			try:
				scan_channels[ch] = default_wifi_freqs[ch]
			except KeyError:
				pass
	channel_time = float(scan_time)/len(scan_channels)
	if(len(scan_channels) > 0):
		wifi_tb = wifi_rx_rftap_nox()
		wifi_tb.start()
		for ch in scan_channels:
			wifi_tb.set_freq(scan_channels[ch])
			if send_updates:
				socketio.emit('update', {'msg':display_wifi_channel(ch)})
				elapsed_time = sleep_channel(channel_time, socketio, elapsed_time)
			else:
				print("\n\nSetting radio to {}".format(display_wifi_channel(ch)))
				sleep(channel_time)
		wifi_tb.stop()
		wifi_tb.wait()


