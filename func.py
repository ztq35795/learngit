#!/usr/bin/python
import glob,os,pwd,grp,time,argparse

def JudgeIsAllAndReturnFilename(All):
    if(All==True):
        fileName=glob.glob("*")+glob.glob(".*")
    else:
        fileName=glob.glob("*")
    return fileName

def lsR(All,Long,j=0):
    filename=JudgeIsAllAndReturnFilename(ALL)
    if(j==0):
        print(".:")
    elif(len(filename)==False):
        print()
        os.chdir("..")
        return
    if(Long):
        lsl(All)
    else:
        lsa(All)
    print()
    for name in filename:
        if(os.path.isdir(name) and (os.path.islink(name)==False)):
            os.chdir(name)
            print("%s:"%os.getcwd())
            lsR(All,l,1)
    os.chdir("..")
    return

def TransOwnFromNumToStr(ownnum):
    stra=''
    a=bin(int(ownnum))[-3:]
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

class GetFormInfo:
    def __init__(self,filename):
        self.Maxsizelen=len("%s"%os.stat(filename[0]).st_size)
        self.Maxlinklen=len("%s"%os.stat(filename[0]).st_nlink)
        self.Maxuserlen=len(pwd.getpwuid(os.stat(filename[0]).st_uid).pw_name)
        self.Maxgrouplen=len(grp.getgrgid(os.stat(filename[0]).st_gid).gr_name)

        #get the max length of each output form
        for name in filename:

            filelinkl=len("%s"%os.stat(name).st_nlink)
            filesizel=len("%s"%os.stat(name).st_size)
            userl=len(pwd.getpwuid(os.stat(name).st_uid).pw_name)
            groupl=len(grp.getgrgid(os.stat(name).st_gid).gr_name)

            if(self.Maxlinklen<=int(filelinkl)):
                self.Maxlinklen=int(filelinkl)

            if(self.Maxsizelen<=int(filesizel)):
                self.Maxsizelen=int(filesizel)

            if(self.Maxuserlen<=int(userl)):
                self.Maxuserlen=int(userl)

            if(self.Maxgrouplen<=int(groupl)):
                self.Maxgrouplen=int(groupl)

    def Maxlink(self):
        return self.Maxlinklen

    def Maxsize(self):
        return self.Maxsizelen

    def Maxuser(self):
        return self.Maxuserlen

    def Maxgroup(self):
        return self.Maxgrouplen

class FileState:
    def __init__(self,name):
        self.link="%s"%os.stat(name).st_nlink
        self.user=pwd.getpwuid(os.stat(name).st_uid).pw_name
        self.group=grp.getgrgid(os.stat(name).st_gid).gr_name
        self.mon=time.localtime(os.stat(name).st_mtime).tm_mon
        self.time1=time.ctime(os.stat(name).st_mtime)[8:-8]
        self.filesize="%s"%os.stat(name).st_size
        self.fileown=oct(os.stat(name).st_mode)[-3:]

    def Link(self):
        return self.link

    def User(self):
        return self.user

    def Group(self):
        return self.group

    def Mon(self):
        return self.mon

    def Time(self):
        return self.time1

    def Filesize(self):
        return self.filesize

    def Fileown(self):
        i=0
        fileowner=[]
        for ownnum in self.fileown:
            str1=TransOwnFromNumToStr(ownnum)
            fileowner += str1
        return fileowner

def lsl(All):
    filename=JudgeIsAllAndReturnFilename(All)
    forminfo=GetFormInfo(filename)

    Maxgrouplen=forminfo.Maxgroup()
    Maxuserlen=forminfo.Maxuser()
    Maxsizelen=forminfo.Maxsize()
    Maxlinklen=forminfo.Maxlink()
    i=0
#    dirsize=os.stat(".").st_size/1000
#    print("总用量 %d"%dirsize)


    for name in filename:
        FileInfo=FileState(name)
        fileowner=[]
        link=FileInfo.Link()
        user=FileInfo.User()
        group=FileInfo.Group()
        filesize=FileInfo.Filesize()
        mon=FileInfo.Mon()
        time1=FileInfo.Time()

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

        fileowner=fileowner+FileInfo.Fileown()

        print(fileowner,link.rjust(Maxlinklen),user.ljust(Maxuserlen),group.ljust(Maxgrouplen),filesize.rjust(Maxsizelen),"%2s月"%(mon),time1,name)



def lsa(All):
    filename=JudgeIsAllAndReturnFilename(All)

    for name in filename:
        print("%s "%(name),end=' ')
        #This is not bug,the compiler is wrong
    print()

def GetCommendAndFile():
    parser=argparse.ArgumentParser()
    parser.add_argument("-a","--all",action="store_true",help="do not ignore entries starting with .")
    parser.add_argument("-l","--long",action="store_true",help="use a long listing format")
    parser.add_argument('-R','--recursive',action='store_true',help='list subdirectories recursively')
    parser.add_argument('files',metavar='File',default='.',nargs='*',help='The files about which the information will be listed')
    args=parser.parse_args()
    return args


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
