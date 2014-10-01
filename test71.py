#!/usr/bin/python
#-*-coding:utf-8-*-
 
import sys, re, os
 
files = os.listdir('/Users/kitagawayoshiaki/Dropbox/100knock/my100knock/english_raw_data')
file_number=0
for file in files:
	write_file = open('sent-per-line-dir/english_sent-per-line_'+str(file_number)+'.txt', 'w')
	print "sent-per-line file " + str(file_number)+"creating"+"..."
	text_list = []
	for line in open('english_raw_data/'+file):
		line_list = re.split("\. |\.|\n ", line.strip())
		for line in line_list:
			text_list.append(line)
		for line in text_list:
			line = line.strip()
			if len(line) > 5:
				if line[-1]==".":
			#		print line
					write_file.write(line+"\n")
				else:
			#		print line+"."
					write_file.write(line+"."+"\n")
		text_list = []
	write_file.close()
	file_number += 1

from geniatagger import *

files = os.listdir('/Users/kitagawayoshiaki/Dropbox/100knock/my100knock/sent-per-line-dir')
file_number=0
tagger = GeniaTagger('/Users/kitagawayoshiaki/Dropbox/100knock/my100knock/geniatagger-3.0.1/geniatagger')
for file in files:
#	os.mkdir("genia_dir")
        genia_file = open('genia_dir/genia_english'+str(file_number)+'.txt', 'w')
        print "genia_file" + str(file_number)+" creating"+"..."
        for line in open('sent-per-line-dir/'+file):
		result = tagger.parse(line)
#		print result
		for tup_list in result:
			line = "\t".join(tup_list)
		#	print line
                	genia_file.write(str(line)+"\n")
        write_file.close()
        file_number += 1

