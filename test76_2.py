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
	file_number = 0
	NP = []
	factor_list = []
        for text in all_text:
		write_file = open("genia_morph_dir/"+"genia_morph"+str(file_number)+".f", 'w')
                for sent in text:
                        for morph,i in zip(sent,range(len(sent))):
#				print i
               			if morph.chunk == "B-NP":
					#最初の空のリストの処理
					if len(NP) == 0:
						NP.append(morph)
						
					else:
						write_file.write("# "+" ".join(NP.w for NP in NP)+"\n")
						#冠詞の確認
						if NP[0].w == "a" or NP[0].w == "A" or NP[0].w == "an":
							factor_list.append("A")
						elif  NP[0].w == "the" or NP[0].w == "The":
							factor_list.append("THE")
						else:
							factor_list.append("None")
						#各項目の出力
						factor_list.append("w[-1]=" + b_morph.w)
                                                factor_list.append("pos[-1]=" + b_morph.pos)
                                                factor_list.append("w[+1]=" + f_morph.w)
                                                factor_list.append("pos[+1]=" + f_morph.pos)
						factor_list.append("fw=" + NP[0].w)
						factor_list.append("fpos=" + NP[0].pos)
						factor_list.append("fw|fpos=" + NP[0].w +"|"+ NP[0].pos)
						if len(NP[1:]) == 0 and NP[0]=="The":
							factor_list.append("w[0]=" + "None")
						elif NP[0].w == "the" or NP[0].w == "The" or NP[0].w == "a" or NP[0].w == "an" or NP[0].w == "A":
							factor_list.append("w[0]=" + "\t".join(NP.w for NP in NP[1:]))
						else:
							factor_list.append("w[0]=" + "\t".join(NP.w for NP in NP))
						factor_list.append("hw=" + NP[-1].w)
						factor_list.append("hpos=" + NP[-1].pos)		
						write_file.write(" ".join(factor_list)+"\n")
                                                factor_list=[]
						NP = []
						NP.append(morph)
					#名詞句の前と後のmorphの更新
                                        if i != 0 and i != len(sent)-1:
                                                b_morph = sent[i-1]
                                                f_morph = sent[i+1]
                                        elif i ==  0:
                                                b_morph = Morph("None", "None", "None", "None")
                                        else:
                                                f_morph = Morph("None", "None", "None", "None")
				elif morph.chunk == "I-NP":
					NP.append(morph)            
					#名詞句の後のmorphの更新
					if i != len(sent)-1:
						f_morph = sent[i+1]
					else:
						f_morph = Morph("None", "None", "None", "None")
		write_file.close()
		file_number += 1
						
							
