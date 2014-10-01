#!/usr/bin/python
#-*-coding:utf-8-*-

import sys 
import MeCab
import re

text = []
for line in open(sys.argv[1]):
        tagger = MeCab.Tagger('mecabrc')
        result = tagger.parse(line)
        result2 = result.strip()
#        print result2
        sentence = result2.split("\n")	
	sent = []
        for tok in sentence:
#		print "aaaaaaaa"
#		print tok
#                to = tok.strip()
#		to = tok
                if "\t" in to: 
                        t = re.split("\t|,", to)
			word_dict = {"surface":t[0], "base":t[7], "pos":t[1], "pos1":t[2]}
			sent.append(word_dict)
	text.append(sent)
		                       
for sent in text:
	for d in sent:
		for i,j in d.items():
			print i,j













#			if t[1] == "動詞":
#                               print t[0] + "\t" + t[1]
