# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "2YY90l9pJjqjUbFcnNDovw31T"
consumer_secret = "gCa7MGO4EBFtzCL09AD8Q50UeurvHNSwS8iyrwdXs3PuSvaykO"
access_token = "943204003202158592-7ShwomVE1H7xFWBSoIBPIUdvCADXHER"
access_token_secret = "KLBfgWhje3DUAngLk4Sew53hYNsNV9HelmTGQZf6vlRMA"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE
# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        "Can't stop. Won't stop. Chatting! This is Tweet #%s!" %
        tweet_number)


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1