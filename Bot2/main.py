import tweepy

consumer_key = "th7WpXxsMfDCdqUXnSl2A7vpl"
consumer_secret = "SPleOqajbExm8LA9NJw8WCBZAJ1W31njgjS51mCuGMefnqqIgD"
access_token = "1241503413281718272-B1rBigiBZF2kJR9hvOXwLsswDhSymX"
access_token_secret = "uimFLngVmMARX2KpgAzGEwW2pcsweaPtsQQJNluqMXW0D"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = '1244052257257201668'
term = 'Detalhes na Thread'

while True:
  for tweet in tweepy.Cursor(api.user_timeline,user, term).items(30):
    texto = tweet.text
    if '#Coronavírus' in texto:
      try:
        tweet.retweet()
        print(texto)
          
      except:
        print('Não há tweet para ser retweetado')




