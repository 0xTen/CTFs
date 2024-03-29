DIR=$PWD

mkdir $DIR/initramfs
cd $DIR/initramfs
cp $DIR/initramfs.cpio.gz .
gunzip initramfs.cpio.gz
cpio -idm < initramfs.cpio
rm initramfs.cpio
