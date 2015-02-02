#!/usr/bin/python
#coding:utf-8

import sys
import json
from pymongo import *

data = json.load(open(sys.argv[1]))

#for line in data:
#	for key,value in line.items():
#		print key
#	if key == "":
#		pass
#	print "------------------------------"

#コネクション作成
con = Connection("fomalhaut", 27017)

#コネクションからtestデータベースを取得
db = con.nlp100_kitagawa
col = db.tweets

for i in data:
	tw = {}
	tw["url"] = "http://twitter.com/"+i["user"]["screen_name"]+"/status/"+i["id_str"]
	tw["data"] = i["created_at"]
	tw["user"] = i["id"]
        tw["nickname"] = i["user"]["name"]
        tw["body"] = i["text"]
        tw["freq_rt"] = i["retweet_count"]
	if "retweeted_status" in i:
		tw["rt_url"] = "http://twitter.com/"+i["user"]["screen_name"]+"/status/"+i["retweeted_status"]["id_str"]
	tw["rt_url"] = None
	if i["in_reply_to_screen_name"] is not None:
		tw["reply_url"] = "http://twitter.com/"+i["in_reply_to_screen_name"]+"/status/"+i["in_reply_to_status_id_str"]
	tw["reply_url"] = None
	col.insert(tw)
	#tw["freq_replied"]
        #tw["qt_url"]
        #tw["freq_qted"]
#	col.insert({"url":i["source"],"data":i["created_at"],\
#		"user":i["id"], "nickname":i["user"]["name"],\
#		"body":i["text"], "freq_rt":i["retweet_count"]})

con.disconnect()
