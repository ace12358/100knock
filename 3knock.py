#!usr/bin/python
#-*-coding:utf-8-*-
"""
excution
python 3knock.py address.txt
"""
__author__  = "@Ace12358 <ace1235813@gmail.com>"
__version__ = "0.0"
__date__    = "14 Oct 2014"

import sys

def main():
    """
    main function
    """
    f1 = open('col1.txt', 'w')
    f2 = open('col2.txt', 'w')
    for line in open(sys.argv[1]):
        itemList = line[:-1].split('\t')
        f1.write("%s\n" %itemList[0])
        f2.write("%s\n" %itemList[1])
    f1.close()
    f2.close()

if __name__=="__main__":
    main()
