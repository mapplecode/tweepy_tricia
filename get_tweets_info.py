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


def send_data(data,id,user_name,mydb=mydb):
    mycursor = mydb.cursor()
    sql = "INSERT INTO tweets_data (user_name, tweet_id , data) VALUES (%s, %s , %s)"
    val = (str(user_name),str(id) ,str(data))
    mycursor.execute(sql, val)
    mydb.commit()



def check_data(id,mydb=mydb):
    try:
        mycursor = mydb.cursor()
        sql = "SELECT tweets_data.id FROM tweets_data WHERE tweets_data.tweet_id = {};".format(id)
        mycursor.execute(sql)
        data = mycursor.fetchone()
        if data:
            return data[0]
        else:
            return None
    except:
        return None

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
                print(tweet_id, ' of ',user_name)
                exist = check_data(id=str(tweet_id))
                if exist:
                    print(tweet_id , ' ID Already Exist')
                    continue
                data = get_status(tweet_id)
                data_dict = {}
                for k in data.keys():
                    if k == 'retweeted_status':
                        print(data[k].__dict__['_json']['user'])
                    if k == 'user':
                        data_dict['owner'] = data[k].__dict__['_json']['screen_name']
                        if data[k].__dict__['_json']['screen_name'] in user_name:
                            data_dict['is_owner'] = True
                    if k == 'retweeted':
                        data_dict['is_retweeted'] = str(data[k])
                    if k == '_json':
                        users_mentioned = (data[k]['entities']['user_mentions'])
                        ment_list = list()
                        for umd in users_mentioned:
                            print(umd['screen_name'])
                            ment_list.append(umd['screen_name'])
                        data_dict['mentiond_list'] = ment_list
                    if k == 'favorite_count':
                        data_dict['favorite_count'] = data[k]
                    if k == 'is_quote_status':
                        data_dict['is_quote_status'] = data[k]
                    if k == 'retweet_count':
                        data_dict['retweet_count'] = data[k]
                    if k == 'text':
                        data_dict['text'] = data[k]
                print(data_dict)
                print('user - ',user_name)
                try:
                    send_data(data=str(data_dict),id=tweet_id,user_name=user_name)
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
            time.sleep(.5)
    except Exception as e:
        print(e)
        pass
    continue




# status = get_status('1479420858888245249')
# pprint.pprint(status['entities']['user_mentions'])
#
# for i in status.keys():
#     pprint.pprint(status[i])
