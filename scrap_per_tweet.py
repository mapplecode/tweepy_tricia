import os,sys
import tweepy






id_folder_list = os.listdir('id_folder')
for fold in id_folder_list:
    folder_name = str(fold).replace('@','').replace('.txt','')
    # print(folder_name)
    file_path = os.path.join(os.getcwd(),'id_folder',fold)
    file_total_data = open(file_path,'r').read()
    data = file_total_data.split('\n')
    for info in data:
        tweet_id = info.split('---')[0]
        # print(tweet_id)

