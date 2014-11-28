#!/usr/bin/python
# -*-coding:utf-8-*-
"""
excution
python 2knock.py address.txt
"""

__author__  = "@Ace12358 <ace1235813@gmail.com>"
__version__ = "0.0"
__date__    = "14 Oct 2014"

import sys

def main():
    """
    main function
    """
    for line in open(sys.argv[1]):
	    print line.strip().replace("	"," ")

if __name__ == "__main__":
    main()
