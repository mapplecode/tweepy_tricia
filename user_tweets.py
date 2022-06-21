import pandas as pd
import tweepy
from creds import CREDS as credentials
# function to display data of each tweet
import csv
import  time
mps_csv = pd.read_csv('MPsonTwitter_list_name.csv')
mpskeys = mps_csv.keys()
print(mps_csv['Screen name'])
mp_name=list()
for i in mps_csv['Screen name']:
    print(i)
consumer_key = credentials['API_Key']
consumer_secret = credentials['API_Key_Secret']
access_token = credentials['Access_token']
access_token_secret = credentials['Access_token_secret']

userID = "JulianSmithUK"


def scrap_mp():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    print(auth.access_token)

    tweets = api.user_timeline(screen_name=userID,
                               # 200 is the maximum allowed count
                               count=200,
                               include_rts = False,
                               # Necessary to keep full_text
                               # otherwise only the first 140 words are extracted
                               tweet_mode='extended'
                               )
    # print(tweets)

    user = api.get_user(screen_name=userID)
    mentions = api.mentions_timeline()
    print('mentions total - ' ,len(mentions))
    followers = api.get_followers(screen_name=userID,)
    print('followers total - ' ,len(followers))
    data=[]
    import time
    for info in tweets[-10:]:
        print(info)
        time.sleep(1)
        try:
             print("ID: {}".format(info.id))

             # for k,v in info.__dict__.items():
             #     print(k,v)
             retweets_list = api.get_retweets(info.id)

             other_mps_favourits = ''
             # for retweet in liked_list:
             #     for mp_name in mps_csv['Screen name']:
             #         if str(retweet.user.screen_name ) in mp_name:
             #             other_mps_favourits += retweet.user.screen_name + ' , '
             created_time= info.created_at
             favorited = info.favorited
             print(favorited ,'=-=-=--=-=-=-=-')
             print(str(created_time))
             # folowers = api.get_followers(userID)
             # for folowe in folowers:
             #     print(folowe.screen_name)
             users_retweeted = ''
             other_mps_retweeted = ''
             # printing the screen names of the retweeters
             for retweet in retweets_list:
                 for mp_name in mps_csv['Screen name']:
                     if str(retweet.user.screen_name ) in mp_name:
                         other_mps_retweeted += retweet.user.screen_name + ' , '
                 users_retweeted += retweet.user.screen_name+' , '
             data.append(["ID: {}".format(info.id), info.created_at, 'info.full_text',users_retweeted,info.retweet_count,
                          info.favorite_count,info.retweet_count,other_mps_retweeted,other_mps_favourits],)
        except Exception as e:
            print(e)

    with open(userID+'scrap.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(['USERNAME - '+str(userID),'Mentions - '+str(len(mentions)) ,'Followers - '+str(len(followers))])
        write.writerow(['ID','Created time','Full tweet text','User retweeted' , 'Retweet count',
                        'Liked count','Retweet count','List Mps Retweeted','List Mps Liked'])
        for info in data:
            write.writerow(info)
scrap_mp()