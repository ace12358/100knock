#!/usr/bin/python
#-*-coding:utf-8-*-

import sys


for line in open(sys.argv[1]):
	word = line.strip().split(" ")
	word.append("\n")
	for i in range(len(word)):
		print word[i]
			


