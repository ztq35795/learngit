#!/usr/bin/python
import func,os

args=func.GetArg()

Dir=args.getfileaddress()
for name in Dir:
    os.chdir(name)  #change to the point file
    if(args.isRecursive()==True):
        func.lsR(args.isAll(),args.isLong())
    elif(args.isLong()==True):
        func.lsl(args.isAll())
    elif(args.isAll()==False):
        func.lsa(args.isAll())
