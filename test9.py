#!/usr/bin/python
# -*-coding:utf-8-*-

import sys

list = []

for line in open (sys.argv[1]):
        itemList = line[:-1].split('\t')
        list.append(itemList)



for i in sorted(list, key = lambda x:(x[1], x[0]), reverse = True):
        print i[0],i[1]
