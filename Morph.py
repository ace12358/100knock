#!usr/bin/python
# -*-coding:utf-8-*-

import sys 
import CaboCha
import re
from collections import defaultdict

class Chunk:

        def __init__(self,morphs,dst,srcs,ID,head_ID):
                self.morphs = morphs
                self.dst = dst
                self.srcs = srcs
                self.ID = ID
		self.head_ID = head_ID

	def __str__(self):
                return "".join([morph.surface for morph in self.morphs])
        
	def inPos(self, str_pos):
                for morph in self.morphs:
                        if morph.pos == str_pos:
                                return True
                return False
        
	def inPos1(self, str_pos1):
                for morph in self.morphs:
                        if morph.pos1 == str_pos1:
                                return True
                return False
	def noun_syzygy(self):
		noun_cnt = 0
		noun_syzygy = ""
		for morph in self.morphs:
			if morph.pos == "名詞":
				noun_syzygy += morph.surface
				noun_cnt += 1
			elif morph.pos != "名詞":
				if noun_cnt>=1:
					return noun_syzygy
				else:
					noun_cnt = 0
					noun_syzygy = ""
		return noun_syzygy
			
	def noun_search(self, str_noun):	
		for morph in self.morphs:
			if re.compile(str_noun).search(morph.surface)==None:
				return False
			else:
				return True



class Morph:

        def __init__(self,surface,base,pos,pos1):
                self.surface = surface
		if base == "*":
                	self.base = surface
		else:
			 self.base = base
                self.pos = pos
                self.pos1 = pos1

def make_chunk_text(test_file):
        SAKI = []
        text = []
        sent = []
        srcdict = defaultdict(list)
        for line in open(test_file):
                line = line.strip()
                if line != 'EOS':
                        SAKI.append(line)
                else:
                        for line in SAKI:
                                if '* ' in line:
                                        itemList = line.split()
                                        Chu = Chunk([], int(itemList[2][:-1]), [], int(itemList[1]), int(itemList[3].split("/")[0]))
                                        srcdict[int(itemList[2][:-1])].append(int(itemList[1]))
                                        sent.append(Chu)
                                else:
                                        itemList = line.split('\t')
                                        List     = itemList[1].split(',')
                                        Chu.morphs.append(Morph(itemList[0], List[6], List[0], List[1]))
                        text.append(sent)
                        for Chu in sent:
                                Chu.srcs = srcdict[Chu.ID]
                        srcdict = defaultdict(list)
                        sent = []
                        SAKI = []
        return text

