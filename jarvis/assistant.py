from downloader import *
from encrypt import *
import instagram_scraper as insta
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import imghdr
from email.message import EmailMessage
import cv2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from requests_html import HTML, HTMLSession
import csv
import numpy as np
import urllib.request
import time
import threading
import math
import requests
import bs4
from textblob import TextBlob 
import sys, tweepy
import matplotlib.pyplot as plt
import json
import csv
import tweepy
import re
import webbrowser as wb
from bs4 import BeautifulSoup
from getpass import getpass
from PrNdOwN import *

#my very own little assistent, that uses voice reconigntion
#from sensitiveInfo import *

engine = pyttsx3.init('dummy')

#api wolframalpha used to qury random stuff, kinda like google home
client = wolframalpha.Client('5EVAUY-493J8VXREU') #my app id from http://developer.wolframalpha.com/portal/myapps/index.html

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

#speak function that takes audio
def speak(audio):
    print('Computer: ' + audio)#takes and prints audio(query that microphone listen for) from myCommand fucntion, and uses speak fucntion to display it in text on terminal
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Hamim, I am your digital assistant Anna the Lady Jarvis!')
speak('When I start listening, speak to me with a command, or type it manually in terminal')
speak('I can also answer questions, by looking for the search query up on wiki, and google')
print(">>> Menu")
print(">>> 1 - youtube link")
print(">>> 2 - porn")
print(">>> 3 - scrape insta username")
print(">>> 4 - insta scraper")
print(">>> 5 - open gmail")
print(">>> 6 - send github csv email")
print(">>> 7 - send twitter email")
print(">>> 8 - scrape github")
print(">>> 9 - quit, abort, bye, or stop(4commands that will exit system)")
print(">>> 10 - twitter")
print(">>> 11 - play soundcloud")
print(">>> 12 - open github")
print(">>> 13 - encryption")
print()
#listens for commands
def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:   #microphone will be source so it can listen to your commannds                                                                    
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source) #listens to command through microphone, which is the source, and saves it in varible audio
    try:
        query = r.recognize_google(audio, language='en-in')#takes the audio varible, which has the command, and uses speeech rec. to understand it in english, and puts it in query varible
        print('User: ' + query + '\n')#prints your query(command) into terminal
        
    except sr.UnknownValueError:
        speak('Sorry Hamim! I didn\'t get that! Try typing the command instead!')
        query = str(input('Command: '))# if speech rec failed, then manually type it in terminal, and it will save your command in the query varible

    return query #returns your query varible
  
