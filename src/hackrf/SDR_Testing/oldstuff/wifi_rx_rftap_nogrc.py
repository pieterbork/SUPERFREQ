#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Wifi Rx Rftap
# Generated: Sun Feb 18 16:11:24 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import ieee802_11
import osmosdr
import rftap
import time
import wx


class wifi_rx_rftap(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Wifi Rx Rftap")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.window_size = window_size = 48
        self.sync_length = sync_length = 320
        self.samp_rate = samp_rate = 20e6
        self.freq = freq = 2.437e9
        self.chan_est = chan_est = ieee802_11.LMS

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.samp_rate,
        	callback=self.set_samp_rate,
        	label="Sample Rate",
        	choices=[1e6, 3e6, 5e6, 10e6, 15e6, 20e6],
        	labels=["1 MHz", "3 MHz", "5 MHz", "10 MHz", "15 MHz", "20 MHz"],
        	style=wx.RA_HORIZONTAL,
        )
        self.Add(self._samp_rate_chooser)
        self._freq_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.freq,
        	callback=self.set_freq,
        	label="Channel",
        	choices=[2.412e9, 2.417e9, 2.422e9, 2.427e9, 2.432e9, 2.437e9, 2.442e9, 2.447e9, 2.452e9, 2.457e9, 2.462e9, 5.035e9, 5.040e9, 5.045e9, 5.055e9, 5.060e9, 5.080e9, 5.170e9, 5.180e9, 5.190e9, 5.200e9, 5.210e9, 5.220e9, 5.230e9, 5.240e9, 5.250e9, 5.260e9, 5.270e9, 5.280e9, 5.290e9, 5.300e9, 5.310e9, 5.320e9, 5.500e9, 5.510e9, 5.520e9, 5.530e9, 5.540e9, 5.550e9, 5.560e9, 5.570e9, 5.580e9, 5.590e9, 5.600e9, 5.610e9, 5.620e9, 5.630e9, 5.640e9, 5.660e9, 5.670e9, 5.680e9, 5.690e9, 5.700e9, 5.710e9, 5.720e9, 5.745e9, 5.755e9, 5.765e9, 5.775e9, 5.785e9, 5.795e9, 5.805e9, 5.825e9],
                labels=["Ch 1 | 2412", "Ch 2 | 2417", "Ch 3 | 2422", "Ch 4 | 2427", "Ch 5 | 2432", "Ch 6 | 2437", "Ch 7 | 2442", "Ch 8 | 2447", "Ch 9 | 2452", "Ch 10 | 2457", "Ch 11 | 2462", "Ch 36 | 5180", "Ch 7 | 5035", "Ch 8 | 5040", "Ch 9 | 5045", "Ch 11 | 5055", "Ch 12 | 5060", "Ch 16 | 5080", "Ch 34 | 5170", "Ch 36 | 5180", "Ch 38 | 5190", "Ch 40 | 5200", "Ch 42 | 5210", "Ch 44 | 5220", "Ch 46 | 5230", "Ch 48 | 5240", "Ch 50 | 5250", "Ch 52 | 5260", "Ch 54 | 5270", "Ch 56 | 5280", "Ch 58 | 5290", "Ch 60 | 5300", "Ch 62 | 5310", "Ch 64 | 5320", "Ch 100 | 5500", "Ch 102 | 5510", "Ch 104 | 5520", "Ch 106 | 5530", "Ch 108 | 5540", "Ch 110 | 5550", "Ch 112 | 5560", "Ch 114 | 5570", "Ch 116 | 5580", "Ch 118 | 5590", "Ch 120 | 5600", "Ch 122 | 5610", "Ch 124 | 5620", "Ch 126 | 5630", "Ch 128 | 5640", "Ch 132 | 5660", "Ch 134 | 5670", "Ch 136 | 5680", "Ch 138 | 5690", "Ch 140 | 5700", "Ch 142 | 5710", "Ch 144 | 5720", "Ch 149 | 5745", "Ch 151 | 5755", "Ch 153 | 5765", "Ch 155 | 5775", "Ch 157 | 5785", "Ch 159 | 5795", "Ch 161 | 5805", "Ch 165 | 5825"])
        self.Add(self._freq_chooser)
        self._chan_est_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.chan_est,
        	callback=self.set_chan_est,
        	label='chan_est',
        	choices=[ieee802_11.LS, ieee802_11.LMS, ieee802_11.STA, ieee802_11.COMB],
        	labels=["LS", "LMS", "STA", "Linear Comb"],
        	style=wx.RA_HORIZONTAL,
        )
        self.Add(self._chan_est_chooser)
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
        self.ieee802_11_parse_mac_0 = ieee802_11.parse_mac(freq, True, False)
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
        self.ieee802_11_moving_average_xx_1.set_length(self.window_size + 16)
        self.ieee802_11_moving_average_xx_0.set_length(self.window_size)

    def get_sync_length(self):
        return self.sync_length

    def set_sync_length(self, sync_length):
        self.sync_length = sync_length
        self.blocks_delay_0.set_dly(self.sync_length)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self._samp_rate_chooser.set_value(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.ieee802_11_frame_equalizer_0.set_bandwidth(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_chooser.set_value(self.freq)
        self.osmosdr_source_0.set_center_freq(self.freq, 0)
        self.ieee802_11_frame_equalizer_0.set_frequency(self.freq)
        self.ieee802_11_parse_mac_0.set_frequency(self.freq)

    def get_chan_est(self):
        return self.chan_est

    def set_chan_est(self, chan_est):
        self.chan_est = chan_est
        self._chan_est_chooser.set_value(self.chan_est)
        self.ieee802_11_frame_equalizer_0.set_algorithm(self.chan_est)


def main(top_block_cls=wifi_rx_rftap, options=None):
    doteleven_freqs = [2.412e9, 2.417e9, 2.422e9, 2.427e9, 2.432e9, 2.437e9, 2.442e9, 2.447e9, 2.452e9, 2.457e9, 2.462e9, 5.035e9, 5.040e9, 5.045e9, 5.055e9, 5.060e9, 5.080e9, 5.170e9, 5.180e9, 5.190e9, 5.200e9, 5.210e9, 5.220e9, 5.230e9, 5.240e9, 5.250e9, 5.260e9, 5.270e9, 5.280e9, 5.290e9, 5.300e9, 5.310e9, 5.320e9, 5.500e9, 5.510e9, 5.520e9, 5.530e9, 5.540e9, 5.550e9, 5.560e9, 5.570e9, 5.580e9, 5.590e9, 5.600e9, 5.610e9, 5.620e9, 5.630e9, 5.640e9, 5.660e9, 5.670e9, 5.680e9, 5.690e9, 5.700e9, 5.710e9, 5.720e9, 5.745e9, 5.755e9, 5.765e9, 5.775e9, 5.785e9, 5.795e9, 5.805e9, 5.825e9]
    tb = top_block_cls()
    tb.Start(True)
    for freq in doteleven_freqs:
        print("\nSetting frequency to {} GHz".format(freq/1e9))
        tb.set_freq(freq)
        time.sleep(1)
    tb.stop()


if __name__ == '__main__':
    main()
