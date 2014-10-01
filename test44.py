#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import MeCab
import re

for line in open(sys.argv[1]):
        tagger = MeCab.Tagger('mecabrc')
        result = tagger.parse(line)
        result2 = result.strip()
        sentence = result2.split("\n")
        for tok in sentence:
                to = tok.strip()
                if "\t" in to:
                        t = re.split("\t|,", to)
                        if t[2] == "サ変接続":
                                print t[0] + "\t" + t[2]

