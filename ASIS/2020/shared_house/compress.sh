gcc -o exploit -static $1
mv ./exploit ./rootfs
cd rootfs
find . -print0 \
| cpio --null -ov --format=newc > rootfs.cpio
mv ./rootfs.cpio ../
