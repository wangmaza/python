#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__authors__ = 'wangZhen'
import os,sys

#需要安装pywin这个模块，需要单独下载
import win32api
import win32con
import win32file
from ctypes import *
# win32api.MessageBox(0, 'Hello,Win32API', 'WYM', win32con.MB_OK)


print(sys.path)
user32 = windll.LoadLibrary('user32.dll')
user32.MessageBoxA(0, 'Ctypes is cool!', 'Ctypes', 0)

