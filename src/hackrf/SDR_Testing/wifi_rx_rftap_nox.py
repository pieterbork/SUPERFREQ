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


default_wifi_freqs = [2.412e9, 2.417e9, 2.422e9, 2.427e9, 2.432e9, 2.437e9, 2.442e9, 2.447e9, 2.452e9, 2.457e9, 2.462e9, 5.035e9, 5.040e9, 5.045e9, 5.055e9, 5.060e9, 5.080e9, 5.170e9, 5.180e9, 5.190e9, 5.200e9, 5.210e9, 5.220e9, 5.230e9, 5.240e9, 5.250e9, 5.260e9, 5.270e9, 5.280e9, 5.290e9, 5.300e9, 5.310e9, 5.320e9, 5.500e9, 5.510e9, 5.520e9, 5.530e9, 5.540e9, 5.550e9, 5.560e9, 5.570e9, 5.580e9, 5.590e9, 5.600e9, 5.610e9, 5.620e9, 5.630e9, 5.640e9, 5.660e9, 5.670e9, 5.680e9, 5.690e9, 5.700e9, 5.710e9, 5.720e9, 5.745e9, 5.755e9, 5.765e9, 5.775e9, 5.785e9, 5.795e9, 5.805e9, 5.825e9]

channel_map = {2.412e9: ("2.4", "1"), 2.417e9: ("2.4","2"), 2.422e9: ("2.4","3"), 2.427e9: ("2.4","4"), 2.432e9: ("2.4","5"), 2.437e9: ("2.4","6"), 2.442e9: ("2.4","7"), 2.447e9: ("2.4","8"), 2.452e9: ("2.4","9"), 2.457e9: ("2.4","10"), 2.462e9: ("2.4","11"),5.035e9: ("5","7"), 5.040e9: ("5","8"), 5.045e9: ("5","9"), 5.055e9: ("5","11"), 5.060e9: ("5","12"), 5.080e9: ("5","16"), 5.170e9: ("5","34"), 5.180e9: ("5","36"), 5.190e9: ("5","38"), 5.200e9: ("5","40"), 5.210e9: ("5","42"), 5.220e9: ("5","44"), 5.230e9: ("5","46"), 5.240e9: ("5","48"), 5.250e9: ("5","50"), 5.260e9: ("5","52"), 5.270e9: ("5","54"), 5.280e9: ("5","56"), 5.290e9: ("5","58"), 5.300e9: ("5","60"), 5.310e9: ("5","62"), 5.320e9: ("5","64"), 5.500e9: ("5","100"), 5.510e9: ("5","102"), 5.520e9: ("5","104"), 5.530e9: ("5","106"), 5.540e9: ("5","108"), 5.550e9: ("5","110"), 5.560e9: ("5","112"), 5.570e9: ("5","114"), 5.580e9: ("5","116"), 5.590e9: ("5","118"), 5.600e9: ("5","120"), 5.610e9: ("5","122"), 5.620e9: ("5","124"), 5.630e9: ("5","126"), 5.640e9: ("5","128"), 5.660e9: ("5","132"), 5.670e9: ("5","134"), 5.680e9: ("5","136"), 5.690e9: ("5","138"), 5.700e9: ("5","140"), 5.710e9: ("5","142"), 5.720e9: ("5","144"), 5.745e9: ("5","149"), 5.755e9: ("5","151"), 5.765e9: ("5","153"), 5.775e9: ("5","155"), 5.785e9: ("5","157"), 5.795e9: ("5","159"), 5.805e9: ("5","161"), 5.825e9: ("5","165")}


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
	band, chan = channel_map[ch]
	return "Wifi {0} GHz<br>Ch {1}".format(band, chan)

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
	scan_channels = []
	if(len(user_channels) < 1):
		scan_channels = default_wifi_freqs
	else:
		for ch in user_channels:
			if float(ch) in default_wifi_freqs:
				scan_channels.append(float(ch))
	if(len(scan_channels) > 0):
		channel_time = float(scan_time)/len(scan_channels)
		wifi_tb = wifi_rx_rftap_nox()
		wifi_tb.start()
		for ch in scan_channels:
			wifi_tb.set_freq(ch)
			if send_updates:
				socketio.emit('update', {'msg':display_wifi_channel(ch)})
				elapsed_time = sleep_channel(channel_time, socketio, elapsed_time)
			else:
				print("\n\nSetting radio to {}".format(display_wifi_channel(ch)))
				sleep(channel_time)
		wifi_tb.stop()
		wifi_tb.wait()


