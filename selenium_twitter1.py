from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import datetime

driver = webdriver.Chrome()
driver.get("https://twitter.com/markrutte")

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

tweets = []

tweet_elems = driver.find_element('xpath', '//div[@data-testid="tweetText"]')
for tweet in tweet_elems:
    tweets.append(tweet.text)

tweet_ids = driver.find_element('xpath', "//*[@class='tweet']//@data-tweet-id")
for tweet in tweet_ids:
    tweets.append(tweet.get_attribute('data-tweet-id'))

tweet_dates = driver.find_element('xpath', "//*[@class='tweet']//*[@class='_timestamp js-short-timestamp ']")
for tweet in tweet_dates:
    tweets.append(tweet.get_attribute('data-time'))

driver.close()