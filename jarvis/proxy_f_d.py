from __future__ import unicode_literals
from selenium import webdriver
from bs4 import BeautifulSoup
from random import choice
import urllib.request, json
from tqdm import tqdm
import requests
import os
#import webbrowser as wb

from time import sleep as sl
import sys 
import youtube_dl as dl
from random import random,randint
import validators as valid


from selenium  import webdriver
import bs4
import webbrowser
#import youtube_dl


#1. search for a usernames profile link and url on insta, and display it in terminal, and browser
#2. You could  then download the url through a proxy request, so the server wont know its yoor ip address requsting the downlaod 
#3. finally, once the file has been downloaded throguh a proxy,it shows the download size/progress, you can name it, and it will save in current directory.

#goes to site and gets random proxy
def get_proxy():
    url = "https://www.sslproxies.org/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    return {'https': choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), 
                                                                      map(lambda x:x.text, soup.findAll('td')[1::8]))))))}

def proxy_request(request_type, url, **kwargs):
    while 1:
        try:
            proxy = get_proxy()#calls the top fucntion, which gets a list of random proxys from "https://www.sslproxies.org/"
            print(f"Using proxy {proxy['https']}")
            response = requests.request(request_type, url, proxies=proxy, timeout=30, **kwargs)
            break
        except Exception as e:
            print(e)
    return response


config = {
    'Audio': {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'nocheckcertificate': True,
        'noplaylist': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    },
    'Video': {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'nocheckcertificate': True,
        'noplaylist': False,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
            #'preferredquality': '137',
        }]
    },
    'list': {
        'listsubtitles': True
    },
    'listformat': {
        'lisformats': True
    }
}

def download_porn_video(url, data):
    try:
        with dl.YoutubeDL(data) as ydl:
            ydl.download([url])
    except dl.utils.DownloadError as err:
        print(err)


def download_yv(url, data):
    if not os.path.exists('/Users/hamimphopal/jarvis/yt_videos'):
        os.mkdir('/Users/hamimphopal/jarvis/yt_videos')
    else:
        os.chdir('/Users/hamimphopal/jarvis/yt_videos')

    with dl.YoutubeDL(data) as ydl:
        ydl.download([url])
        #https://www.youtube.com/watch?v=aZdt7soOQu0
  
          

def download_ys(url, data):
    if not os.path.exists('/Users/hamimphopal/jarvis/YTSongs'):
        os.mkdir('/Users/hamimphopal/jarvis/YTSongs')
        
    else:
        os.chdir('/Users/hamimphopal/jarvis/YTSongs')

    try:
        with dl.YoutubeDL(data) as ydl:
            ydl.download([url])
    except dl.utils.DownloadError as err:
        print(err)




def soundcloud_d(full):
    #full = input("Name of the soundcloud track to download: ")
    ydl_opts = {}
    with dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([full])



def r_song():
    while True:
        url = "https://soundcloud.com/charts/top"
        #webbrowser.open(url)
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
        choice = input(">>> Your choice (x to exit program): ")
        if choice == 'x': break
        else: choice = int(choice)
        print()
        #choice = int(choice)

        # print(genre_links[choice])

        url = "http://soundcloud.com" + genre_links[choice]
        request = requests.get(url)
        webbrowser.open(url)
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

            webbrowser.open("http://soundcloud.com" + track_links[choice])
            full="http://soundcloud.com" + track_links[choice]
            print(full)
            while True:
                option = input("download the audio if you want: y for yes or n for no: ")
                if option == 'n': break
                else: option = 'y'
                soundcloud_d(full)
                break
   
       
       

def main():
    while True:
        print()
        print("Welcome")
        print()
        print("MENU OPTIONS")
        print("1 - download pornhub video")
        print("2 - download url file with proxy")
        print("3 - download youtube video")
        print("4 - get soundcloud web scrapper, and download a soundcloud song")
        print("5 - download a soundcloud song")
        print("6 - download youtube song")
        print("0 - Exit")
        print()
        choice = input("> ")
        print()

        if choice == "0":
            break

        if choice == "1":
            print("Whats's the name of the pornhub link?")
            if not os.path.exists('/Users/hamimphopal/jarvis/adult'):
                    os.mkdir('/Users/hamimphopal/jarvis/adult')
            else:
                    os.chdir('/Users/hamimphopal/jarvis/adult')
            search_video = input("Enter the video link: ")
            download_porn_video(search_video, config['Video'])

        if choice == "2":
            print("Whats's the name of the link?")
            if not os.path.exists('/Users/hamimphopal/jarvis/proxy_files'):
                    os.mkdir('/Users/hamimphopal/jarvis/proxy_files')
            else:
                    os.chdir('/Users/hamimphopal/jarvis/proxy_files')
            chunk_size = 1024 * 1024
            final_url = input("Enter url of file to download: ")
            r = proxy_request('get', final_url, stream = True)
            total_size = int(r.headers['content-length'])
            filename = final_url.split('/')[-1]
            filename = input("Enter name for the file: ")
            with open(filename, 'wb') as f:
                for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'MB'):
                    f.write(data)
                
            print("Download complete for "+filename)

        if choice == "3":
            print("Whats's the name of the youtube video link?")
            search = input("Enter the youtube video link to download: ")
            download_yv(search, config['Video'])
            #https://www.youtube.com/watch?v=LghP41RapDM example link to download
        if choice == "4":
            print("opening soundcloud scrapper")
            if not os.path.exists('/Users/hamimphopal/jarvis/soundcloud_songs'):
                    os.mkdir('/Users/hamimphopal/jarvis/soundcloud_songs')
            else:
                    os.chdir('/Users/hamimphopal/jarvis/soundcloud_songs')
            r_song()

        if choice == "5":
            print("download a soundcloud song link")
            if not os.path.exists('/Users/hamimphopal/jarvis/soundcloud_songs'):
                    os.mkdir('/Users/hamimphopal/jarvis/soundcloud_songs')
            else:
                    os.chdir('/Users/hamimphopal/jarvis/soundcloud_songs')
            full = input("Name of the soundcloud track to download: ")
            soundcloud_d(full)

        if choice == "6":
            print("Whats's the name of the youtube audio link?")
            ytsearch = input("Enter the youtube song link to download: ")
            download_ys(ytsearch, config['Audio'])
            #https://www.youtube.com/watch?v=nlW--ZwTARA&t=41s example audio link to download
            

        print()
        print("Again? (y/n)")
        again = input("> ")
        if again == "n":
            break
        
    
if __name__ == "__main__":
    main()
