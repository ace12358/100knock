#!usr/bin/python
# -*-coding-utf-8-*-

import sys
import CaboCha
import re
from collections import defaultdict

class Chunk:

        def __init__(self,morphs,dst,srcs,ID):
                self.morphs = morphs
                self.dst = dst
                self.srcs = srcs
                self.ID = ID

class Morph:

        def __init__(self,surface,base,pos,pos1):
                self.surface = surface
                self.base = base
                self.pos = pos
                self.pos1 = pos1

def main():
	text = []
        sent = []
        Morph_class_list = []
        D_p = defaultdict(lambda:[])
        setu_i = 0
        for line in open(sys.argv[1]):
                line = line.strip()
                if not ("* " in line or "EOS" in line):
                        item = re.split("\t|,", line)
                        M = Morph(item[0], item[7], item[1], item[2])
                        Ch.morphs.append(M)
		elif "* " in line:
                        item = line.split()
                        D = int(item[2][:-1])
                        D_p[D].append(str(setu_i))
                        Ch = Chunk([],D,[],setu_i)
                        setu_i += 1
                        sent.append(Ch)

                elif "EOS" in line:
                        for Ch in sent:
                                Ch.srcs += D_p[Ch.ID]
#                                for morph in Ch.morphs:
#                                       print morph.surface, morph.base, morph.pos, morph.pos1, Ch.dst, Ch.srcs,Ch.ID
                        text.append(sent)
			Morph_class_list = []
                        D_p = defaultdict(lambda:[])
                        setu_i = 0
                        sent = []

	return text
if __name__ == "__main__":
        main()

