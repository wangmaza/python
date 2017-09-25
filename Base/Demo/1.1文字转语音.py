#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__authors__ = 'wangZhen'

import importlib,sys
importlib.reload(sys)

#coding=utf-8
import pyttsx3
engine = pyttsx3.init()
engine.say('I will speak this text.')
engine.runAndWait()