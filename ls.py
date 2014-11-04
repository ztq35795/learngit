#!/usr/bin/python
def strtran(inputstr):
    stra=''
    a=bin(int(inputstr))[-3:]
#    b=bin(inputcstr[1])[-3:]
#    c=bin(inputstr[2])[-3:]

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


import pwd
import os
import glob
import sys


commend=sys.argv
filename=glob.glob("[!.]*")
hidefile=glob.glob(".*")
hidefilesize=[]
filesize=[]
fileown=[]
hidefileown=[]
fileowner=[]
i=0
for name in hidefile:
    hidefilesize.append(os.path.getsize(name))
    hidefileown.append(oct(os.stat(name)[0])[-3:])
    i=i+1

print("hi")
i=0
for name in filename:
    filesize.append(os.path.getsize(name))
    fileown.append(oct(os.stat(name)[0])[-3:])
    fileowner.append('-')
    print(fileown[0][0],fileowner[0])
#    str2=fileown[0][0]
    for j in range(3):
        str1=strtran(fileown[i][j])
        fileowner[i] += str1

    i=i+1


i=1
if(len(commend)>=2):
    for i in len(commend)-1:
        if(commend[i]=="-a"):
            for name in hidefile:
                print("%s %d" %(name,hidefilesize[i]),end=' ')
                i=i+1
            i=0
        elif(commend[i]=="-l"):
            for name in filename:
                print("%s ")

i=0
for name in filename:
    print("%s %d %s" %(name,filesize[i],fileowner[i]),end=' ')
    i=i+1
print()

