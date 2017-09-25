#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue = queue.Queue()
result_queue = queue.Queue()
def return_task():
    return task_queue
def return_result():
    return result_queue
class QueueManager(BaseManager):
    pass
def test():
    QueueManager.register('get_task',callable = return_task)
    QueueManager.register('get_result',callable = return_result)
    manager = QueueManager(address = ('127.0.0.1',5000),authkey = b'abc')#绑定到端口5000,并且设置验证码'abc'
    manager.start()
#获得经过封装之后的task和result
    task,result = manager.get_task(),manager.get_result()
#放一些任务
    for i in range(5):
        print('put %d in task'%i)
        task.put(i)
#获取结果
    print('try to get result')
    for i in range(5):
        r = result.get(timeout = 10)
        print('get the result %d'%r)
    manager.shutdown()
    print('master exit')

if __name__ == '__main__':
    freeze_support()
    test()