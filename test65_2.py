#coding:utf-8

import sys,os

noun100 = []
for line in open(sys.argv[1]):
	noun100.append(line.strip().split()[0])

files = os.listdir('/Users/kitagawayoshiaki/Dropbox/100knock/my100knock/work_dir_n') #指定したパスのディレクトリ内のファイルをリストとして返す
for file in files:
	for line in open("work_dir_n/"+file):
		list = line.strip().split("\t")
		noun = list[0]
		if noun in noun100:
			dst = list[1]
			srcs = list[2:]
			print noun +"->"+ dst
			for src in srcs:
				print noun +"<-"+ src	
