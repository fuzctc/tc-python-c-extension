# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhichang Fu
# Created Time: 2019-06-13 14:38:52

import time


def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


start_ts = time.time()
print(fib_recursive(35))
print(time.time() - start_ts)

from speedup_fib import speedup_fib
start_ts = time.time()
print(speedup_fib(35))
print(time.time() - start_ts)


