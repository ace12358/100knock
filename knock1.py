#!/usr/bin/python
#-*-cording:utf-8-*-
import sys

def main():
    num_line = 0
    for line in open(sys.argv[1]):
        num_line += 1
    print num_line

if __name__ == "__main__":
    main()
