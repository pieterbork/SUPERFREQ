#!/bin/bash
#author : Kade Cooper kaco0964@colorado.edu
#name : wifi_nearby_devices.bash
#purpose : Test for nearby wireless devices
#date : 2018.03.15
#version: 1.0.0

#Run arp for locally cached devices via the router (IPv4)
arp -ae
IPV4CODE=$?

#Run ip -6 for finding local devices with IPv6  
ip -6 neighbor show
IPV6CODE=$?

#Check status code to be passed on
if [ $IPV4CODE -eq 0 ] || [ $IPV6CODE -eq 0 ]; then
	exit 0
else
	exit 1
fi