#coding:utf-8

import sys,os
from Morph import *

if __name__ == "__main__":
        files = os.listdir('/Users/kitagawayoshiaki/Dropbox/100knock/my100knock/work_dir')
        file_number = 0 
        for file in files:
                print file
                text = make_chunk_text('work_dir/'+file)
		for noun in open(sys.argv[1]):
			noun = noun.split("\t")[0]
			for sent in text:
                        	for chunk in sent:
					if chunk.noun_search(noun):
                                        	noun_syzygy = chunk.noun_syzygy()
#                                       	dst = str(sent[chunk.dst])
                                        	dst_chunk = sent[chunk.dst]
                                        	dst_morph=dst_chunk.morphs[dst_chunk.head_ID]
                                        	if not dst_morph.pos == "助詞" and not dst_morph.pos=="助動詞" and not dst_morph.pos1=="非自立語":
                                        	        dst = dst_morph.base
                                        	srcs_list=[]
                                        	for srcs_chunk_ID in chunk.srcs:
#                                       	        srcs_list.append(str(sent[srcs_chunk_ID]))
                                        	        srcs_chunk = sent[srcs_chunk_ID]
                                        	        srcs_morph=srcs_chunk.morphs[srcs_chunk.head_ID]
                                        	        if not srcs_morph.pos == "助詞" and not srcs_morph.pos=="助動詞" and not srcs_morph.pos1=="非自立語":
                                        	                srcs_list.append(srcs_morph.base)    
#                                        	srcs = "\t".join(srcs_list)
						print noun +"->"+ dst
						for src in srcs_list:
							print noun+"<-"+ src
#                                        	noun_file.write(noun_syzygy+"\t"+dst+"\t"+srcs+"\n")
                file_number+=1

