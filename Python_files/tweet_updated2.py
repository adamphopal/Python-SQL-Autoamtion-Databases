#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from textblob import TextBlob 
import sys, tweepy
import matplotlib.pyplot as plt
import os
from getpass import getpass
import csv

def percentange(part,whole):
    return 100* float(part)/float(whole)

def twit_any(searchTerm, noOfSearchTerms):
    consumer_key = 'K6VmuHewqBjxDp3IAp18MZqiX'
    consumer_secret = 'VrQHA0MS2mJFsouGgStNyUnqvt1L9YtR6UVdA7PVkPD7Ywhgqd'
    access_token = '936623210501619713-LgvjALs0n8Ib6XsbmR2PZ5uQrqxyhU1'
    access_token_secret = 'g1fX4SuXHsnI0SYMRmVrh5FcMHc4XwEoYyR4BY3BvzHmM'


    #consumer_key = os.environ.get('CONSUMER_KEY')
    #consumer_secret = os.environ.get('CONSUMER_SECRET')
    #access_token = os.environ.get('ACCESS_TOKEN')
    #access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #searchTerm = input("Enter keyword/hashtag to search about:")
    #noOfSearchTerms = int(input("Enter number of tweet to analyze:"))

    tweets = tweepy.Cursor(api.search, q = searchTerm,lang = "en" ).items(noOfSearchTerms)

    positive = 0
    negative = 0
    neutral= 0
    polarity = 0
    total = 0

    for tweet in tweets:
        #print(tweet.text)
        analysis = TextBlob(tweet.text)
        polarity += analysis.sentiment.polarity
        #print(analysis.sentiment.polarity)
        total += 1
        if(analysis.sentiment.polarity == 0):
            neutral += 1
            #print("neutral increased " + str(neutral))
            
        elif(analysis.sentiment.polarity < 0.00):
            negative += 1
            #print("negative increased " + str(negative))
            
        elif(analysis.sentiment.polarity > 0.00):
            positive += 1   
            #print("positive increased " + str(positive))
        
    print("positive "+str(positive))
    print("negative "+str(negative))
    print("neutral "+str(neutral))

    positive = percentange(positive , total)
    negative = percentange(negative , total)
    neutral = percentange(neutral , total)

    positive = format(positive , '.2f' )
    negative = format(negative , '.2f' )
    neutral = format(neutral , '.2f' )

    print("positive %"+str(positive))
    print("negative %"+str(negative))
    print("neutral %"+str(neutral))

    print("How are people reacting on #" + searchTerm + "by analyzing " + str(noOfSearchTerms)+ ' Tweets.')

    if(polarity == 0):
        print("neutral")    
    elif(polarity > 0):
        print("positive")
    elif(polarity < 0):
        print("negative")
        
    labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
    sizes = [positive,neutral, negative ]
    colors = ['yellowgreen',  'gold','red']
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title('How people are reacting on #' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


def scrape_twitter_csv():
    consumer_key = 'K6VmuHewqBjxDp3IAp18MZqiX'
    consumer_secret = 'VrQHA0MS2mJFsouGgStNyUnqvt1L9YtR6UVdA7PVkPD7Ywhgqd'
    access_token = '936623210501619713-LgvjALs0n8Ib6XsbmR2PZ5uQrqxyhU1'
    access_token_secret = 'g1fX4SuXHsnI0SYMRmVrh5FcMHc4XwEoYyR4BY3BvzHmM'

    hashtag_phrase = input("Enter Hashtag Phrase to scrape its hashtags, timestamps, tweet-text, username, and follower count from twitter: ")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #create authentication for accessing Twitter
    auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API
    api = tweepy.API(auth)
    #get the name of the spreadsheet we will write to
    fname = input("Enter name to give to twitter csv file to save data in: ")

    csv_file = open(fname, 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count'])

    for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', \
                                   lang="en", tweet_mode='extended').items(100):
        csv_writer.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'),
        tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']],
        tweet.user.followers_count])

    csv_file.close()


def Main():
    #searchTerm = input("Enter keyword/hashtag to search about:")
    #noOfSearchTerms = int(input("Enter number of tweet to analyze:"))
    #twit_any(searchTerm, noOfSearchTerms)
    #print("Done getting tweets.")

    scrape_twitter_csv()
    print("Done getting csv tweets.")

if __name__ == '__main__':
    Main()
	
