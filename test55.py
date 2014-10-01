#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re
from test54 import *
re_marks = re.compile(u"[。、「」『』]")
dst = ""
srcs = ""
text = main()
for sent in text:
	for Ch in sent:
		for w in Ch.morphs:
			if re_marks.search(w.surface.decode("utf-8")) is None:
				dst += w.surface
		for w in sent[Ch.dst].morphs:
			if  re_marks.search(w.surface.decode("utf-8")) is None:
				srcs += w.surface
		print dst + "\t" + srcs
		dst = ""
		srcs = ""				




