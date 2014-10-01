#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict

word_freq = defaultdict(lambda: 0)

for line in open(sys.argv[1]):
	list = line.strip().split()
	word_freq[list[1]] += int(list[0])

#for i, j in word_freq.items():
#	print i, j

for line2 in open(sys.argv[1]):
	list2 = line2.strip().split()
	P = float(list2[0]) / word_freq[list2[1]]
	print "%r	%s	%s" %(P, list2[1], list2[2])
