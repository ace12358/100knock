#!/usr//bin/python
#-*-coding:utf-8-*-

import sys
word_dict = {}

for line in open(sys.argv[1]):
	list = line.strip().split("|")
	word_dict[list[0]] = (list[1], list[3], list[6])

#for w, t in word_dict.items():
#	print w, t

flag = True
while (flag):
    word = raw_input()
    print word_dict[word]
