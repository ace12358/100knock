#usr/bin/python
#coding:utf-8

import sys
from collections import defaultdict
noun_vec = defaultdict(dict)
for line in open(sys.argv[1]):
	itemlist = line.strip().split("\t")
	noun = itemlist[0]
	for context_w in itemlist[1:]:
		context_w_list = context_w.split(":")
#		try:
		context = ":".join(context_w_list[:-1])
		w = float(context_w_list[-1])
#		except ValueError,e:
#			print "error", e, "on context=", noun , context_w_list[0], context_w_list[1]
		noun_vec[noun][context] = w


cos = defaultdict(lambda:defaultdict(lambda:0))
noun1 = "鱗"
noun2 = "甲殻"
for context1, w1 in noun_vec[noun1].items():
	 for context2, w2 in noun_vec[noun2].items():
		if context1 == context2:
			cos[noun1][noun2] += w1*w2
print str(cos[noun1][noun2])+"\t"+noun1+"\t"+noun2
