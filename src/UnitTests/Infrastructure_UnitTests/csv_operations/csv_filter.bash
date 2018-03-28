#!/bin/bash

#author : Kade Cooper kaco0964@colorado.edu
#name : csv_filter.bash
#purpose : Filter csv files to help generate graphs from the terminal application
#date : 2018.03.28
#version: 1.0.10


#Detect the latest file to be added
# ls -1 -t | head -1

#Copy the unfiltered.csv. VERIFIED!
cp unfiltered.csv tmp_unfiltered.csv

#Find number of occurences for each line and save to a file that will be manipulated. VERIFIED!
sort tmp_unfiltered.csv | uniq --count | sort -bgr > unique_lines.txt

#Clean up added four leading spacing in unique_lines.txt file. VERIFIED!
sed "s/^[[:space:]]*//" -i unique_lines.txt

#Clean up all spaces between commas. VERIFIED!
sed 's/, \+\| \+,/,/g' -i unique_lines.txt

#Remove all matched strings from our wordfile.txt. VERIFIED!
sed -e "$(sed 's:.*:s/&//ig:' wordfile.txt)" unique_lines.txt > cleaned_unique_lines.txt

#Cut all lines but the first column. VERIFIED!
awk  '{$1=$1; print $1}' cleaned_unique_lines.txt > occurences.txt

#Create a shadow copy without the number in a file for sorted.csv. VERIFIED!
sed -i -r 's/\S+(\s+)?//1' cleaned_unique_lines.txt

#Find total number of lines. VERIFIED!
TOTALLINES=$(wc -l tmp_unfiltered.csv | awk '{print $1}')

#Calculate percentages for each
while read i; do
  printf '%.4f\n' "$(echo "scale=4;$i/$TOTALLINES" | bc)" >> percentage.txt
done <occurences.txt

#Attach percentages to the end of each row in the unique_lines.txt
paste -d"," cleaned_unique_lines.txt percentage.txt > filtered.csv


#After all is said and done, use Vim in Ex mode to add header column to the file for importing into the database
ex -sc '1i|duration,frame,subtype,ssid,seq_nr,mac_address_1,mac_address_2,mac_address_3,frequency,percentage' -cx filtered.csv

#Remove files this script made
rm tmp_unfiltered.csv occurences.txt unique_lines.txt cleaned_unique_lines.txt percentage.txt 