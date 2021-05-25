#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from textblob import TextBlob 
import sys, tweepy
import matplotlib.pyplot as plt
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from getpass import getpass

def percentange(part,whole):
    return 100* float(part)/float(whole)

def twit_any():
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

    searchTerm = input("Enter keyword/hashtag to search about:")
    noOfSearchTerms = int(input("Enter number of tweet to analyze:"))

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


def send_twit_email():
    email_user = 'hamimphopal50@gmail.com' #input("what is your gmail address? \n ")
    email_password = getpass("what is the password for that email address? \n  ")
    email_send  = input("Who would you like to send this email too? \n ")

    subject = 'Python daily Twitter-Data'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'Hi there, Ive added a png image which was created from a python twitter script that scrapes the 500 most recent tweets about python, and displays its sentimal analysis, based on how positive, negative, and neatral a tweet was is. My website: http://167.71.157.4/'
    msg.attach(MIMEText(body,'plain'))

    filename = input("Enter a filename, with extensions, for the twitter email your sending: ")
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)#init gmail smtp
    server.starttls()#encrypt connection
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    server.quit() #close connection
    print("successfully sent the email message")

#twit_any()
#send_twit_email()

def Main():
    choice = input("Would you like to get tweets(T) or send tweet email(E)?: ")

    if choice == 'T':
        twit_any()
        print("Done getting tweets.")
    elif choice == 'E':
        send_twit_email()
        print("Done sending tweet png email.")
    else:
        print("No Option selected, closing...")

if __name__ == '__main__':
    Main()
	

