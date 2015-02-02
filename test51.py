#!/usr/bin/python
# coding=utf-8
 
import CaboCha
import sys

def main():
	for line in open(sys.argv[1]):
		Cabo = CaboCha.Parser('--charset=UTF8')
		print Cabo.parse(line).toString(CaboCha.FORMAT_LATTICE),
		
 
def test():
 
    c = CaboCha.Parser('--charset=UTF8')
    sentence = u"マリカーをやりたいけどできないよ。100本ノックが待ってるよ".encode('utf-8')
 
    print c.parseToString(sentence)
 
    tree = c.parse(sentence)
    print "--------------TREE形式--------------"
    print tree.toString(CaboCha.FORMAT_TREE)
    print "--------------LATTICE形式--------------"
    print tree.toString(CaboCha.FORMAT_LATTICE)
    print "--------------FORMAT_XML形式--------------"
    print tree.toString(CaboCha.FORMAT_XML)
 
if __name__ == '__main__':
#    test()
    main()

