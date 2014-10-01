#/usr/bin/python
#coding:utf-8

import sys

for line in open(sys.argv[1]):
	itemList = line.strip().split()
	print line.strip()
	if itemList[1] == "a" or itemList[1] == "A":
		print "A"
	elif itemList[1] == "the" or itemList[1] == "The":
		print "THE"
	else:
		print "None"
