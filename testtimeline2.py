#!/usr/bin/python
#-*-coding:utf-8-

from tweepy.streaming import StreamListener, Stream
from tweepy.auth import OAuthHandler
import chardet
from datetime import timedelta

def getOauth():
	consumerKey = 'jCLoeEVXxq4ygfPsJma33jUTN'
	consumerSecret = 'yPSDOl17fqBqaSKfDa8rDlaHaHBZ6llyClcLRO1G3kV6cIWnWz'
	accessKey = '495476602-OalwRLSU9poetl3HuQiX9AZ8tcd9QQuhfHLjQ8xf'
	accessSecret = 'bQhekPGvSn87VmxSuPtP8ODCXFzZKJ1zoZnRvMThVLNof'
 
	auth = OAuthHandler(consumerKey, consumerSecret)
	auth.set_access_token(accessKey, accessSecret)
	return auth
 
 
class AbstructListener(StreamListener):
	def on_status(self, status):
		#try:
			#status=unicode
			name = status.author.name
			name = name.encode('utf8')
			id = status.author.id
			#id=user_id.encode('utf8')
			screen_name = status.author.screen_name
			s_name=screen_name.encode('utf8')
			text = status.text
			text = text.encode('utf8')
			#icon_path = status.author.profile_image_url
			status.created_at += timedelta(hours=9)
			created_at = status.created_at
			src=status.source
			src=src.encode('utf8')
			print created_at
			print id
			print name 
			print text
			print s_name
			print src
			print "___"
			print 
		#except:
			#pass

	def on_error(self, status):
		print status
 
if __name__ == '__main__':
	
	auth = getOauth()
	stream = Stream(auth, AbstructListener(), secure=True)
	query1 = '横浜'.decode('utf8')
	#query2 = 'usogui'.decode('utf8')
	#query = query.encode('ascii')
	query = []
	query.append(query1)
	#query.append(query2)
	stream.filter(track=query)

	#query.append(query2)
	#stream.filter(track=query)

