#!/bin/bash

checkfile="flag"
logfile="log"
freq=2
temp=$(stat $checkfile | grep Access | tail -n 1)
echo "----------------------------------------" | tee -a $logfile
echo "Start tracing $(pwd)/$checkfile per $freq sec" | tee -a $logfile
echo $temp | tee -a $logfile
echo "----------------------------------------" | tee -a $logfile

while :
do
    result=$(stat $checkfile | grep Access | tail -n 1)
    if [ "$result" != "$temp" ]; then
        echo "$result" | tee -a $logfile
    fi
    sleep $freq
    temp=$result
done
