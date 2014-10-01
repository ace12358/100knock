#!/usr/bin/python
# -*-coding:utf-8-*-

import sys
import re
from collections import defaultdict

tweet = ""
account = ""

tweet_dict = defaultdict(list)

re_account = re.compile(r"([0-9a-zA-Z_]{1,15}) : ")

for line in open(sys.argv[1]):
        result_match = re_account.match(line)
        if result_match is None:
                tweet = tweet + line
        else:
                if account == "":
                        pass
                else:
                        tweet = tweet[:-1]
                        tweet_dict[account].append(tweet)
                account = result_match.group(1)
                tweet = line[len(result_match.group()):]


for key, value in tweet_dict.items():
        for tweet1 in value:
                if re.search(r"なう$", tweet1):
                        print "----------ツイート-----------------------"
                        print tweet1
                        print "-----------------------------------------"
                        print ""
                        print ""
			print ""
			print ""
			print ""
                        print ""
                        print ""
                else:
                        pass

