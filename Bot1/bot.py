from TwitterAPI import TwitterAPI
import tweepy

keys = dict(consumer_key='',
          consumer_secret='',
          access_token_key='',
          access_token_secret='')

api = TwitterAPI(**keys)

def login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    ret = {}
    ret['api'] = api
    ret['path'] = auth
    return api

def post_tweets(message):
    consumer_key = "jtHg4Sfdk3D3b0a4Ub8TqTrc2"
    consumer_secret = "qSwc34rMmAD2c1EYXIZXU8tA5UyvEPr8Ln6cQON6LwJnLlxG6W"
    access_token = "1241503413281718272-ScNoFrdQ9XeRnbRMc7PaddqDFofU6j"
    access_token_secret = "DJQo0DqzqDL04B929xGvSa06f1UupgfavpQqqqaYMfT9J"

    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret)

    ret = api.update_status(status=message)
