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
    print(stra)
    return stra

def lsa(path):
    import os
    import pwd
    import grp
    filename=glob.glob("*")
    filesize=[]
    fileowner=[]
    link
    user
    group
    i=0
    for name in filename:
        link=os.stat(name).st_nlink
        user=pwd.getpwuid(name).pw_name
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
        print("%s %s"%(fileowner[i],name,link,user))
import os
import glob
import sys

commend=sys.argv
filename=glob.glob("*")
filesize=[]
fileowner=[]
i=0

i=i+1


i=1
if(len(commend)>=2):
    for i in len(commend)-1:
        if(commend[i]=="-a"):
            for name in filename:
                print("%s %d" %(name,hidefilesize[i]),end=' ')
                i=i+1
            i=0
        elif(commend[i]=="-l"):
            for name in filename:
                print("%s ")
    else:
        for name in filename
            if(name)
print()

