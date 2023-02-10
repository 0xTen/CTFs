cd /home/xten/Documents/research/linux/initramfs
fakeroot scripts/decompress.sh
nano initramfs/etc/init.d/S99ctf
fakeroot scripts/compress.sh
rm -rf initramfs
