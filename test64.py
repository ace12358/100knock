#coding:utf-8

import sys,os,math,re,marshal
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
                        if noun in tf_freq:
                                df_freq[noun]+=1
                noun_list = []  

	tf_idf_file = open('tf_idf_dict.txt', "wb")
    	tf_idf_dict = {}
        for noun,tf in tf_freq.items():
                tf_idf = tf*math.log(float(N)/df_freq[noun],2)
		tf_idf_dict[noun] = tf_idf
	marshal.dump(tf_idf_dict, tf_idf_file)
	tf_idf_file.close()

	n = 0
	for noun,tf_idf in sorted(tf_idf_dict.items(),key=lambda x:-x[1]):
		if not re.compile("\d").search(noun):
			print noun+"\t"+str(tf_idf)
			n += 1
			if n==100:
				break
