from TwitterAPI import TwitterAPI
import tweepy

keys = dict(consumer_key='HERE',
          consumer_secret='HERE',
          access_token_key='HERE',
          access_token_secret='HERE')

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
    consumer_key = "HERE"
    consumer_secret = "HERE"
    access_token = "HERE"
    access_token_secret = "HERE"

    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret)

    ret = api.update_status(status=message)
