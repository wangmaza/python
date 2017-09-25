#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

class QueueManager(BaseManager):
    pass

if __name__ == '__main__':
    QueueManager.register('get_task')
    QueueManager.register('get_result')
    server_adr = '127.0.0.1'
    print('connect to the server%s',server_adr)
    manager = QueueManager(address = (server_adr,5000),authkey = b'abc')
    manager.connect()
    print('connect successfuly')

    task = manager.get_task()
    result = manager.get_result()
    for i in range(5):
        try:
            t = task.get(timeout = 1)
            print('now process the task%d'%t)
            result.put(t*t)
        except Queue.Empty:
            print('the task queue is empty, maybe some task lost?')
    print('wordker exit')