#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import MeCab
import re

from collections import defaultdict

mapping = defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:0)))) 


for line in open(sys.argv[1]):
	tagger = MeCab.Tagger('mecabrc')
	result = tagger.parse(line)
	result2 = result.strip()
#	print result2
	sentence = result2.split("\n")
	for tok in sentence:
		to = tok.strip()
		if "\t" in to:
			t = re.split("\t|,", to)
			mapping[t[0]][t[7]][t[1]][t[2]] = line


print mapping["名"]["名"]["名詞"]["一般"]

#for a,b in mapping.items():
#	for c,d in b.items():
#		for e,f in d.items():
#			for g,h in f.items():
#				print mapping[a][c][e][g]

#                	if t[1] == "動詞":
#              			print t[0] + "\t" + t[1]

"""
		print tok
		for i in range(len(tok)):
			print tok[i]
			if '\t' in tok[i]:
				t = re.split("\t|,", tok[i])
				if t[1] == "動詞":
					print t[0] + "\t" + t[1]
			
		
"""



"""
		tok_list = re.split(u"\t|,", tok)
		if tok_list[1] == "動詞":
			print tok_list[0] + "\t" + tok_list[1]
"""
