cd initramfs
find . -print0 \
| cpio --null -ov --format=newc > ../initramfs.cpio
cd ../
gzip ./initramfs.cpio
rm -rf ./initramfs.cpio
rm -rf initramfs
