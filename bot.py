import tweepy 
import datetime
import os
from time import sleep
consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_SECRET')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
imagePath = "zeldameme.jpg"



def publictweet():
    
        tweettopublish = (' ')
        api.update_with_media(imagePath, tweettopublish)

if __name__ == '__main__':
    
    while True:
        dt=datetime.datetime.now()
    
    
        if dt.hour==12 and dt.minute==0 and dt.second==0:
            publictweet()
        
