#!/usr/bin/python
#coding:utf-8

import sys
import json
import pymongo
from pymongo import *


#コネクション作成
con = Connection('127.0.0.1', 27017)

#コネクションからtestデータベースを取得
db = con.nlp100_kitagawa
col = db.tweets

tweet_list = []
find_str = unicode(sys.argv[1], "utf-8")

for tweet in col.find():
	if find_str in tweet["body"]:
		tweet_list.append(tweet)

for tweet in sorted(tweet_list, key=lambda x:-x["freq_rt"]):
	print tweet["nickname"], tweet["body"]

con.disconnect()
