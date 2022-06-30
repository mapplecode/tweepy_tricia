import tweepy
from creds import CREDS as credentials
consumer_key = credentials['API_Key']
consumer_secret = credentials['API_Key_Secret']
access_token = credentials['Access_token']
access_token_secret = credentials['Access_token_secret']
app_name = credentials['NAME']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
search_words = "JulianSmithUK"
date_since = "01-01-2022"
date_since_pro = "202008130000"
numTweets = 100

# standart search
# tweets = tweepy.Cursor(api.search_tweets, q=search_words, since=date_since).items(numTweets)

# premium search
tweets=api.search_full_archive(environment_name=app_name, query=search_words, since=date_since,label=app_name)


print(tweets)