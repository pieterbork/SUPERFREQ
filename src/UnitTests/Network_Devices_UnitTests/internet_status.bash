#!/bin/bash
#author : Kade Cooper kaco0964@colorado.edu
#name : internet_status.bash
#purpose : Ensure internet is turned on. This test may be used for future work...
#date : 2018.03.15
#version: 1.0.1

#Run ping command for Google Server and store exit code in variable
ping -c 1 8.8.8.8
PINGCODE=$?

#Run wget to see if web content exists. These two tests should help determine internet connectivity
wget --spider http://google.com
WGETCODE=$?

#Check status code to be passed on
if [ $PINGCODE -eq 0 ] || [ $WGETCODE -eq 0 ]; then
	exit 0
else
	exit 1
fi