#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict

word_freq = defaultdict(lambda: 0)

for line in open(sys.argv[1]):
	word_freq[line.strip()] += 1

for w, f in word_freq.items():
	print "%r	%s" %(f, w)
