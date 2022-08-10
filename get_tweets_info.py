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
from mycreds import CREDS as credentials
    #      ------------       #
consumer_key = credentials['API_Key']
consumer_secret = credentials['API_Key_Secret']
access_token = credentials['Access_token']
access_token_secret = credentials['Access_token_secret']
        ######      #####

all_files=os.listdir('id_folder')


def send_data(data,id,user_name,mydb=mydb):
    mycursor = mydb.cursor()
    sql = "INSERT INTO tweets_data (user_name, tweet_id , data) VALUES (%s, %s , %s)"
    val = (str(user_name),str(id) ,str(data))
    mycursor.execute(sql, val)
    mydb.commit()

def get_status(id):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    status = api.get_status(id)
    return (status.__dict__)

for i in all_files:
    try:
        existing_date_list = list()
        old_file = 'id_folder/' + str(i)
        print(i)
        user_name = str(i).replace('.txt','')
        old_file = open(old_file, 'r').read().split('\n')
        for text in old_file:
            try:
                tweet_id = text.split('---')[0]
                print(tweet_id)
                data = get_status(tweet_id)
                try:
                    send_data(data=data,id=tweet_id,user_name=user_name)
                except Exception as e:
                    print(e)
            except:
                print(text)
            time.sleep(2)
    except Exception as e:
        print(e)
        pass
    continue




# status = get_status('1479420858888245249')
# pprint.pprint(status['entities']['user_mentions'])
#
# for i in status.keys():
#     pprint.pprint(status[i])
