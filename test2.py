#!/usr/bin/python
# -*-cording:utf-8-*-

import sys

def main():
    for line in open(sys.argv[1]):
	    print line.strip().replace("	"," ")

if __name__ == "__main__":
    main()
