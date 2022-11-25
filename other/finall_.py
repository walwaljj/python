#path.splitext("images/dog/aaaa.png") => ('images/dog/aaaa'.'.png')로 알 수 있게함

import os
from os import path

base = 'images'

def get_category_images(base):
    images = {}
    for dir in os.listdir(base) :
        dir_path = path.join(base, dir)
        images[dir] = os.listdir(dir_path)

    return images

category_images = get_category_images(base)

for dir, fnames in category_images.items():
    for ix,fname in enumerate(fnames,1) :
        print(fname)
        src_path = path.join(base,dir,fname)
        dst_path = path.join(base,dir,f'{ix:04}.png')
        # print(f'{src_path}=>{dst_path}')
        os.rename(src_path,dst_path)


