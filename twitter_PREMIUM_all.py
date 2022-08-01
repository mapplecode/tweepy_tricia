import time

import tweepy
from mycreds import CREDS as credentials
from date_producer import get_total_weeks
import pandas as pd
mps_csv = pd.read_csv('MPsonTwitter_list_name.csv')
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


client = tweepy.Client( consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,)

# premium search

USER_TWEETS_IDS = list()

def get_twets(search_words):
    existing_ids = list()
    all_dates = get_total_weeks()
    for key,val in all_dates.items():
        date_start= str(val).split(',')[0][:-2]
        date_stop= str(val).split(',')[1][:-2]
        tweets=api.search_full_archive( query=search_words,label=label,fromDate=date_start,toDate=date_stop)
        try:
            read_file = open('id_folder/' + str(search_words) + '.txt', 'r').read()
            existing_ids = read_file.split('\n')
        except Exception as e:
            print(e)
        try:
            for i in tweets:
                print("ID: {}".format(i.id) , ' --- ','CREATED: ',i.created_at)
                USER_TWEETS_IDS.append(str(i.id))
                tweet_user_file = open('id_folder/' + str(search_words) + '.txt', 'a')
                if str(i.id) not in existing_ids:
                    tweet_user_file.write(str(i.id) + '\n')
                    tweet_user_file.close()
                    print(str(i.id),'ADDED TO ---->',search_words ,' TXT FILE')
        except Exception as e:
            print(e)
        time.sleep(120)

for i in mps_csv['Screen name']:
    print(i)
    get_twets(search_words=i)
    time.sleep(600)