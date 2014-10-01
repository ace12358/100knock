#coding:utf-8

import sys,os,math
from Morph import *
from collections import defaultdict

if __name__ == "__main__":
        files = os.listdir('/Users/kitagawayoshiaki/Dropbox/100knock/my100knock/work_dir')
        file_number = 0 
        for file in files:
                print file
                text = make_chunk_text('work_dir/'+file)
                for noun in open(sys.argv[1]):
			m = 0
                        noun = noun.split("\t")[0]
                        for sent in text:
                                for chunk in sent:
                                        if chunk.noun_search(noun):
						context_freq = defaultdict(lambda:0)
                                                dst_chunk = sent[chunk.dst]
                                                dst_morph=dst_chunk.morphs[dst_chunk.head_ID]
                                                if not dst_morph.pos == "助詞" and not dst_morph.pos=="助動詞" and not dst_morph.pos1=="非自立語":
                                                        dst = dst_morph.base
						context_freq[dst] += 1
                                                srcs_list=[]
                                                for srcs_chunk_ID in chunk.srcs:
                                                        srcs_chunk = sent[srcs_chunk_ID]
                                                        srcs_morph=srcs_chunk.morphs[srcs_chunk.head_ID]
                                                        if not srcs_morph.pos == "助詞" and not srcs_morph.pos==">助動詞" and not srcs_morph.pos1=="非自立語":
						               context_freq[srcs_morph.base] += 1
						               srcs_list.append(srcs_morph.base)
						norm2 = 0.0
						for w,freq in context_freq.items():
							norm2 += freq*freq
						norm = math.sqrt(norm2)
                                                print noun +"->"+ dst+"_"+str(m)+":"+str(context_freq[dst]/norm)+"\t",
                                                for src in srcs_list:
                                                       print "<-"+ src+"_"+str(m) +":"+str(context_freq[src]/norm)+"\t",
						print ""
						m += 1
                file_number+=1

