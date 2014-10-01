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
#               try:
                context = ":".join(context_w_list[:-1])
                w = float(context_w_list[-1])
#               except ValueError,e:
#                       print "error", e, "on context=", noun , context_w_list[0], context_w_list[1]
                noun_vec[noun][context] = w 

noun_list=[]
for line in open(sys.argv[2]):
	noun_list.append( line.strip().split()[0])
cos = defaultdict(lambda:0)
for noun1, i in zip(noun_list, range(len(noun_list))):
	for noun2 in noun_list[i:]:
		for context1, w1 in noun_vec[noun1].items():
			for context2, w2 in noun_vec[noun2].items():
				if context1 == context2:
					cos[noun1+" "+noun2] += w1*w2
#					if cos[noun1+" "+noun2]>=0.6:
#						print cos[noun1+" "+noun2],noun1,noun2
for noun1_noun2,cos in sorted(cos.items(), key = lambda x:-x[1]):
	noun1,noun2 = noun1_noun2.split()
	if cos >= 0.6 and noun1 != noun2:
			print str(cos)+"\t"+noun1+"\t"+noun2

