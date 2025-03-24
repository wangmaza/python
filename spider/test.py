#!/usr/bin/python
# -*- coding: UTF-8 -*-


from bs4 import BeautifulSoup

import requests
print('ok')


r=requests.get("http://www.crazyant.net")
print(r.status_code)
# print(r.text)
print(r.encoding)
print(r.headers)
print("===================")
r=requests.get("http://www.baidu.com")
#网页的编码，一般会从headers中返回，request会自动获取，但是有些网页中没有，request会默认设置成ISO-8859-1
print(r.encoding) #百度的编码并不是ISO-8859-1，通过r.text中的charset可以知道是以utf-8编码的，所以我们要改正，否则会乱码
print(r.status_code)
r.encoding="utf-8"
print(r.text)
print(r.headers)