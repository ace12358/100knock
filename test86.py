#!/usr/bin/python
#coding:utf-8

import sys
import json
import pymongo
from pymongo import *


#コネクション作成
con = Connection('127.0.0.1', 27017)

#コネクションからデータベースを取得
db = con.nlp100_kitagawa
col = db.tweets

for tweet in col.find({"url" : "http://twitter.com/basukeekuroko/status/485830078509486080"}):
	print tweet["nickname"],tweet["body"]
for tweet in col.find({"url" : "http://twitter.com/mintiatime/status/485830078513700864"}):
	print tweet["nickname"],tweet["body"]

con.disconnect()
