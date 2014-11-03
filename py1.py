#!/usr/bin/python
'a test module'
__author__ = 'Billion Zhan'
import os
filename=os.listdir(".")
for name in filename:
    print("%s "%(name),end=' ')
print()
