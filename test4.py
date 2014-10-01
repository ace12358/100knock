#!/usr/bin/python
# -*-cording:utf-8-*-

import sys

list1 = []
list2 = []

for line1 in open(sys.argv[1]):
	line1 = line1.strip()
	list1.append(line1)

for line2 in open(sys.argv[2]):
	line2 = line2.strip()
	list2.append(line2)

for i in range(len(list1)):
	print list1[i] + "\t" + list2[i]
