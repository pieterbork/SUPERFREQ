#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Wifi Rx Rftap
# Generated: Thu Feb 15 16:12:21 2018
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
        	choices=[2.437e9, 5.805e9],
        	labels=["Ch 6 | 2437", "Ch 161| 5805"],
        )
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
        self.ieee802_11_parse_mac_0 = ieee802_11.parse_mac(True, True)
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

    def get_chan_est(self):
        return self.chan_est

    def set_chan_est(self, chan_est):
        self.chan_est = chan_est
        self._chan_est_chooser.set_value(self.chan_est)
        self.ieee802_11_frame_equalizer_0.set_algorithm(self.chan_est)


def main(top_block_cls=wifi_rx_rftap, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
