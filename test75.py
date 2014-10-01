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
	NP = []
        for text in all_text:
                for sent in text:
                        for morph,i in zip(sent,range(len(sent))):
               			if morph.chunk == "B-NP":
					#frontの成分をここで出力（タイミングがここ）
					if len(NP) == 0:
						pass
					else:
						print "w[+1]=" + f_morph.w + "\t",
						print "pos[+1]=" + b_morph.pos + "\t"
					#名詞句の前と後のmorphの更新
					if i != 0 and i != len(sent)-1:
						b_morph = sent[i-1]
						f_morph = sent[i+1]
					elif i ==  0:
						b_morph = Morph("None", "None", "None", "None")
					else:
						f_morph = Morph("None", "None", "None", "None")

					#最初の空のリストの処理
					if len(NP) == 0:
						NP.append(morph)
					else:
						print "# "+" ".join(NP.w for NP in NP)
						#冠詞の確認
						if NP[0].w == "a" or NP[0].w == "A":
							print "A" + "\t",
						elif  NP[0].w == "the" or NP[0].w == "The":
							print "THE" + "\t",
						else:
							print "None" + "\t",
						#各項目の出力
						print "w[-1]=" + b_morph.w + "\t",
						print "pos[-1]=" + b_morph.pos + "\t",
						print "fw=" + NP[0].w + "\t",
						print "fpos=" + NP[0].pos + "\t",
						print "fw|fpos=" + NP[0].w +"|"+ NP[0].pos + "\t",
						if len(NP[1:]) == 0 and NP[0]=="The":
							print "w[0]=" + "None" + "\t",
						elif NP[0].w == "the" or NP[0].w == "The" or NP[0].w == "a" or NP[0].w == "A":
							print "w[0]=" + " ".join(NP.w for NP in NP[1:]),
						else:
							print "w[0]=" + " ".join(NP.w for NP in NP),
						print "hw=" + NP[-1].w + "\t",
						print "hpos=" + NP[-1].pos + "\t",				
						NP = []
						NP.append(morph)
				elif morph.chunk == "I-NP":
					NP.append(morph)            
					#名詞句の後のmorphの更新
					if i != len(sent)-1:
						f_morph = sent[i+1]
					else:
						f_morph = Morph("None", "None", "None", "None")

						
							
