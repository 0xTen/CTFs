#include <linux/init.h>
#include <linux/module.h>
#include <linux/slab.h>
#include <linux/fs.h>
#include <linux/string.h>
#include <asm/uaccess.h>
#include <linux/miscdevice.h>

#define DEV_NAME "researcher"
#define CLASS_NAME "researcher"

#define OBJ_SIZE    PAGE_SIZE/2
#define OBJ_MAX     128

static long researcher_ioctl(struct file *fd, unsigned cmd, unsigned long u_req);

static struct miscdevice researcher_dev;
static struct file_operations researcher_ops = {
    .unlocked_ioctl = researcher_ioctl
};

struct researcher_cache{
    char buf[OBJ_SIZE];
};

struct researcher_req{
    unsigned idx;
    size_t size;
    void __user *buf;
};

static struct kmem_cache *researcher_cachep;

enum researcher_cmd{
    cmd_alloc = 0x1337000,
    cmd_delete = 0x1337001,
    cmd_write = 0x1337002
};

void *researcher_objs[OBJ_MAX];
void *aux_buf;

int researcher_write(unsigned idx, void __user *buf, size_t size){

    if(copy_from_user(aux_buf, buf, size)){
        return -EFAULT;
    }
    memcpy(researcher_objs[idx], aux_buf, size);
    return 0;
}

static long researcher_ioctl(struct file *fd, unsigned cmd, unsigned long u_req){

    struct researcher_req req;

    if(copy_from_user(&req, (void __user *)u_req, sizeof(struct researcher_req))){
        return -EFAULT;
    }

    switch(cmd){
        case cmd_alloc:
            if (req.idx >= OBJ_MAX || researcher_objs[req.idx]){
                return -EFAULT;
            }
            researcher_objs[req.idx] = kmem_cache_zalloc(researcher_cachep, GFP_KERNEL);
            printk("0x%lx",(unsigned long)researcher_objs[req.idx]);

            if (req.size > OBJ_SIZE){
                return -EFAULT;
            }

            return researcher_write(req.idx, req.buf, req.size);

        case cmd_delete:
            if (!researcher_objs[req.idx]){
                return -EFAULT;
            }
            kmem_cache_free(researcher_cachep, researcher_objs[req.idx]);
            return 0;

        case cmd_write:
            if (req.size > OBJ_SIZE || !researcher_objs[req.idx]){
                return -EFAULT;
            }

            return researcher_write(req.idx, req.buf, req.size);
    }

    return -EFAULT;
}

static int __init researcher_init(void){
    researcher_dev.minor = MISC_DYNAMIC_MINOR;
    researcher_dev.name = DEV_NAME;
    researcher_dev.fops = &researcher_ops;
    researcher_dev.mode = 0644;
    if (misc_register(&researcher_dev)){
        return -EFAULT;
    }

    researcher_cachep = KMEM_CACHE(researcher_cache, SLAB_PANIC | SLAB_ACCOUNT);
    if(!researcher_cachep){
        return -EFAULT;
    }

    memset(researcher_objs, '\0', OBJ_MAX*sizeof(void *));
    aux_buf = kzalloc(OBJ_SIZE, GFP_KERNEL);

    return 0;
}

static void __exit researcher_exit(void){
    misc_deregister(&researcher_dev);

    return;
}

module_init(researcher_init);
module_exit(researcher_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("0xTen");
MODULE_DESCRIPTION("researcher LKM");
