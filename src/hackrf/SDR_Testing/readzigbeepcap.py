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

if __name__ == '__main__':
	layer_count = {}
	for l in ZB_Layers:
		layer_count[ZB_Layers_Names[ZB_Layers.index(l)]] = 0
	zb_file = "/tmp/sensor.pcap"
	packets = kbrdpcap(zb_file)
	for pkt in packets:
		for l in ZB_Layers:
			if detect_layer(pkt,l):
				layer_count[ZB_Layers_Names[ZB_Layers.index(l)]] += 1
				if 'ext_src' in pkt.getlayer(l).fields:
					print("----------------------------")
					print(pkt.summary())
                                	print("SOURCE: " + ':'.join(x.encode('hex') for x in struct.pack('>Q',pkt.getlayer(l).fields['ext_src'])))
                                	print("DEST: " + ':'.join(x.encode('hex') for x in struct.pack('>Q',pkt.getlayer(l).fields['ext_dst'])))
	print(len(packets))
	print(layer_count)



#    if DEBUG: print "\nProcessing files:",zb_files,"\n"
#    for zb_file in zb_files:
#        if DEBUG: print "\nProcessing file:",zb_file,"\n"
#        #print "\nProcessing file:",zb_file,"\n"
#        data = kbrdpcap(zb_file)
#        num_pkts = len(data)
#
#        # Detect Layers
#        if DEBUG: print indent + "Detecting ZigBee Layers"
#        for e in range(num_pkts):
#	    print("\n\nPacket #{0}".format(e))
#            if DEBUG: print indent + "Packet " + str(e),data[e].summary()
#
#            for l in ZB_Layers:
#                if detect_layer(data[e],l): 
#                    print indent*2 + ZB_Layers_Names[ZB_Layers.index(l)]
#                    fields = data[e].getlayer(l).fields
#                    if DEBUG: print indent*3 + "Fields:",fields
#                    for a in addr_names:
#                        if fields.has_key(a) and fields[a]: 
#                            val = fields[a]
#                            # If this is an extended address then we have to split
#                            if val > 0xffff:
#                                print indent*3 + a + ":",':'.join(x.encode('hex') for x in struct.pack('>Q',val))
#                            else:
#                                print indent*3 + a + ":",hex(val)
#
#        print ""



