from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import pickle
driver_path = '/media/mapple/241488e2-eb3b-43cf-a9b2-547a01bb9cbc/python_projects/tweepy_tricia/chromedriver'
if os.name == 'nt':
     driver_path = 'win/chromedriver.exe'


driver = webdriver.Chrome(executable_path=driver_path)
driver.implicitly_wait(10)
url_list = ['https://twitter.com/DisneyPlusHS/status/1538055802614714368/']
driver.maximize_window()
cookies = pickle.load(open("cookies.pkl", "rb"))
try:
    for cookie in cookies:
        driver.add_cookie(cookie)
except:
    pass
driver.get('https://twitter.com/i/flow/login')
time.sleep(4)
try:
    username = driver.find_element(By.XPATH,'//input[@autocomplete="username"]')
    username.send_keys('sparsh_3333')
    username.send_keys(Keys.ENTER)
    time.sleep(1)
    input_password = driver.find_element(By.XPATH,'//input[@type="password"]')
    input_password.send_keys('Pass@123')
    input_password.send_keys(Keys.ENTER)
    time.sleep(2)
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
except:
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
user_list = []
for url in url_list:
    driver.get(url)
    time.sleep(1)
    driver.get(driver.current_url+'likes')
    time.sleep(5)
    b= True
    # try:
    liked_by_div = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/section/div')
    liked_inner_div = liked_by_div.find_element(By.TAG_NAME,'div')
    while b==True:

        last_check = len(user_list)
        liked_by_div = liked_inner_div.find_elements(By.XPATH,'/div[@data-testid="cellInnerDiv"]')
        for like_div in liked_by_div:
            try:
                at_ = like_div.find_element(By.TAG_NAME,'a')
                print(str(at_.get_attribute('href')).split('/')[-1])
                name_liker = str(at_.get_attribute('href')).split('/')[-1]
                if name_liker not in user_list:
                    user_list.append(name_liker)
            except Exception as e:
                print(e)
        driver.execute_script("arguments[0].scrollIntoView(true);", liked_by_div[-1])
        if last_check == len(user_list):
            b=False
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(true);", liked_by_div[-1])
