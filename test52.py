#!usr/bin/python
# -*-coding-utf-8-*-

import sys
import CaboCha
import re

class Morph:

	def __init__(self,surface,base,pos,pos1):
		self.surface = surface
		self.base = base
		self.pos = pos
		self.pos1 = pos1


def main():
	for line in open(sys.argv[1]):
		Morph_class_list = []
		line = line.strip()
		if not ("* " in line or "EOS" in line):
			item = re.split("\t|,", line)
			M = Morph(item[0], item[7], item[1], item[2])
			Morph_class_list.append(M)
			print M.surface, M.base, M.pos, M.pos1
			








#def main():
#	Morph_text = []
#	for line in open(sys.argv[1]):
#		Morph_sentence = []
#		Cabo = CaboCha.Parser('--charset=UTF8')
#		Cabo_LAT = Cabo.parse(line).toString(CaboCha.FORMAT_LATTICE)
#		Cabo_bunsetu_list = Cabo_LAT.split("* ")
##		print Cabo_bunsetu		for Cabo_bunsetu in Cabo_bunsetu_list:
#			print Cabo_bunsetu 





if __name__ == "__main__":
	main()
