#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__authors__ = 'wangZhen'


import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("王振喜欢乔雅欣")