#!/usr/bin/python
#-*-coding:utf-8-*-
 
import sys
import re
 
re_sentence = re.compile(r"(\.) ([A-Z])")
 
for line in open(sys.argv[1]):
    m = re_sentence.split(line.strip())
 
m = [m[0][0], m[0][1:]] + m[1:-1] + [m[-1][0:len(m[-1])-1], m[-1][-1]]
 
for i in range(0, len(m)-1, 3):
    print m[i]+m[i+1]+m[i+2]
 



"""
#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

re_sentence = re.compile(r"(\.) [A-Z]")

for line in open (sys.argv[1]):
	m = re_sentence.split(line.strip())

m = [m[0][0], m[0][1:] + m[1:-1] + [m[-1][0:len(m[-1]-1)], m[-1][-1]]

for i in range(0, len(m)-1, 3):
	print m[i]+m[i+1]+m[i+2]
"""
