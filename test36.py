#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

word_list = []

for line in open(sys.argv[1]):
	list = line.strip().split("\t")
	word_list.append(list[1])

for i in range(len(word_list)-1):
	print word_list[i]+"\t"+word_list[i+1]


