#!/usr/bin/python
#-*-cording:utf-8-*-
import sys

addressDict = dict()
for line in open(sys.argv[1]):
        addressDict[line.strip().split('\t')[0]] = 0

print len(addressDict)
