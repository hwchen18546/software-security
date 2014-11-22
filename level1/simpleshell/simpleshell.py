#!/usr/bin/env python

import telnetlib  
# The remote host
HOST = 'secprog.cs.nctu.edu.tw' 
PORT = 10001
tn = telnetlib.Telnet(HOST,PORT)

data = tn.read_until('#')
print data
tn.write("info\n")
data = tn.read_until('#')
print data
seed = data.split('Start time ')[1]
seed = int(seed.split('\n')[0])
print seed

password = list("DoYouThinkThisIsPassword")
number = 65535 * seed + 31337
print number
magic1 = number & 0xff
#print magic1

number = seed / 65535
magic2 = number & 0xff
#print magic2

index = 0
for i in range(0,6):
    password[index] = chr(ord(password[index])^magic1)
    password[index+2] = chr(ord(password[index+2])^magic2)
    index = index + 4
print password
password = ''.join(password)
tn.write("login\n")
data = tn.read_until(':')
print data
tn.write("admin\n")
data = tn.read_until(':')
print data
tn.write(password)
tn.write('\n')
tn.interact()
