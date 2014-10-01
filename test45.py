#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import MeCab
import re

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
	if "の"==longlist[i-10] and longlist[i-19]=="名詞" and longlist[i+1] == "名詞":
		print longlist[i-20] + longlist[i-10] + longlist[i]

