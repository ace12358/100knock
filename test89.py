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
	frag = 0
	for byegram in tweet["byegram"]:
		if byegram == u"神田":
			frag = 1
	if frag == 1:
		print tweet["nickname"], tweet["body"]

con.disconnect()
