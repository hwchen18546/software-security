#!/bin/bash
cp client.py client_tmp.py
read -p "remote_ip: " remote_ip
sed -i 's/remote_ip/'$remote_ip'/g' client_tmp.py
read -p "remote_port: " remote_port
sed -i 's/remote_port/'$remote_port'/g' client_tmp.py
read -p "sleep_time(sec): " sleep_time
sed -i 's/sleep_interval/'$sleep_time'/g' client_tmp.py
dir=$remote_ip'@'$remote_port
mkdir $dir
cp server.py $dir'/server.py'
sed -i 's/remote_port/'$remote_port'/g' $dir'/server.py'
mv client_tmp.py $dir'/'client.py
