#user/bin/python
#-*-coding:utf-8-*-

import math,sys,os,marshal

files = os.listdir('/Users/kitagawayoshiaki/Dropbox/100knock/my100knock/work_dir_n') #指定したパスのディレクトリ内のファイルをリストとして返す

from collections import defaultdict
noun_context = defaultdict(lambda:defaultdict(lambda:0))#[名詞][周辺単語]=周辺単語の頻度

for file in files:
        for line in open("work_dir_n/"+file):
                list = line.strip().split("\t")
                noun = list[0]
                dst = list[1]
                srcs = list[2:]
		noun_context[noun]["-> "+dst] += 1
		for src in srcs:
			noun_context[noun]["<- "+src] += 1

noun_vec_norm = defaultdict(lambda:0)
for noun, context_dict in noun_context.items():
	for context, freq in context_dict.items():
		noun_vec_norm[noun] += freq*freq

#for noun, context_dict in noun_context.items():
	print noun+"\t",
	for context, freq in context_dict.items():
		print context+":"+str(float(freq)/math.sqrt(noun_vec_norm[noun]))+"\t",
	print 
