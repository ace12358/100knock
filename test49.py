#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import matplotlib.pyplot as plt
from collections import defaultdict

#word = defaultdict(lambda: 0)
word_list = []

for line in open(sys.argv[1]):
        list = line.strip().split('\t')
	word_list.append(int(list[1])) 


print word_list

fig = plt.figure(1)
plt.hist(word_list, bins = 200, range = (0,50))
plt.title(r"test49", fontsize=20)
#plt.xlab
plt.savefig("test49.eps")
plt.show()













#for i in range(len(x)):
#       print listnum[i],y[i]
#print type(y[1])

#plt.bar(list(word.key()), word.value())
#plt.xticks(listnum, x)
#plt.show()



