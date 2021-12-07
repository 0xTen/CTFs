mkdir rootfs
cd rootfs
cp ../rootfs.cpio.gz .
gunzip ./rootfs.cpio.gz
cpio -idm < ./rootfs.cpio
rm rootfs.cpio
