#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import matplotlib.pyplot as plt

listnum =[]
i = 1
x = []
y = []

for line in open(sys.argv[1]):
	list = line.strip().split('\t')
	x.append(list[0].decode("utf8"))
	y.append(int(list[1]))
	listnum.append(i)
	i += 1

#for i in range(len(x)):
#	print listnum[i],y[i]
#print type(y[1])

plt.bar(listnum, y)
#plt.xticks(listnum, x)
plt.show()
















"""
fig, axes = plt.subplots(figsize=(7,4)) 
axes.plot(x, y, 'r')
axes.set_xlabel('verb') #x軸のラベルを設定します
axes.set_ylabel('freq') #y軸のラベルを設定します
axes.set_title('verb_freq') #titleを設定します
fig.show
fig.savefig("test49figure.png") #これで画像を保存. オプション引数でdpiも指定できる
"""
