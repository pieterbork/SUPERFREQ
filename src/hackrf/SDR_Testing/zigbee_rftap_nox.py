#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: IEEE 802.15.4 Transceiver using OQPSK PHY
# Generated: Thu Mar 15 20:38:54 2018
##################################################

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from epy_block_0 import blk
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from ieee802_15_4_oqpsk_phy import ieee802_15_4_oqpsk_phy  # grc-generated hier_block
from optparse import OptionParser
import foo
import ieee802_15_4
import osmosdr
import rftap

from scapy.all import *
from killerbee import * 
from killerbee.scapy_extensions import *

from collections import OrderedDict
from time import sleep

zb_file = "/tmp/zigbee.pcap"

default_zigbee_freqs = [2.405e9, 2.410e9, 2.415e9, 2.420e9, 2.425e9, 2.430e9, 2.435e9, 2.440e9, 2.445e9, 2.450e9, 2.455e9, 2.460e9, 2.465e9, 2.470e9, 2.475e9, 2.480e9]
channel_map = {2.405e9: "11", 2.410e9: "12", 2.415e9: "13", 2.420e9: "14", 2.425e9: "15", 2.430e9: "16", 2.435e9: "17", 2.440e9: "18", 2.445e9: "19", 2.450e9: "20", 2.455e9: "21", 2.460e9: "22", 2.465e9: "23", 2.470e9: "24", 2.475e9: "28", 2.480e9: "26"}

ZB_Layers = [ \
    Dot15d4, \
    Dot15d4FCS, \
    Dot15d4Beacon, \
    Dot15d4Data, \
    Dot15d4Ack, \
    Dot15d4Cmd, \
    ZigbeeNWK, \
    ZigBeeBeacon, \
    ZigbeeSecurityHeader, \
    ZigbeeAppDataPayload, \
    ZigbeeAppCommandPayload, \
]
ZB_Layers_Names = [ \
    "Dot15d4", \
    "Dot15d4FCS", \
    "Dot15d4Beacon", \
    "Dot15d4Data", \
    "Dot15d4Ack", \
    "Dot15d4Cmd", \
    "ZigbeeNWK", \
    "ZigBeeBeacon", \
    "ZigbeeSecurityHeader", \
    "ZigbeeAppDataPayload", \
    "ZigbeeAppCommandPayload" \
]

zb_addrs = { \
    'src_addr':'00:00:00:00:00:00', \
    'dest_addr':'00:00:00:00:00:00', \
    'extended_pan_id':'00:00:00:00:00:00', \
    'src_addr':0xffff, \
    'source':'00:00:00:00:00:00', \
    #'source':0xffff, \
    'src_panid':0xffff, \
    'ext_src':'00:00:00:00:00:00', \
    'dest_panid':0xffff, \
    'dest_addr':0x0, \
    'destination':0xffff \
}
addr_names = zb_addrs.keys()


