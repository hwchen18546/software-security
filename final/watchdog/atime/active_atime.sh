#!/bin/bash

# you must active atime to get the access time
# linux default is relatime(update in some case)
# https://en.wikipedia.org/wiki/Stat_%28system_call%29#Solutions
echo -e "original mount"
mount | grep "ext"
sudo mount -o remount,strictatime /
echo -e "remount option to strictatime"
mount | grep "ext"
