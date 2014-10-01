#!/usr/bin/python
#-*-cording:utf-8-*-

import sys
from collections import defaultdict
itemList1=[]

for line in open(sys.argv[1]):
        itemList = line.strip().split('\t')
        itemList1.append(itemList[1])

#for address in itemList1:
#        print address

addressDict = defaultdict(lambda: 0)

for w in itemList1:
        if w in addressDict:
                addressDict[w] += 1
        else:
                addressDict[w] = 1
for i, j in sorted(addressDict.items(), key = lambda x:-x[1]):
        print "%s\t%r" %(i, j)
