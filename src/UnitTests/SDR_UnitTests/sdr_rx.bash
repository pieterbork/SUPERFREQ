#!/bin/bash -e
#author : Kade Cooper kaco0964@colorado.edu
#name : sdr_rx.bash
#purpose : Ensure HackRF device is connected
#date : 2018.03.29
#version: 1.0.10

#Run our command through the docker container with the hackrf attached to print to file
timeout 10 btle_rx -o > bluetooth_out.txt

#If the file exists then return code 0 to signify the test passed. Otherwise, false
if [ -s bluetoot_out.txt ]
then
        exit 0
else
        exit 1
fi