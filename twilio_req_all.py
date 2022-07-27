import tweepy
from mycreds import CREDS as credentials
consumer_key = credentials['API_Key']
consumer_secret = credentials['API_Key_Secret']
access_token = credentials['Access_token']
access_token_secret = credentials['Access_token_secret']
app_name = credentials['NAME']
label = credentials['LABEL']
Bearer_token = credentials['Bearer_Token']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
token = auth.get_authorization_url()
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
search_words = "JulianSmithUK"
date_since = "01-01-2022"
date_since_pro = "202008130000"
numTweets = 100
client = tweepy.Client( consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,)
print(client.access_token)
# standart search
# tweets = tweepy.Cursor(api.search_tweets, q=search_words, since=date_since).items(numTweets)

# premium search
tweets=api.search_full_archive( query=search_words,label=label)

try:
    for i in tweets[-1:]:
        # print(i.__dict__)
        print("ID: {}".format(i.id))
        print(i.created_at)
except Exception as e:
    print(e)
try:
    for i in tweets[:1]:
        # print(i.__dict__)
        print("ID: {}".format(i.id))
        print(i.created_at)
except Exception as e:
    print(e)
# try:
#     print(tweets.__dict__.keys())
#     print(tweets)
# except Exception as e:
#     print(e)