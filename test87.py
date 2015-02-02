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

count = 0
for tweet in col.find().sort("freq_rt",pymongo.DESCENDING):
	count += 1
	print tweet["nickname"],tweet["body"],tweet["freq_rt"]
	if count == 10:
		break
con.disconnect()
