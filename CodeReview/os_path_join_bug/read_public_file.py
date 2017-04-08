#!/usr/bin/env python
# coding: utf-8
# Author: Anka9080
# Email: FunSociety@gmail.com

import os
import sys

if __name__ == '__main__':

    if len(sys.argv) < 2: exit()

    file = sys.argv[1]

    print('文件名:{}'.format(file))

    # proj_dir 根据实际环境修改
    proj_dir = '/home/anka9080/Desktop/test/os_path_join_bug/'

    public_dir = 'public/'

    abs_file = os.path.join(proj_dir,public_dir,file)

    print('绝对路径:{}'.format(abs_file))

    with open(abs_file,'r') as input:
        print('文件内容如下:')
        print(input.read())
