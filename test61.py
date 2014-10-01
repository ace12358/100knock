#!usr/bin/python
#-*-coding:utf-8-*-

import sys,os,CaboCha

def dir_files_list():
	files = os.listdir('/Users/kitagawayoshiaki/Dropbox/100knock/my100knock/corpus') #指定したパスのディレクトリ内のファイルをリストとして返す
	return files

if __name__ == "__main__":
	files = dir_files_list()
	file_number = 0 #ファイルnumber
	for file in files:
		cab_file = open('work_dir/japanese_caboha'+str(file_number)+'.txt', 'w')
		for line in open('corpus/'+file):
			Cab = CaboCha.Parser('--charset=UTF8')
			cab_sentense=Cab.parse(line).toString(CaboCha.FORMAT_LATTICE).strip()
			cab_file.write(cab_sentense+"\n")
		cab_file.close()
		file_number += 1
