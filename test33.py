#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import marshal

f = open(sys.argv[1], 'rb')

marshal_list = []
count = 0
for line in marshal.load(f):
	marshal_list.append(line)

for line2 in open(sys.argv[2]):
	list = line2.strip().split("\t")
	word = list[2]
	
	for i in range(len(marshal_list)):
		if word in marshal_list[i]:
			count += 1
	if count != 0:
		print word + " is in dict"
	else:
		print word + " is out of dict"

	count = 0