#predefined commands for query that computer reconizes, that do specific things
#if __name__ == '__main__':
def assistent(query):
    while True:
        query = myCommand();
        query = query.lower()
        
        if 'youtube link' in query:
            speak('Downloads all youtube links from songs.txt, and downloads into mp3 songs into a folder called Songs')
            youtube_link = input("Enter a youtube song link to add to songs.txt: ")
            f = open('/Users/samehphopal/jarvis/songs.txt', 'w')
            f.write(youtube_link)
            f.close()
            if not os.path.exists('/Users/samehphopal/jarvis/Songs'):
                os.mkdir('/Users/samehphopal/jarvis/Songs')
            else:
                os.chdir('/Users/samehphopal/jarvis/Songs')
            yt()
 

        elif 'porn' in query:
            speak('Downloads the pornhub video in HD, from the link you entered')
            Reset="\033[0m"
            cor = ["\033[1;33m","\033[1;34m","\033[1;30m","\033[1;36m","\033[1;31m","\033[35m","\033[95m","\033[96m","\033[39m","\033[38;5;82m","\033[38;5;198m","\033[38;5;208m","\033[38;5;167m","\033[38;5;91m","\033[38;5;210m","\033[38;5;165m","\033[38;5;49m","\033[38;5;160m","\033[38;5;51m","\033[38;5;13m","\033[38;5;162m","\033[38;5;203m","\033[38;5;113m","\033[38;5;14m"]
            colors = cor[randint(0,15)]
            colors2 = cor[randint(0,15)]
            colors4 = cor[randint(0,15)]
            colors3 = cor[randint(0,15)]
            colors4 = cor[randint(0,15)]
            colors5 = cor[randint(0,15)]
            colors6 = cor[randint(0,15)]
            colors7 = cor[randint(0,15)]
            colors8 = cor[randint(0,15)]
            colors9 = cor[randint(0,15)]
            while True:
                clear()
                banner()
                check2='Y'
                if net('https://pornhub.com/'):
                    if check2 == 'Y':
                        link = input(colors + "["+colors3+"*"+colors4+"]" + colors2 + " Enter the link: " + colors9)
                        if not valid.url(link):
                            print("\n" + colors8 + "["+colors2+"!"+colors5+"]" + colors7 + " Unvalid Url!!!" + colors6)
                            print(colors8 + "["+colors2+"!"+colors5+"]" + colors7 + " Please Try Again" + colors6)
                            exit(1)
                        if check(link):
                            print(colors6 + "Title Video: " +colors+ "{}".format(get_info(link)))
                            print(colors5 + "[*] 1.Download an Audio playlist")
                            print(colors3 + "[*] 2.Download a Video playlist")
                            print(colors7 + "[*] 3.Download a Single Audio")
                            print(colors8 + "[*] 4.Download a single video file")
                            check2 = int(input(colors + "["+colors4+"------------Enter your choice------------"+colors5+"]: "))
                            if check2 in [1, 2, 3, 4]:
                                if check2 == 1:
                                    config['Audio']['noplaylist'] = False
                                    download(link, config['Audio'])
                                elif check2 == 2:
                                    config['Video']['noplaylist'] = False
                                    download(link, config['Video'])
                                elif check2 == 4:
                                    download(link, config['Video'])
                                else:
                                    download(link, config['Audio'])
                            else:
                                print(colors8 + "Unknown Choice :(")
                            check2 = str(input(colors7 + "[*] do you want to continue?(Y/n): "))
                            if check2 == 'n':
                                break
                                print(colors9 + "Enjoy Watching Your Video, BYE/BYE :-D")

        elif 'scrape insta username' in query:
            speak('scraping the given instagram user id')
            username = input("Enter the instagram user-id: ")

            try:
                a = requests.get("https://www.instagram.com/"+username)
                co = a.content
                soup = BeautifulSoup(co,'html.parser')
                link = soup.find_all('meta' , property="og:image")
                print(link)
                print(type(soup))

                imagelink=(str(link[0])[15:])
                imagelink=imagelink[:len(imagelink)-23]
                print(imagelink)
                wb.open_new_tab(imagelink)

            except :
                print("No such username exists")
 

        elif 'insta scraper' in query:
            speak('Downloads a specific amount of pics, into a directory, from the insta username you add')
            ig_users = input("Enter ig username, to add to ig_users.txt, to download images from: ")
            f = open('/Users/samehphopal/jarvis/ig_users.txt', 'w')
            f.write(ig_users)
            f.close()
            profiles = []
            with open("ig_users.txt") as file:
                    for l in file:
                        profiles.append(l.strip())


            x = 0
            def InstaImageScraper():
                number_of_pics = int(input("Enter the max number of isnta pics to download: "))
                ''' Scrape image on profiles '''
                imgScraper = insta.InstagramScraper(usernames=profiles,
                                                    maximum=number_of_pics,
                                                    media_metadata=True, latest=True,
                                                    media_types=['image', 'video'])
                imgScraper.scrape()

                print("image scraping is running, please wait 50 seconds.")


            InstaImageScraper()
            
                        

        elif 'open github' in query:
            speak('opening github for you')
            webbrowser.open('https://github.com/')


        elif 'encryption' in query:
            speak('(E)ncrypt or (D)ecrypt files')
            
            choice = input("Would you like to (E)ncrypt or (D)ecrypt? ")

            if choice == 'E':
                filename = input("File to encrypt: ")
                password = getpass('Password: ')
                encrypt(getKey(password), filename)
                print("Done.")
                continue
            
            elif choice == 'D':
                filename = input("File to decrypt: ")
                password = getpass('Password: ')
                decrypt(getKey(password), filename)
                print("Done.")
                continue
    
            else:
                print("No Option selected, closing...")


        elif 'open hamims website' in query:
            speak('opening your python code board website for you')
            webbrowser.open('http://167.71.157.4/')

        elif 'open python index' in query:
            speak('opening python module index')
            webbrowser.open('https://docs.python.org/3/py-modindex.html')


        elif 'open gmail' in query:
            speak('logging into gmail for you')
            usernameStr = 'hamimphopal50@gmail.com'
            passwordStr = getpass("Enter password:")

            driver = webdriver.Chrome('/Users/samehphopal/downloads/chromedriver 7')
            driver.get(('https://accounts.google.com/ServiceLogin?'
                     'service=mail&continue=https://mail.google'
                     '.com/mail/#identifier'))

