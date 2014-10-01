#/usr/bin/python
#coding:utf-8

import os
from test72 import *

if __name__ == "__main__":
        files = os.listdir("/Users/kitagawayoshiaki/Dropbox/100knock/my100knock/genia_dir")
	#テキストの読み込み
        all_text = []
        for file in files:
                f = "genia_dir/"+file
                text = make_text(f)
                all_text.append(text)
	#名詞句を探す
	NP = []
        for text in all_text:
                for sent in text:
                        for morph in sent:
               			if morph.chunk == "B-NP":
					#最初の空のリストの処理
					if len(NP) == 0:
						NP.append(morph.w)
					else:
						print "# "+" ".join(NP)
						NP = []
						NP.append(morph.w)
				
				elif morph.chunk == "I-NP":
					NP.append(morph.w)                

