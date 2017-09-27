#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__authors__ = 'wangZhen'

import struct

# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
b=struct.pack('>I',8)
print(b)

# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
ub=struct.unpack('>IH', b'\x00\x00\x00\x08\x00\x02')
print(ub)

