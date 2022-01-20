gcc -o exploit -static $1 -lpthread
mv ./exploit ./rootfs
cd rootfs
find . -print0 \
| cpio --null -ov --format=newc > rootfs.img
mv ./rootfs.img ../
