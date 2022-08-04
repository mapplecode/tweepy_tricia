import os.path
import time

import tweepy
from creds import CREDS as credentials
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

def get_twets(search_words,st_date=''):
    existing_ids = list()
    all_dates = get_total_weeks()
    for key,val in all_dates.items():
        date_start= str(val).split(',')[0][:-2]
        if st_date != '':
            date_start = st_date
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
                if str(i.id)+'---'+str(i.created_at) not in existing_ids:
                    tweet_user_file.write(str(i.id)+'---'+str(i.created_at) + '\n')
                    tweet_user_file.close()
                    print(str(i.id),'ADDED TO ---->',search_words ,' TXT FILE')
        except Exception as e:
            print(e)
        time.sleep(120)

for i in mps_csv['Screen name']:
    # print(i)
    if os.path.exists( 'id_folder/' + str(i) + '.txt'):
        # try:
        #     existing_date_list = list()
        #     old_file = 'id_folder/' + str(i) + '.txt'
        #     old_file = open(old_file,'r').read().split('\n')
        #     for text in old_file:
        #         try:
        #             date = text.split('---')[1]
        #             existing_date_list.append(date)
        #         except:
        #             print(text)
        #     max_date = str(max(existing_date_list))[:10].replace('-','')+'0000'
        #     get_twets(search_words=i, st_date=str(max_date))
        # except:
        #     pass
        continue
    else:
        get_twets(search_words=i)
        time.sleep(600)