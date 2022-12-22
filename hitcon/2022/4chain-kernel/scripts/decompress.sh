mkdir initramfs
cd initramfs
gunzip ../initramfs.cpio.gz
cpio -idm < ../initramfs.cpio
rm -rf ../initramfs.cpio
