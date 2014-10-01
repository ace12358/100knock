#!usr/bin/python
# -*-coding:utf-8-*-

import sys
import re
import os
from collections import defaultdict

class Morph:

        def __init__(self,w,lem,pos,chunk):
                self.w = w
                self.lem = lem
                self.pos = pos
                self.chunk = chunk

def make_text(test_file):
        text = []
        sent = []
        for line in open(test_file):
                line = line.strip()
                if line.split()[0]== '.':
			itemList = line.split("\t")
			morph = Morph(itemList[0],itemList[1],itemList[2],itemList[3])
			sent.append(morph)
                        text.append(sent)
			sent = []
                else:
			itemList = line.split("\t")
			morph = Morph(itemList[0],itemList[1],itemList[2],itemList[3])
			sent.append(morph)
        return text

if __name__ == "__main__":
	files = os.listdir("/Users/kitagawayoshiaki/Dropbox/100knock/my100knock/genia_dir")
	all_text = []
	for file in files:
		f = "genia_dir/"+file
		text = make_text(f)
		all_text.append(text)
	for text in all_text:
		for sent in text:
			for morph in sent:
				print morph.w, morph.lem, morph.pos, morph.chunk
	
