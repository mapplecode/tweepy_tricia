from TwitterAPI import TwitterAPI
from creds import CREDS as credentials


username = "JulianSmithUK"
consumer_key = credentials['API_Key']
consumer_secret = credentials['API_Key_Secret']
access_token = credentials['Access_token']
access_token_secret = credentials['Access_token_secret']
app_name = credentials['NAME']
lable = credentials['NAME']
api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
r = api.request('tweets/search/fullarchive/:{}'.format(lable),
                {'query':username})
for item in r:
    print(item)