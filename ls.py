#!/usr/bin/python
def strtran(inputstr):
    stra=''
    a=bin(int(inputstr))[-3:]
    if a[0] =='1':
        stra+='r'
    else:
        stra+='-'
    if a[1] =='1':
        stra+='w'
    else:
        stra+='-'
    if a[2] =='1':
        stra+='x'
    else:
        stra+='-'
    return stra

def lsa():
    import os
    import pwd
    import grp
    import time
    filename=glob.glob("*")
    filesize=[]
    fileowner=[]

    i=0

    for name in filename:
        link=os.stat(name).st_nlink
        user=pwd.getpwuid(os.stat(name).st_uid).pw_name
        group=grp.getgrgid(os.stat(name).st_gid).gr_name
        time=os.stat()
        filesize.append(os.stat(name).st_size)
        fileown=oct(os.stat(name).st_mode)[-3:]
        if(os.path.isfile(name)):
            fileowner.append('-')
        elif(os.path.isdir(name)):
            fileowner.append('d')
        else:
            fileowner.append('l')
        for j in range(3):
            str1=strtran(fileown[j])
            fileowner[i] += str1
        print("%s %s %s %s %s %s"%(fileowner[i],link,user,group,filesize[i],name))
        i=i+1
import os
import glob
import sys

commend=sys.argv
filename=glob.glob("*")
filesize=[]
fileowner=[]
lsa()

i=1
print()

