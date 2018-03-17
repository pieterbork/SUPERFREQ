#!/bin/bash
#author : Kade Cooper kaco0964@colorado.edu
#name : wifi_status.bash
#purpose : Ensure wifi is turned on
#date : 2018.03.11
#version: 1.0.0

#Run wifi command rfkill list: If no, then wifi is turned on. If yes, then wifi is turned off
rfkill list | grep no

#Check status code to be passed on
if [ $? -eq 0 ]; then
	exit 0
else
	exit 1
fi