class zigbee_rftap_nox(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "IEEE 802.15.4 Transceiver using OQPSK PHY")

        ##################################################
        # Variables
        ##################################################
        self.gain = gain = 50
        self.freq = freq = 2.45e9

        ##################################################
        # Blocks
        ##################################################
        self.rftap_rftap_encap_0 = rftap.rftap_encap(2, 195, "")
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(4e6)
        self.osmosdr_source_0.set_center_freq(freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(gain, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.ieee802_15_4_rime_stack_0 = ieee802_15_4.rime_stack(([129]), ([131]), ([132]), ([23,42]))
        self.ieee802_15_4_oqpsk_phy_0 = ieee802_15_4_oqpsk_phy()
        self.ieee802_15_4_mac_0 = ieee802_15_4.mac(True)
        self.foo_wireshark_connector_0 = foo.wireshark_connector(195, False)
        self.epy_block_0 = blk()
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_CLIENT", "127.0.0.1", "52001", 10000, False)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, zb_file, False)
        self.blocks_file_sink_0.set_unbuffered(True)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.epy_block_0, 'out'), (self.rftap_rftap_encap_0, 'in'))    
        self.msg_connect((self.ieee802_15_4_mac_0, 'pdu out'), (self.foo_wireshark_connector_0, 'in'))    
        self.msg_connect((self.ieee802_15_4_mac_0, 'pdu out'), (self.ieee802_15_4_oqpsk_phy_0, 'txin'))    
        self.msg_connect((self.ieee802_15_4_mac_0, 'app out'), (self.ieee802_15_4_rime_stack_0, 'fromMAC'))    
        self.msg_connect((self.ieee802_15_4_oqpsk_phy_0, 'rxout'), (self.epy_block_0, 'in'))    
        self.msg_connect((self.ieee802_15_4_oqpsk_phy_0, 'rxout'), (self.foo_wireshark_connector_0, 'in'))    
        self.msg_connect((self.ieee802_15_4_oqpsk_phy_0, 'rxout'), (self.ieee802_15_4_mac_0, 'pdu in'))    
        self.msg_connect((self.ieee802_15_4_rime_stack_0, 'toMAC'), (self.ieee802_15_4_mac_0, 'app in'))    
        self.msg_connect((self.rftap_rftap_encap_0, 'out'), (self.blocks_socket_pdu_0, 'pdus'))    
        self.connect((self.foo_wireshark_connector_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.ieee802_15_4_oqpsk_phy_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.ieee802_15_4_oqpsk_phy_0, 0))    

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.osmosdr_source_0.set_gain(self.gain, 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.osmosdr_source_0.set_center_freq(freq, 0)


def detect_layer(pkt,layer):
    if not pkt.haslayer(layer):
        return False
    return True

def parse_zigbee_scan():
	global send_packet_updates
	layer_count = {}
	for l in ZB_Layers:
		layer_count[ZB_Layers_Names[ZB_Layers.index(l)]] = 0
	packets = kbrdpcap(zb_file)
	pkt_info = []
	for pkt in packets:
		out_str_li = []
		if detect_layer(pkt, ZigbeeNWK):
			pkt_nwk = pkt.getlayer(ZigbeeNWK).fields
			out_str_li.append("src: {}".format(pkt_nwk['source']))
			out_str_li.append("dst: {}".format(pkt_nwk['destination']))
			if "ext_src" in pkt_nwk:
				out_str_li.append("ext_src: {}".format(':'.join(x.encode('hex') for x in struct.pack('>Q',pkt_nwk['ext_src']))))
			else:
				out_str_li.append("ext_src: XX:XX:XX:XX:XX:XX:XX:XX")
			if "ext_dst" in pkt_nwk:
				out_str_li.append("ext_dst: {}".format(':'.join(x.encode('hex') for x in struct.pack('>Q',pkt_nwk['ext_dst']))))
			else:
				out_str_li.append("ext_dst: XX:XX:XX:XX:XX:XX:XX:XX")

		if detect_layer(pkt, ZigbeeSecurityHeader):
			pkt_nwk = pkt.getlayer(ZigbeeSecurityHeader).fields
			if "source" in pkt_nwk:
				out_str_li.append("sec_src: {}".format(':'.join(x.encode('hex') for x in struct.pack('>Q',pkt_nwk['source']))))
			else:
				out_str_li.append("sec_src: XX:XX:XX:XX:XX:XX:XX:XX")
			if "destination" in pkt_nwk:
				out_str_li.append("sec_dst: {}".format(':'.join(x.encode('hex') for x in struct.pack('>Q',pkt_nwk['destination']))))
			else:
				out_str_li.append("sec_dst: XX:XX:XX:XX:XX:XX:XX:XX")
		pkt_info.append(out_str_li)
	with open("/tmp/zb_out.txt", "a") as f:
		for pkt in pkt_info:
			if (len(pkt) > 0):
				f.write(", ".join(pkt) + "\n")

def sleep_channel(channel_time, socketio, elapsed_time):
	num_updates = int(channel_time)	* 2		#update every half second
	leftover_time = channel_time - int(channel_time)
	while (True):		#always run the update at least once
		num_packs = len(rdpcap(zb_file))
		print("Packets - " + str(num_packs))
		socketio.emit('zigbee_count', {'msg': num_packs})
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
	

def run_zigbee_scan(user_channels=[], socketio=None, send_updates=False, scan_time=30, elapsed_time=0):
	scan_channels = []
	if (len(user_channels) < 1):
		scan_channels = default_zigbee_freqs
	else:
		for ch in user_channels:
			if float(ch) in default_zigbee_freqs:
				scan_channels.append(float(ch))
	if(len(scan_channels) > 0):
		channel_time = float(scan_time)/len(scan_channels)
		zb_tb = zigbee_rftap_nox()
		zb_tb.start()
		for ch in scan_channels:
			zb_tb.set_freq(ch)
			if send_updates:
				socketio.emit('update', {'msg':"Zigbee<br>Ch {}".format(channel_map[ch])})
				elapsed_time = sleep_channel(channel_time, socketio, elapsed_time)
			else:
				print("\nSetting radio to Zigbee - Ch {}".format(ch))
				sleep(channel_time)
			parse_zigbee_scan()
		zb_tb.stop()
		zb_tb.wait()


