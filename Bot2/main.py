import tweepy
import time

consumer_key = "qFhbTmFTYVIoX3I4DViQJI85j"
consumer_secret = "qrt8vNood2fyCiHXrAmsZcvnoZaMRhz0Nqt52RS25G08eZphQM"
access_token = "1244052257257201668-0NY8vactaeJhO6QeCDkfVcoSenBXNe"
access_token_secret = "3KnF9dRGjHthFrzcw4hkbwaPqOdHmDfsrVnz9GTjP5YWf"

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




