#!/bin/bash
#author : Kade Cooper kaco0964@colorado.edu
#name : bluetooth_nearby_devices.bash
#purpose : Check if bluetooth is on. This test may be used for future work...
#date : 2018.03.11
#version: 1.0.0

#Run a bluetooth scan for nearby devices to see if they are on. Will fail if hcitool dev failed
hcitool scan 

#Check status code to be passed on
if [ $? -eq 0 ]; then
	exit 0
else
	exit 1
fi