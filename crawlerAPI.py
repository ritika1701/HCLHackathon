import tweepy
from tweepy import OAuthHandler
 
consumer_key = '5huoCPKtYJHCGJ2KUP7FCAua8'
consumer_secret = '7LKpTk0KjPTP0XUbEYrTjQL6Ds4h93rAWokTjFpFrOLxvCrvcW'
access_token = '878350613490348032-IgVTSuBuiI6ag9IBcr8fAKmRBMQ4YZn'
access_secret = '	gE1JUR6EwIZkTIlYk2LlKkYZNG9aedo7GOjgsNAPeFEtU'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)