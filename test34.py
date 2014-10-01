#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import marshal
from collections import Counter

f = open(sys.argv[1], 'rb')

count = Counter()
marshal_list = []

for line in marshal.load(f):
        marshal_list.append(line)

for line2 in open(sys.argv[2]):
        list = line2.strip().split("\t")
        word = list[2]

        for i in range(len(marshal_list)):
                if word in marshal_list[i]:
                        count[word] += 1
        if count[word] != 0:
                pass
        else:
                print word
