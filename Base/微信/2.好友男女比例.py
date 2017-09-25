#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__authors__ = 'wangZhen'
import itchat
itchat.auto_login(hotReload=True)
itchat.dump_login_status()

friends = itchat.get_friends(update=True)[:]
total = len(friends) - 1
male = female = other = 0

for friend in friends[1:]:
    sex = friend["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
print("男性好友：%.2f%%" % (float(male) / total * 100))
print("女性好友：%.2f%%" % (float(female) / total * 100))
print("其他：%.2f%%" % (float(other) / total * 100))

