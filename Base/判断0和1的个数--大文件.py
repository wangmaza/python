#!/usr/bin/env python
# -*- coding: utf-8 -*-
#这个程序需要在python2下才能执行

import struct, os
filename="F:\\CentOS-7-x86_64-DVD-1511.iso"
count_one=0
count_zero = 0

with open(filename,'rb') as current_byte:
    print(current_byte)
    for lines in  current_byte:
        for ff in list(lines):
            count_one += bin(struct.unpack("B", ff)[0]).count('1')
            count_zero += bin(struct.unpack("B", ff)[0]).count('0')
            print('0的次数;'+str(count_one)+'        '+'1的次数:'+ str(count_zero))

count_zero = os.path.getsize(filename) * 8 - count_one
print('One:  ' + str(count_one) + ' times           Zero: ' + str(count_zero) )