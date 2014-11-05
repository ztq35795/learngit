#!/usr/bin/python
def lsR(j):
    import ls
    import glob
    import os
    filename=glob.glob("*")
    if(j==0):
        print(".:")
    elif(len(filename)==False):
        print()
        os.chdir("..")
        return

    ls.lsa(0)
    print()
    for name in filename:
        if(os.path.isdir(name)):
            os.chdir(name)
            print("%s:"%os.getcwd())
            lsR(1)
    os.chdir("..")
    return

lsR(0)
