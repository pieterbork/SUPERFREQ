#!/bin/bash
#author : Kade Cooper kaco0964@colorado.edu
#name : bluetooth_status.bash
#purpose : Check if bluetooth is on. This test may be used for future work...
#date : 2018.03.11
#version: 1.0.0

#Run hcitool dev to list local bluetooth devices
hcitool dev | grep -v 'Devices:'

#Check status code to be passed on
if [ $? -eq 0 ]; then
	exit 0
else
	exit 1
fi