#!/usr/bin/python
# -*-coding:utf-8-*-

import sys
import re
from collections import defaultdict

tweet = ""
account = ""

tweet_dict = defaultdict(list)

re_account = re.compile(r"([0-9a-zA-Z_]{1,15}) : ")
re_RT = re.compile(r"RT @([0-9a-zA-Z_]{1,15}): ")
re_atstart = re.compile(r"@([0-9a-zA-Z_]{1,15})")
re_ABC = re.compile(r"([一-龠])+\(([A-Z]+)\)")
re_name = re.compile(r"([一-龠ぁ-んァ-ヶー]{1,20})(ちゃん|氏|さん|君)")
re_senaddress = re.compile(r"仙台市[一-龠0−9\-]{1,50}")
re_kaomoji = re.compile(r"(\([^一-龠]+\))")

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
                kaomoji = re_kaomoji.search(tweet1)
                if kaomoji is None:
                        pass
                else:
                        print kaomoji.group()
