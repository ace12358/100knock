#!/usr/bin/python
# -*-coding:utf-8-*-

import sys

list = []

for line in open (sys.argv[1]):
	itemList = line[:-1].split('\t')
	list.append(itemList)



for i in sorted(list, key = lambda x:x[1]):
	print i[0],i[1]
	
