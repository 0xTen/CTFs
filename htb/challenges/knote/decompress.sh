mkdir rootfs
cd rootfs
cp ../rootfs.img .
cpio -idm < ./rootfs.img
rm rootfs.img
