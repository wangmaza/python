#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__authors__ = 'wangZhen'
import itchat

itchat.auto_login(hotReload=True)
itchat.dump_login_status()

# f=itchat.search_friends()
# print(f)

#1.通过昵称来找
# ccc=itchat.search_friends(name='陈小举')[0]

#2.发送信息，不要过于频繁，不然微信会删除你俩的好友关系
# ccc.send("hello")
# print(ccc)

# 3.获取特定 UserName 的用户信息，userName是会改变的
# cc=itchat.search_friends(userName='@6f6940b2cf134d109dd7e3d616813069')
# print(cc)



chatrooms=itchat.get_chatrooms(update=True)
#print(chatrooms)

xiaohuo=itchat.search_chatrooms(userName='深情小伙伴')
print(xiaohuo)
