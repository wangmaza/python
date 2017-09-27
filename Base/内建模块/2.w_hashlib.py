#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__authors__ = 'wangZhen'

import hashlib

md5=hashlib.md5()
md5.update('how to use'.encode('utf-8')) #必须经过编码后才能进行
print(md5.hexdigest())


#sha1
import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())