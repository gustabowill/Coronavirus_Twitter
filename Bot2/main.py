import tweepy
import time

consumer_key = "OrIocvu3tGJPLSXjfXeTMgLc0"
consumer_secret = "Ay4ZvFVpklYDOjD0y7CZf5HbV2nzZTdEJ88AeTBCQwxLcnywnn"
access_token = "1244052257257201668-n0Rm4GMsbHuZRXkHuNm4y9ZJFDuppQ"
access_token_secret = "YJvISxdcPF1qwB4lePUkzMHfomyhqky2kSDlrxFi1EJYr"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = '1241503413281718272'

while True:
  for tweet in tweepy.Cursor(api.user_timeline,user).items(20):
    texto = tweet.text
    if 'Data:' in texto:
      try:
        tweet.retweet()
        print(texto)
          
      except:
        print('Não há tweet para ser retweetado')
  time.sleep(1800) 




