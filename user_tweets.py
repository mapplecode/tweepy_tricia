import pandas as pd
import tweepy
from creds import CREDS as credentials
# function to display data of each tweet
import csv
consumer_key = credentials['API_Key']
consumer_secret = credentials['API_Key_Secret']
access_token = credentials['Access_token']
access_token_secret = credentials['Access_token_secret']

userID = "JulianSmithUK"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name=userID,
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                           tweet_mode='extended'
                           )
print(tweets)
data=[]
for info in tweets[:3]:
     print("ID: {}".format(info.id))
     print(info.created_at)
     print(info.full_text)
     print("\n")
     data.append(["ID: {}".format(info.id) ,info.created_at ,info.full_text])

with open(userID+'scrap.csv', 'w') as f:
    write = csv.writer(f)
    for info in data:
        write.writerow(info)