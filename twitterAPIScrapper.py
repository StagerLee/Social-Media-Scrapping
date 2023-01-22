import tweepy
import time
import pandas as pd
import csv

# API keyws that yous saved earlier
api_key = '5jSiFwMvk2f0ZHkmru7xtmSJ4'
api_secrets = 'n8FQz9YYq7XKR9BuyvooGfy0bPnzyZfgY15ZMHElxBp8XyRMfT'
access_token = '1126819147688681472-3IAgUmAC48OagKnwpX1VKVn93Q9T7z'
access_secret = 'WUWgVS28noFlMGAlSMtof2GiDVeGJlIA9KoRd12vE44qQ'
 
# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)
 
#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

results = []

username = ["geertwilderspvv", "markrutte"]
no_of_tweets = 3200

for user in username:
    try:
    #The number of tweets we want to retrieved from the user
        tweets = api.user_timeline(screen_name=username, count=no_of_tweets)
    
    #Pulling Some attributes from the tweet
        attributes_container = [[tweet.created_at, tweet.favorite_count,tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
        columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
        
        data = {"Date Created": tweet.created_at, "Number of Likes": tweet.favorite_count, "Source of Tweet": tweet.source, "Tweet": tweet.text}
    #Creation of Dataframe
        results.append(data)
        tweets_df = pd.DataFrame(results)
tweets_df.to_csv('results.csv', index=False)
        
        tweets_df = pd.DataFrame(attributes_container, columns=columns)
    except BaseException as e:
        print('Status Failed On,',str(e))
        time.sleep(3)