import mysql.connector
import json
import re
import ast


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
 database="tweets"
)

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

def check_username(id,mydb=mydb):
    try:
        mycursor = mydb.cursor()
        sql = "SELECT followers.id FROM followers WHERE followers.user_name = {};".format(id)
        mycursor.execute(sql)
        data = mycursor.fetchone()
        if data:
            return data[0]
        else:
            return None
    except Exception as e:
        print(e)
        return None

def send_followers(followers,friends,following,user_name,mydb=mydb):
    try:
        mycursor = mydb.cursor()
        sql = "INSERT INTO followers (user_name, followers , friends, following) VALUES (%s, %s , %s,%s)"
        val = (str(user_name),str(followers) ,str(friends),str(following))
        mycursor.execute(sql, val)
        mydb.commit()
        return True
    except Exception as e:
        print(e)