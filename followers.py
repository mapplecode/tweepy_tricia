import time
import tweepy
import pandas as pd
from creds import CREDS as credentials
from filter_sql import send_followers,check_username
##############################################################################
##############################################################################
consumer_key = credentials['API_Key']
consumer_secret = credentials['API_Key_Secret']
access_token = credentials['Access_token']
access_token_secret = credentials['Access_token_secret']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
##############################################################################
##############################################################################


mps_csv = pd.read_csv('MPsonTwitter_list_name_main.csv')
friendship_list = []
for i in mps_csv['Screen name']:
    try:
        exist = check_username(id=i)
        if exist:
            print(i, ' ID Already Exist')
            continue
        follower = ''
        friend = ''
        following = ''
        for k in mps_csv['Screen name']:
            try:
                if i == k:
                    continue
                print(i,'-',k)
                data = (api.get_friendship(source_screen_name= i,target_screen_name  =k))[1].__dict__['_json']
                print(data)
                if str(data['following']) == 'True' and str(data['followed_by']) =='True':
                    friend += k+','
                if str(data['following']) == 'True':
                    follower += k+','
                if str(data['followed_by']) == 'True':
                    following += k+','
            except Exception as e:
                print('INNER error')
                print(e)
            time.sleep(2.5)
        print(follower, following, friend)
        data = send_followers(following=following, friends=friend, user_name=i, followers=follower)
        print(data)
        print('saved')
    except Exception as e:
        print('OUTER ERROR')
        print(e)
