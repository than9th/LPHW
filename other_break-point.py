# encoding: utf-8
"""
@ Author: Kunkai Su 
@ Contact: su.kk@qq.com
@ Site: www.geneureka.com
@ Project: LPHW
@ File: other_break-point.py
@ Time: 2017/8/21 17:54:35

这一行开始写关于本文件的说明与解释
"""


import threading
import time


def get_thread_name():
    t = threading.current_thread()
    return t.name


def print_time(delay):
    """Define a function for the thread"""
    thread_name = get_thread_name()
    count = 0
    while count < 8:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (thread_name, time.ctime()))

# Create two threads as follows
t1 = threading.Thread(target=print_time, args=(1,))
t2 = threading.Thread(target=print_time, args=(2,))
t1.start()
t2.start()
t1.join()
t2.join()
