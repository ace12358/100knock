#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

sentence_list = []

for line in open(sys.argv[1]):
	sentence = line.strip().split(".")

for i in range(len(sentence)):
	print sentence[i]
