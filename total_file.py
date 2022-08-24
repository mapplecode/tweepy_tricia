import mysql.connector
import json
import re
import ast
import csv
from text_between import get_reply_name
import pandas as pd
from text_between import get_reply_name
mps_csv = pd.read_csv('MPsonTwitter_list_name.csv')
mpskeys = mps_csv.keys()
# print(mps_csv['Screen name'])
MP_DICT = dict()
for i in mps_csv['Screen name']:
    MP_DICT[str(i).replace('@','')] = {'count':0,'mp_who_mentiond':''}

print(MP_DICT)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
 database="tweets"
)


def check_data(mydb=mydb):
    mycursor = mydb.cursor()
    sql = "SELECT tweets_data.user_name,tweets_data.data,tweets_data.tweet_id FROM tweets_data"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data

def get_mps_mentioned_data():
    checkData = check_data()

    for cd in checkData:
        data = eval(cd[1])
        tweet_id = (cd[2])
        data_text = data['text']
        data_mentiond_list = data['mentiond_list']
        data_owner = data['owner']
        data_is_owner = data['is_owner']
        data_is_quote_status = data['is_quote_status']
        data_retweet_count = data['retweet_count']
        data_favorite_count = data['favorite_count']
        data_is_retweeted = data['is_retweeted']
        for mention in data_mentiond_list:
            if mention in MP_DICT.keys():
                count = MP_DICT[mention]['count']
                MP_DICT[mention]['count'] = count +1
                MP_DICT[mention]['mp_who_mentiond'] = str(MP_DICT[mention]['mp_who_mentiond'])+','+str(data_owner)
    with open('count_scrap.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(['MP NAME', 'NO of times mentioned','MPs who mentioned this user'])
        for k,v in MP_DICT.items():
            write.writerow(   [k, v['count'],v['mp_who_mentiond'] ] )

def get_tweet_data():
    checkData = check_data()
    with open('latest_tweets_data.csv', 'w', encoding="utf-8") as f:
        write = csv.writer(f)
        write.writerow(['tweet_id' , 'owner' ,'retweet_count' , 'favorite_count' , 'is_retweeted' ,'mentiond_list' , 'text' ])
        for cd in checkData:
            data = eval(cd[1])
            data_text = data['text']
            tweet_id = (cd[2])
            data_mentiond_list = data['mentiond_list']
            data_owner = data['owner']
            data_is_owner = data['is_owner']
            data_is_quote_status = data['is_quote_status']
            data_retweet_count = data['retweet_count']
            data_favorite_count = data['favorite_count']
            data_is_retweeted = data['is_retweeted']

            write.writerow([tweet_id, data_owner, data_retweet_count,
                            data_favorite_count, data_is_retweeted , data_mentiond_list, str(data_text)])


print(get_tweet_data())