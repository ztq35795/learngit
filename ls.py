#!/usr/bin/python
'a test module'
__author__ = 'Billion Zhan'
import os
import glob
import sys
commend=sys.argv
filename=glob.glob("[!.]*")
hidefile=glob.glob(".*")
if(len(commend)==2):
    if(commend[1]=="-a"):
        for name in hidefile:
            print("%s "%(name),end=' ')

for name in filename:
    print("%s "%(name),end=' ')

print()
