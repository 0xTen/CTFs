gcc exploit/exploit.c -o xpl -static -lpthread

scripts/decompress.sh
cp xpl initramfs/
scripts/compress.sh

scripts/qemu.sh
