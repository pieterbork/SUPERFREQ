#!/bin/bash

#author : Kade Cooper kaco0964@colorado.edu
#name : wifi_csv_filter.bash
#purpose : Filter csv files to help generate graphs from the terminal application
#date : 2018.03.30
#version: 1.2.01

CURRENTDIR=`pwd | sed 's/\(src\).*/\1/g'`
PATHTODB='/UnitTests/Infrastructure_UnitTests/csv_operations/'
#Concatenate the two strings
FULLPATH=$CURRENTDIR$PATHTODB

#Navigate here for test
cd $FULLPATH


#Copy the unfiltered.csv. VERIFIED!
cp wifi_out.txt tmp_unfiltered.csv

#Find number of occurrences for each line and save to a file that will be manipulated. VERIFIED!
sort tmp_unfiltered.csv | uniq --count | sort -bgr > unique_lines.txt

#Clean up added four leading spacing in unique_lines.txt file. VERIFIED!
sed "s/^[[:space:]]*//" -i unique_lines.txt

#Clean up all spaces between commas. VERIFIED!
sed 's/, \+\| \+,/,/g' -i unique_lines.txt

#Remove all matched strings from our wordfile.txt. VERIFIED!
sed -e "$(sed 's:.*:s/&//ig:' wifi_wordfile.txt)" unique_lines.txt > cleaned_unique_lines.txt

#Cut all lines but the first column. VERIFIED!
awk  '{$1=$1; print $1}' cleaned_unique_lines.txt > occurrences.txt

#Create a shadow copy without the number in a file for sorted.csv. VERIFIED!
sed -i -r 's/\S+(\s+)?//1' cleaned_unique_lines.txt

#Find total number of lines. VERIFIED!
TOTALLINES=$(wc -l tmp_unfiltered.csv | awk '{print $1}')


#Calculate percentages for each
while read i; do
  printf '%.4f\n' "$(echo "scale=4;$i/$TOTALLINES" | bc)" >> percentage.txt
done <occurrences.txt


#Attach percentages to the end of each row in the unique_lines.txt
#paste -d"," cleaned_unique_lines.txt percentage.txt > wifi_filtered.csv

#For whole number use below
paste -d"," cleaned_unique_lines.txt occurrences.txt > wifi_filtered.csv

#Remove any lines which do not have the correct number of columns. This will prepare the below file for DB import
awk -F',' 'NF==10' wifi_filtered.csv  > db_wifi_filtered.csv


#After all is said and done, use Vim in Ex mode to add header column to the file for importing into the database
#ex -sc '1i|duration,frame,subtype,ssid,seq_nr,mac_address_1,mac_address_2,mac_address_3,frequency,percentage' -cx db_wifi_filtered.csv
ex -sc '1i|duration,frame,subtype,ssid,seq_nr,mac_address_1,mac_address_2,mac_address_3,frequency,occurrence' -cx db_wifi_filtered.csv


#Finally, in order for our graphs to have any meaning, display the top ten occurrences
sed -n -e '1,21p' db_wifi_filtered.csv > graph_wifi_filtered.csv

#Remove files this script made
rm tmp_unfiltered.csv unique_lines.txt cleaned_unique_lines.txt percentage.txt occurrences.txt wifi_filtered.csv

#NOTE: TWO files db_wifi_filtered.csv & graph_wifi_filtered.csv should exist in each respective directory

#Reset test directory
cd $CURRENTDIR