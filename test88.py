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

for tweet in col.find():
	prev = "<s>"
	byegram_list = list()
	for cha in tweet["body"]:
#		byegram = prev + cha
		byegram_list.append(prev + cha)
		prev = cha
#	byegram = prev + "</s>"
	byegram_list.append(prev + "</s>")
	tweet["byegram"] = byegram_list	
	col.save(tweet)

col.create_index([("url", ASCENDING)])
col.create_index([("data", ASCENDING)])
col.create_index([("user", ASCENDING)])
col.create_index([("rt_url", ASCENDING)])
col.create_index([("reply_url", ASCENDING)])
col.create_index([("qt_url", ASCENDING)])
col.create_index([("byegram", ASCENDING)])

con.disconnect()
