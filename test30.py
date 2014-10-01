#!/usr/bin/python
#-*-coding:utf-8-*-
from stemming.porter2 import stem
import sys
import re

for line in open(sys.argv[1]):
        list = line.strip().split(" ")
	list.append(stem(list[1]))
	print list[0], list[1], list[2]
