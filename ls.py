#!/usr/bin/python
import argparse
import os
import func
parser=argparse.ArgumentParser()
parser.add_argument("-a","--all",action="store_true",help="do not ignore entries starting with .")
parser.add_argument("-l","--long",action="store_true",help="use a long listing format")
parser.add_argument('-R','--recursive',action='store_true',help='list subdirectories recursively')
parser.add_argument('files',metavar='File',default='.',nargs='*',help='The files about which the information will be listed')
args=parser.parse_args()


Dir=args.files
for name in Dir:
    os.chdir(name)
    if(args.recursive):
        func.lsR(args.all,args.long)
    elif(args.long):
        func.lsl(args.all)
    else:
        func.lsa(args.all)