# fill in username and hit the next button
            username = driver.find_element_by_id('identifierId')
            username.send_keys(usernameStr)

            nextButton = driver.find_element_by_id('identifierNext')
            nextButton.click()
# wait for transition then continue to fill items
            password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password")))

            password.send_keys(passwordStr)

            signInButton = driver.find_element_by_id('passwordNext')
            signInButton.click()
            print("successfully logged into gmail!")
           
           
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'send github csv email' in query: #sends an email with a csv file with python project names from github
            speak('sending email for you')
            email_user = 'hamimphopal50@gmail.com' #input("what is your gmail address? \n ")
            email_password = getpass("what is the password for that email address? \n  ")
            email_send  = input("Who would you like to send this email too? \n ")

            subject = 'Python daily CSV-Data'

            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject

            body = 'Hi there,this csv file contains the updated/daily scraped python repos from github that are trending the most, containing the name, description, and code link. My website: http://167.71.157.4/'
            msg.attach(MIMEText(body,'plain'))

            filename = 'python_github.csv'
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
            

        elif 'send twitter email' in query: 
            speak('sending email for you')
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
          

        elif 'scrape github' in query:
            speak('Scraping the trending page for python project only, updated daily')
            speak('Saves the newest github python project name, description, and code link into a csv file nicly organized')
            csv_file = open('python_github.csv', 'w')
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Name', 'Description', 'Link'])

            session = HTMLSession()
            r = session.get('https://github.com/trending/python?since=daily')

            articles = r.html.find('article')
            for article in articles:
                headline = article.find('.text-normal', first=True).text
                headline_u = headline.split("/")[0]
                print("Python Github repo name: ", headline_u)

                description = article.find('p', first=True).text 
                print("Description: ", description)

                try: 
                    link = article.find('a', first=True).attrs['href']
                    link_id = link.split('%2F')[1:3]
                    final_link = "/"
                    final_link = final_link.join(link_id)
                    gh_link = f'https://github.com/{final_link}'
                except Exception as e:
                    gh_link = None

                print("Github repo link: ", gh_link)
                print()
                csv_writer.writerow([headline_u, description, gh_link])

            csv_file.close()
        

                                
                    
        elif 'quit' in query or 'abort' in query or 'stop' in query:
            speak('Bye Hamim, have a good day.')
            sys.exit()
           

        elif 'bye' in query:
            speak('Bye Hamim, have a good day.')
            sys.exit()

        elif 'twitter' in query:
            speak('Twitter sentiment Analysis using Python')
            speak('The Tweepy module is used to stream live tweets directly from Twitter in real-time.')
            speak('Sentiment Analysis can used to understand customers opinion on services he/she use.')
            def percentange(part,whole):
                return 100* float(part)/float(whole)



            consumer_key = 'K6VmuHewqBjxDp3IAp18MZqiX'
            consumer_secret = 'VrQHA0MS2mJFsouGgStNyUnqvt1L9YtR6UVdA7PVkPD7Ywhgqd'
            accessToken = '936623210501619713-LgvjALs0n8Ib6XsbmR2PZ5uQrqxyhU1'
            accessTokenSecret = 'g1fX4SuXHsnI0SYMRmVrh5FcMHc4XwEoYyR4BY3BvzHmM'

            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(accessToken, accessTokenSecret)
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
                print(tweet.text)
                analysis = TextBlob(tweet.text)
                polarity += analysis.sentiment.polarity
                print(analysis.sentiment.polarity)
                total += 1
                if(analysis.sentiment.polarity == 0):
                    neutral += 1
                    print("neutral increased " + str(neutral))
                    
                elif(analysis.sentiment.polarity < 0.00):
                    negative += 1
                    print("negative increased " + str(negative))
                    
                elif(analysis.sentiment.polarity > 0.00):
                    positive += 1   
                    print("positive increased " + str(positive))
                
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
        
                      
                                    
        elif 'play soundcloud' in query:
            speak('Welcome to the Python Soundcloud Scraper')
            speak('soundcloud scraper, Explore the Top / New & Hot Charts for all Genres')
            speak('Search Soundcloud for Tracks, Artist, and Mixes')
            top_url = "https://soundcloud.com/charts/top"
            new_url = "https://soundcloud.com/charts/new"
            track_url = "https://soundcloud.com/search/sounds?q="
            artist_url = "https://soundcloud.com/search/people?q="
            mix_url_end = "&filter.duration=epic"

            # create the selenium browser
            browser = webdriver.Chrome('/Users/samehphopal/downloads/chromedriver 7')
            browser.get("https://soundcloud.com")

            # main menu
            print()
            print(">>> Welcome to the Python Soundcloud Scraper")
            print(">>> Explore the Top / New & Hot Charts for all Genres")
            print(">>> Search Soundcloud for Tracks, Artist, and Mixes")
            print()

            # new or top menu
            while True:
                print(">>> Menu")
                print(">>> 1 - Search for a track")
                print(">>> 2 - Search for an artist")
                print(">>> 3 - Search for a mix")
                print(">>> 4 - Top charts")
                print(">>> 5 - New & hot charts")
                print(">>> 0 - Exit")
                print()
                choice = int(input(">>> Your choice: "))
                if choice == 0:
                    browser.quit()
                    break
                print()

                # search for a track
                if choice == 1:
                    name = input("Name of the track: ")
                    print()
                    "%20".join(name.split(" "))
                    browser.get(track_url + name)
                    continue

                # search for an artist
                if choice == 2:
                    name = input("Name of the artist: ")
                    print()
                    "%20".join(name.split(" "))
                    browser.get(artist_url + name)
                    continue

                if choice == 3:
                    name = input("Name of the mix: ")
                    print()
                    "%20".join(name.split(" "))
                    browser.get(track_url + name + mix_url_end)
                    continue

                # genre menu
                while True:
                    print(">>> Genres Available:")
                    print()

                    # genre menu
                    url = ''
                    if choice == 4: url = top_url
                    else: url = new_url

                    # parse the html with beautiful soup
                    request = requests.get(url)
                    soup = bs4.BeautifulSoup(request.text, "lxml")
                    # print request.text

                    genres = soup.select("a[href*=genre]")[2:]
                    # print each genre

                    genre_links = []

                    # print out the available genres
                    for index, genre in enumerate(genres):
                        print(str(index) + ": " + genre.text)
                        genre_links.append(genre.get("href"))

                    print()
                    choice = input(">>> Your choice (x to re-select chart type): ")
                    print()

                    if choice == 'x': break
                    else: choice = int(choice)

                    # print(genre_links[choice])

                    url = "http://soundcloud.com" + genre_links[choice]
                    request = requests.get(url)
                    soup = bs4.BeautifulSoup(request.text, "lxml")

                    tracks = soup.select("h2")[3:]
                    track_links = []
                    track_names = []
                    # print(tracks)

                    for index, track in enumerate(tracks):
                        track_links.append(track.a.get("href"))
                        track_names.append(track.text)
                        print(str(index+1) + ": " + track.text)
                        print()

                    # song selection loop
                    while True:
                        choice = input(">>> Your choice (x to re-select genre): ")
                        print()

                        if choice == 'x': break
                        else: choice = int(choice)-1

                        print("Now playing: " + track_names[choice])
                        print()

                        browser.get("http://soundcloud.com" + track_links[choice])

            print()
            print("Goodbye!")
            print()
        
        
                
       #if command(qury) was not the ones specified above, and are genereal questions that google can answer or wiki, then the else goes into a diffrent part of code, that uses wiki and gets info, for whatever question u ask     
        #api using WOLFRAM-ALPHA for searching stuff like google home would
        else:
            query = query #for ex. asking the assistent a question, who is donald trump?
            speak('Searching...')
            try:
                try:
                    res = client.query(query)#takes your question
                    results = next(res.results).text#converts it to text to display on terminal
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)#searches your query in wiki, and gives 2 sentences of info
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Hamim!')


assistent(myCommand)
