#!/bin/bash -e
#author : Kade Cooper kaco0964@colorado.edu
#name : usb_status.bash
#purpose : Ensure HackRF device is connected
#date : 2018.03.29
#version: 1.0.0

#Run built-in command to test HackRF
lsusb | egrep "Great Scott Gadgets HackRF|OpenMoko, Inc."

#Check status code to be passed on
if [ $? -eq 0 ]; then
	exit 0
else
	exit 1
fi