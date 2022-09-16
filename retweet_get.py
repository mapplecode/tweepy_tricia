import os
import time

import requests
import tweepy
import pprint
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
 database="tweets"
)


#### CREDS  #####
from creds import CREDS as credentials
    #      ------------       #
consumer_key = credentials['API_Key']
consumer_secret = credentials['API_Key_Secret']
access_token = credentials['Access_token']
access_token_secret = credentials['Access_token_secret']
        ######      #####

all_files=os.listdir('id_folder')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


for i in all_files:
    try:
        existing_date_list = list()
        old_file = 'id_folder/' + str(i)
        user_name = str(i).replace('.txt','')
        old_file = open(old_file, 'r').read().split('\n')
        for text in old_file:
            try:
                tweet_id = text.split('---')[0]
                try:
                    print(tweet_id)
                    data = api.get_status(tweet_id)
                    print(data)
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
        pass