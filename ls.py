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

def lsl(a):
    import os
    import pwd
    import grp
    import time
    import glob
    if(a==0):
        filename=glob.glob("*")
    else:
        filename=glob.glob(".*")+glob.glob("*")
    filesize=[]
    fileowner=[]

    i=0

    for name in filename:
        link=os.stat(name).st_nlink
        user=pwd.getpwuid(os.stat(name).st_uid).pw_name
        group=grp.getgrgid(os.stat(name).st_gid).gr_name
        mon=time.localtime(os.stat(name).st_mtime).tm_mon
        time1=time.ctime(os.stat(name).st_mtime)[7:-8]
        filesize.append(os.stat(name).st_size)
        fileown=oct(os.stat(name).st_mode)[-3:]
        if(os.path.isfile(name)):
            fileowner.append('-')
        elif(os.path.isdir(name)):
            fileowner.append('d')
        elif(os.path.islink(name)):
            fileowner.append('l')
        elif(group=='disk'):
            fileowner.append('b')
        else:
            fileowner.append('c')
        for j in range(3):
            str1=strtran(fileown[j])
            fileowner[i] += str1
        print("%s %s %s %s %6s %2d月 %s %s"%(fileowner[i],link,user,group,filesize[i],mon,time1,name))
        i=i+1
def lsa(a):
    import glob
    if(a==1):
        filename=glob.glob(".*")+glob.glob("*")
    else:
        filename=glob.glob("*")
    for name in filename:
        print("%s "%(name),end=' ')
import sys

commend=sys.argv
if(len(commend)>=2):
    if(commend[1]=="-al"):
        lsl(1)
    if(commend[1]=="-l"):
        lsl(0)
    if(commend[1]=="-a"):
        lsa(1)
else:
        lsa(0)

print()

