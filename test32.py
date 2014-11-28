#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import marshal
from collections import Counter

f = open('dict.txt', 'wb') 

dict = {}
tapple = ()
cnt = Counter()

for line in open(sys.argv[1]):
	list = line.strip().split("|")
	tapple = (list[1], list[3], list[6])
	if list[0] in dict:
		cnt[list[0]] += 1
		w = list[0] + "(" + str(cnt[list[0]]+1) +")"
		dict[w] = tapple
	else:
		dict[list[0]] = tapple


marshal.dump(dict, f)
f.close()


