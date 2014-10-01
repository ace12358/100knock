#!usr/bin/python
#-*-coding:utf-8-*-

import sys 

print "graph knock069{"
for line in open(sys.argv[1]):
        list = line.strip().split("\t")
        print "\t\"" + list[1] + "\" -- \"" + list[2] + "\";"
print "}" 

