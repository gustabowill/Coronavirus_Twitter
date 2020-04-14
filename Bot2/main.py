import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = ''

while True:
  for tweet in tweepy.Cursor(api.user_timeline,user, term).items(30):
    texto = tweet.text
    if '#Coronavírus' in texto:
      try:
        tweet.retweet()
        print(texto)
          
      except:
        print('Não há tweet para ser retweetado')




