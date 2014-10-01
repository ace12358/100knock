#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import MeCab
import re

def test46():

	longlist = []

	for line in open(sys.argv[1]):
        	tagger = MeCab.Tagger('mecabrc')
        	result = tagger.parse(line)
        	result2 = result.strip()
        	sentence = result2.split("\n")
        	for tok in sentence:
        	        to = tok.strip()
        	        if "\t" in to:
        	                t = re.split("\t|,", to)
        	                longlist += t
	for i in range(len(longlist)):
       		if longlist[i]=="名詞" and longlist[i+10]=="名詞":
               		noun2 = longlist[i-1] + longlist[i+9]
                	a = i+20
                	while longlist[a]=="名詞":
                        	noun2 += longlist[a-1]
                        	a+=10
                	print noun2

