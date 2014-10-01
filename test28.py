#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
word = []

for line in open(sys.argv[1]):
        list = line.strip().split("\t")
        word.append(list[1])

#print word

byegram = []

for i in range(len(word)-1):
	byegram.append(word[i] + " " + word[i+1])

for i in range(len(byegram)):
	print byegram[i]

from collections import defaultdict
wordDict = defaultdict(lambda: 0)

for w in byegram:
	wordDict[w] += 1

for i, j in sorted(wordDict.items(), key = lambda x:-x[1]):
        print "%s\t%r" %(i, j)

