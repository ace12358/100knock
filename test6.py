#!/usr/bin/python
# -*-cording:utf-8-*-

import sys

argvs = sys.argv
argc = len(argvs)
t = int(argvs[2])

print type(t)
print argc
print t
list =[]

for line in open(sys.argv[1]):
        list.append(line)
list.reverse()

for count in range(t):
        print list[count],
