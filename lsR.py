#!/usr/bin/python
def lsR():
    import ls
    import glob
    import os
    filename=glob.glob(".*")+glob.glob("*")
    ls.lsa(0)
    for name in filename:
        if(os.path.isdir(name)):
            os.chdir(name)
            print(os.getcwd())
            lsR()
    print()
    os.chdir("..")
    return

lsR()
