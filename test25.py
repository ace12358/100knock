#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

re_priod = re.compile(r"(.+)(\.|\,)+")

for line in open(sys.argv[1]):
        word = line.strip().split(" ")
#        word.append("\n")
        for i in range(len(word)):
                priod = re_priod.match(word[i])
                if priod is None:
                        print word[i],
			print "\t",
                	print word[i].lower()
		else:
                        print priod.group(1),
			print "\t",
			print priod.group(1).lower()
                        print priod.group(2),
			print "\t",
			print priod.group(2).lower()
#print ""
