#!/bin/bash
#author : Kade Cooper kaco0964@colorado.edu
#name : internet_status.bash
#purpose : Ensure internet is turned on. This test may be used for future work...
#date : 2018.03.11
#version: 1.0.0

#Run ping command for Google Server...test will fail for users who can't reach this. Sorry!
ping -c 1 8.8.8.8

#Check status code to be passed on
if [ $? -eq 0 ]; then
	exit 0
else
	exit 1
fi