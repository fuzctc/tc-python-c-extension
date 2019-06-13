# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhichang Fu
# Created Time: 2019-06-13 16:12:56

from distutils.core import setup, Extension
speedup_fib_module = Extension('speedup_fib', sources=['speedup_fib.c'])
setup(
    name='SpeedupFib',
    description='A package containing modules for speeding up fib.',
    ext_modules=[speedup_fib_module],
)
