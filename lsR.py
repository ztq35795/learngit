#!/usr/bin/python
def lsR(a):
    import glob
    if(a==1):
        filename=glob.glob(".*")+glob.glob("*")
    else:
        filename=glob.glob("*")



    for name in filename:
        print("%s "%(name),end=' ')


