#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

re_nessly = re.compile(r"([a-zA-Z]+)(ness|ly)+")

for line in open(sys.argv[1]):
        list = line.strip().split("\t")
	word = list[0]
        nessly = re_nessly.match(word)
        if nessly is None:
		pass
        else:
		print nessly.group()

