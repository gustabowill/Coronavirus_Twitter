from TwitterAPI import TwitterAPI
import tweepy

keys = dict(consumer_key='qFhbTmFTYVIoX3I4DViQJI85j',
          consumer_secret='qrt8vNood2fyCiHXrAmsZcvnoZaMRhz0Nqt52RS25G08eZphQM',
          access_token_key='1244052257257201668-0NY8vactaeJhO6QeCDkfVcoSenBXNe',
          access_token_secret='3KnF9dRGjHthFrzcw4hkbwaPqOdHmDfsrVnz9GTjP5YWf')

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
    consumer_key = "qFhbTmFTYVIoX3I4DViQJI85j"
    consumer_secret = "qrt8vNood2fyCiHXrAmsZcvnoZaMRhz0Nqt52RS25G08eZphQM"
    access_token = "1244052257257201668-0NY8vactaeJhO6QeCDkfVcoSenBXNe"
    access_token_secret = "3KnF9dRGjHthFrzcw4hkbwaPqOdHmDfsrVnz9GTjP5YWf"

    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret)

    ret = api.update_status(status=message)