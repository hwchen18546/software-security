#!/usr/bin/python
import socket, subprocess
import time
import sys 

HOST = ''
PORT = remote_port

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))
    while 1:  
        result, (rip, rport) = s.recvfrom(1024)
        sys.stdout.write('%s@%d:%s' %(rip, rport, result))
except KeyboardInterrupt:
    s.close 
