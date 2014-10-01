#usr/bin/python
#coding:utf-8

import sys
from collections import defaultdict

#クラス間の最長距離を計算
def furthest_neighbor(class1, class2):
	cos_min = 1.0
	for word1 in class1:
		for word2 in class2:
			if not word1+" "+word2 in cos_dict:
				cos_dict[word1+" "+word2] = 1.0
			if cos_dict[word1+" "+word2] < cos_min:
				cos_min = cos_dict[word1+" "+word2]
	if cos_min != 1.0:
		return cos_min
	else:
		return 0.0

if __name__ == "__main__":
	#読み込み
	cos_dict = {}
	word_dict = {}
	for line in open(sys.argv[1]):
		itemlist = line.strip().split()
		cos = float(itemlist[0])
		word1, word2 = itemlist[1], itemlist[2]
		word_dict[word1] = 0
		word_dict[word2] = 0
		cos_dict[word1+" "+word2] = cos
		cos_dict[word2+" "+word1] = cos
	
	#初期クラスの作成
	class_list = [] 
	for word in word_dict.keys():
		word = [word]
		class_list.append(word)
	
	while(len(class_list)!=int(sys.argv[2])):
		d_max = 0
		best_class = tuple
		for class1 in class_list:
			for class2 in class_list:
				if class1 != class2:
					d = furthest_neighbor(class1, class2)
					if d >= d_max:
						d_max = d
						best_class = (class1, class2)
		class1, class2 = best_class[0], best_class[1]
		class_list.append(class1 + class2)
		class_list.remove(class1)
		class_list.remove(class2)


	a = 0
	for cls in class_list:
		print "class" + str(a),
		for class_word in cls:
			print class_word.decode("utf-8"),
		print
		a += 1







		

