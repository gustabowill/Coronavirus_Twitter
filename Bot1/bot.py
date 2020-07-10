from TwitterAPI import TwitterAPI
import tweepy

keys = dict(consumer_key='th7WpXxsMfDCdqUXnSl2A7vpl',
          consumer_secret='SPleOqajbExm8LA9NJw8WCBZAJ1W31njgjS51mCuGMefnqqIgD',
          access_token_key='1241503413281718272-B1rBigiBZF2kJR9hvOXwLsswDhSymX',
          access_token_secret='uimFLngVmMARX2KpgAzGEwW2pcsweaPtsQQJNluqMXW0D')

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
    consumer_key = "th7WpXxsMfDCdqUXnSl2A7vpl"
    consumer_secret = "SPleOqajbExm8LA9NJw8WCBZAJ1W31njgjS51mCuGMefnqqIgD"
    access_token = "1241503413281718272-B1rBigiBZF2kJR9hvOXwLsswDhSymX"
    access_token_secret = "uimFLngVmMARX2KpgAzGEwW2pcsweaPtsQQJNluqMXW0D"

    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret)

    ret = api.update_status(status=message)