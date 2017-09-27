#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__authors__ = 'wangZhen'

import itertools
na=itertools.count(2)
# for i in na:
#     print(i)
# 因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。

# cycle()会把传入的一个序列无限重复下去：

cs =itertools.cycle('abc')
# for i in cs:
#     print(i)

ns = itertools.repeat('A', 3)
for i in ns:
    print(ns)


for c in itertools.chain('ABC', 'XYZ'):
    print(c)

for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))