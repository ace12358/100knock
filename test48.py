#!/usr/bin/python
# -*-coding:utf-8-*-

import sys
from collections import defaultdict

verb_freq = defaultdict(lambda: 0)

for line in open(sys.argv[1]):
#	list = line.decode("utf8").strip().split('\t')
	list = line.strip().split('\t')
	verb_freq[list[0]] += 1

for verb, freq in sorted(verb_freq.items(), key = lambda x : x[1], reverse = True):
	print "%s\t%r" %(verb,freq)
