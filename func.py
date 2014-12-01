#!/usr/bin/python
import glob,os,pwd,grp,time,argparse

def GetCommendAndFile():
    parser=argparse.ArgumentParser()
    parser.add_argument("-a","--all",action="store_true",help="do not ignore entries starting with .")
    parser.add_argument("-l","--long",action="store_true",help="use a long listing format")
    parser.add_argument('-R','--recursive',action='store_true',help='list subdirectories recursively')
    parser.add_argument('files',metavar='File',default='.',nargs='*',help='The files about which the information will be listed')
    args=parser.parse_args()
    return args

def lsR(a,l,j=0):
    if(a):
        filename=glob.glob("*")+glob.glob(".*")
    else:
        filename=glob.glob("*")
    if(j==0):
        print(".:")
    elif(len(filename)==False):
        print()
        os.chdir("..")
        return
    if(l):
        lsl(a)
    else:
        lsa(a)
    print()
    for name in filename:
        if(os.path.isdir(name) and (os.path.islink(name)==False)):
            os.chdir(name)
            print("%s:"%os.getcwd())
            lsR(a,l,1)
    os.chdir("..")
    return
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
    if(a==0):
        filename=glob.glob("*")
    else:
        filename=glob.glob(".*")+glob.glob("*")
    filesize=[]
    fileowner=[]
    i=0
    dirsize=os.stat(".").st_size/1000
    print("总用量 %d"%dirsize)


    Max=len("%s"%os.stat(filename[0]).st_size)
    Max=Max
    Maxlink=len("%s"%os.stat(filename[0]).st_nlink)
    Maxuser=len(pwd.getpwuid(os.stat(filename[0]).st_uid).pw_name)
    Maxgroup=len(grp.getgrgid(os.stat(filename[0]).st_gid).gr_name)
    for name in filename:
        filelinkl=len("%s"%os.stat(name).st_nlink)
        filesizel=len("%s"%os.stat(name).st_size)

        userl=len(pwd.getpwuid(os.stat(name).st_uid).pw_name)
        groupl=len(grp.getgrgid(os.stat(name).st_gid).gr_name)

        if(Maxlink<=int(filelinkl)):
            Maxlink=int(filelinkl)
        if(Max<=int(filesizel)):
            Max=int(filesizel)

        if(Maxuser<=int(userl)):
            Maxuser=int(userl)

        if(Maxgroup<=int(groupl)):
            Maxgroup=int(groupl)
    for name in filename:
        link="%s"%os.stat(name).st_nlink
        if(Max<=int(filesizel)):
            Max=int(filesizel)
        user=pwd.getpwuid(os.stat(name).st_uid).pw_name
        group=grp.getgrgid(os.stat(name).st_gid).gr_name
        mon=time.localtime(os.stat(name).st_mtime).tm_mon
        time1=time.ctime(os.stat(name).st_mtime)[8:-8]
        filesize.append("%s"%os.stat(name).st_size)
        fileown=oct(os.stat(name).st_mode)[-3:]
        if(os.path.isfile(name)):
            fileowner.append('-')
        elif(os.path.islink(name)):
            fileowner.append('l')
            filesize[i]="7"
        elif(os.path.isdir(name)):
            fileowner.append('d')
        elif(group=='disk'):
            fileowner.append('b')
        else:
            fileowner.append('c')
        for j in range(3):
            str1=strtran(fileown[j])
            fileowner[i] += str1
        print(fileowner[i],link.rjust(Maxlink),user.ljust(Maxuser),group.ljust(Maxgroup),filesize[i].rjust(Max),"%2s月"%(mon),time1,name)
        i=i+1
def lsa(a):
    if(a==1):
        filename=glob.glob(".*")+glob.glob("*")
    else:
        filename=glob.glob("*")
    for name in filename:
        print("%s "%(name),end=' ')
    print()

class GetArg():
    """Get commend and address
then return them"""
    def __init__(self):
        self.args=GetCommendAndFile()

    def getfileaddress(self):
        return self.args.files

    def isAll(self):
        return self.args.all

    def isLong(self):
        return self.args.long

    def isRecursive(self):
        return self.args.recursive
