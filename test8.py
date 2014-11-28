#!/usr/bin/python
# -*-coding:utf-8-*-
"""
実行方法
python test8.py address.txt
"""
import sys

list = list()

for line in open(sys.argv[1]):
	itemList = line[:-1].split('\t')
	list.append(itemList)

for i,j in sorted(list, key = lambda x:x[1]):
	print "%s\t%s" %(i,j)
	
