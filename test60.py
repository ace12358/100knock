#!usr/bin/python
#-*-coding:utf-8-*-

import sys

print "digraph knock060{"
for line in open(sys.argv[1]):
	line = line.strip()
	line = line.replace('\"', r'\"')
	list = line.split("\t")
	print "\t\"" + list[0] + "\" -> \"" + list[1] + "\";"
print "}"

