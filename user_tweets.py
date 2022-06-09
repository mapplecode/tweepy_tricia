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
# print(tweets)
data=[]
for info in tweets[:3]:
     print("ID: {}".format(info.id))

     retweets_list = api.get_retweets(info.id)
     # folowers = api.get_followers(userID)
     # for folowe in folowers:
     #     print(folowe.screen_name)
     users_retweeted = ''
     # printing the screen names of the retweeters
     for retweet in retweets_list:
         users_retweeted += retweet.user.screen_name+' , '
     data.append(["ID: {}".format(info.id), info.created_at, info.full_text,users_retweeted])
with open(userID+'scrap.csv', 'w') as f:
    write = csv.writer(f)
    for info in data:
        write.writerow(info)