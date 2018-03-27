#! /usr/bin/env python

# FIXME: This tools should identify gateways, clients, and their associated PANIDs

###############################
# Imports taken from zbscapy
###############################

try:
	from scapy.all import *
except ImportError:
	print 'This Requires Scapy To Be Installed.'
	from sys import exit
	exit(-1)
from killerbee import * 
from killerbee.scapy_extensions import *	# this is explicit because I didn't want to modify __init__.py

del hexdump
from scapy.utils import hexdump				# Force using Scapy's hexdump()
import os, sys, struct
from glob import glob
###############################

###############################
# Processing Functions
###############################
# Defaults
indent      = "    "
DEBUG       = False
SHOW_RAW    = False
#zb_file     = None
zb_files    = []
network_key = None
cert_key    = None
SE_Smart_Energy_Profile = 0x0109 # 265

# Dictionaries may not be processed in order. Therefore, these must be separate lists
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

# Addresses
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

def usage():
    print "%s Usage"%sys.argv[0]
    print "    -h: help"
    print "    -f <filename>: capture file with zigbee packets."
    print "    -d <directory name>: directory containing capture files with zigbee packets."
    print "    -D: Turn on debugging."
    sys.exit()

def detect_encryption(pkt):
    '''detect_entryption: Does this packet have encrypted information? Return: True or False'''
    if not pkt.haslayer(ZigbeeSecurityHeader) or not pkt.haslayer(ZigbeeNWK):
        return False
    return True

def detect_app_layer(pkt):
    '''detect_entryption: Does this packet have encrypted information? Return: True or False'''
    if not pkt.haslayer(ZigbeeAppDataPayload):
        return False
    return True

def detect_layer(pkt,layer):
    '''detect_entryption: Does this packet have encrypted information? Return: True or False'''
    #if not pkt.haslayer(ZigbeeAppDataPayload):
    if not pkt.haslayer(layer):
        return False
    return True
###############################

def parse_zigbee_scan():
	layer_count = {}
	for l in ZB_Layers:
		layer_count[ZB_Layers_Names[ZB_Layers.index(l)]] = 0
	zb_file = "/tmp/sensor.pcap"
	packets = kbrdpcap(zb_file)
	for pkt in packets:
		out_str_li = []
		if detect_layer(pkt, ZigbeeNWK):
			pkt_nwk = pkt.getlayer(ZigbeeNWK).fields
			print(pkt_nwk)
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
		print(out_str_li)
			
			

