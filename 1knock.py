#!/usr/bin/python
#-*-cording:utf-8-*-
import sys

"""
excution
python 1knock.py address.txt
"""
__author__  = "@Ace12358 <ace1235813@gmail.com>"
__version__ = "0.0"
__date__    = "14 Oct 2014"

def main():
    """
    main function
    """
    num_line = 0
    for line in open(sys.argv[1]):
        num_line += 1
    print num_line

if __name__ == "__main__":
    main()
