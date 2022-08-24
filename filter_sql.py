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