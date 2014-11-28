#!usr/bin/python
#-*-cording:utf-8-*-
import sys

f1 = open('col1.txt', 'w')
f2 = open('col2.txt', 'w')
for line in open(sys.argv[1]):
    itemList = line[:-1].split('\t')
    f1.write(itemList[0]+"\n")
    f2.write(itemList[1]+"\n")
f1.close()
f2.close()
