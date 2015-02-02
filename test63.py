#coding:utf-8

import sys,os,math
from Morph import *
from collections import defaultdict
if __name__ == "__main__":
        files = os.listdir('/Users/kitagawayoshiaki/Works/LabStudy/100knock/work_dir_n')
	N = len(files)
	tf_freq = defaultdict(lambda:0)
	#tfの計算 
        for file in files:
                for noun in open('work_dir_n/'+file):
			noun = noun.strip().split("\t")[0]
			tf_freq[noun] += 1

	#idfの計算
	noun_list = []
	df_freq = defaultdict(lambda:0)
	for file in files:
              	for noun in open('work_dir_n/'+file):
			noun=noun.strip().split("\t")[0]
			noun_list.append(noun)
		for noun in set(noun_list):
				df_freq[noun]+=1
		noun_list = []	
	
	for noun,tf in tf_freq.items():
		tf_idf=str(tf*math.log(N/df_freq[noun],2))
		print noun+"\t"+tf_idf+"\t"+str(tf)+"\t"+str(df_freq[noun])

	
