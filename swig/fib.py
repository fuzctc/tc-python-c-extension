# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhichang Fu
# Created Time: 2019-06-13 14:38:52

import time

from speedup_fib import fib

start_ts = time.time()
print(fib(35))
print(time.time() - start_ts)


