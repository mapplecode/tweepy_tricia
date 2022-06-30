import pandas as pd
import tweepy
from creds import CREDS as credentials
# function to display data of each tweet
import csv
import  time
mps_csv = pd.read_csv('../MPsonTwitter_list_name.csv')
mpskeys = mps_csv.keys()
print(mps_csv['Screen name'])
mp_name=list()
consumer_key = credentials['API_Key']
consumer_secret = credentials['API_Key_Secret']
access_token = credentials['Access_token']
access_token_secret = credentials['Access_token_secret']



for i in mps_csv['Screen name']:
    print(i)
    userID = i
    max_id=None
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    b=True
    last_max_id = False
    while(b==True):
        print('--- ',max_id)
        tweets = api.user_timeline(screen_name=userID,
                                   count=1,
                                   include_rts = False,max_id=max_id)

        data=[]
        import time
        for info in tweets:
            print("ID: {}".format(info.id))
        print(tweets[0].id)
        if last_max_id != False and last_max_id == tweets[0].id:
            max_id = tweets[0].id
            b=False
        else:
            max_id = tweets[0].id
            last_max_id = tweets[0].id

