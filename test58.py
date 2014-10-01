#!/usr/bin/python
#-*-coding:utf-8-*-

import sys 
import re
from test54 import *
re_marks = re.compile(u"[。、「」『』]|。")
srcs = ""
dst = ""
text = main()
for sent in text:
        for Ch in sent:
		if len(Ch.srcs) >= 2:
                	for w in Ch.morphs:
                        	if re_marks.search(w.surface, re.U) is None:
                                	        srcs += w.surface
                	for i in Ch.srcs:
				for w in sent[int(i)].morphs:
	                        	if re_marks.search(w.surface, re.U) is None:
	                                	dst += w.surface
				print dst + "\t" + srcs
				dst = ""
			print "-------------------------------------------------\n"
                srcs = ""

