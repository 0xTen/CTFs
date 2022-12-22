extract-vmlinux bzImage > vmlinux
terminator --new-tab -x "gdb vmlinux --ex 'target remote :1234'" &
scripts/run.sh
rm -rf vmlinux
