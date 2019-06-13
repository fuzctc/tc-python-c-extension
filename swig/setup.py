# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhichang Fu
# Created Time: 2019-06-13 18:41:41

from distutils.core import setup, Extension

# Extension module name 要有底线前缀
speedup_fib_module = Extension('_speedup_fib', sources=['speedup_fib_wrap.c'])
setup(
    name='SpeedupFib',
    description='A package containing modules for speeding up performance.',
    ext_modules=[speedup_fib_module],
)
