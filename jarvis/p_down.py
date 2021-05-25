from __future__ import unicode_literals
from time import sleep as sl
import os,sys,requests
import youtube_dl as dl
from random import random,randint
import validators as valid

from downloader import *

# downloads soundcloud songs, without logging in through links!!
#ex: https://soundcloud.com/emune/bluise 23 min mp3 song file
#ex: https://soundcloud.com/xjkbeats/six-figures_ep
#download porn videos instantly through a link
#works on https://www.pornhub.com, https://www.xvideos.com,
#, https://www.redtube.com, and https://www.eporner.com , and more
def net(url):
    """
    check if the user has connected to the internet.
    """
    try:
        requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Please check your network connection.")
        return False
    except requests.exceptions.Timeout:
        print("Site is taking too long to load, TimeOut.")
        return False
    except requests.exceptions.TooManyRedirects:
        print("Too many Redirects.")
        return False
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print(e)
        sys.exit(1)
    return True


def check(link):
    """
    checking the validity of the link.
    """
    try:
        requests.get(link)
        return True
    except requests.exceptions.ConnectionError:
        print("disconnected from network.")
        return False
    except requests.exceptions.HTTPError as err:
        print(err)
        return False
config = {
    'Audio': {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'nocheckcertificate': True,
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    },
    'Video': {
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': True,
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


def download(link, data):
    try:
        with dl.YoutubeDL(data) as ydl:
            ydl.download([link])
    except dl.utils.DownloadError as err:
        print(err)


def get_info(link):
    ydl2 = dl.YoutubeDL({'outtmpl': '%(title)s%(ext)s'})
    with ydl2:
        result = ydl2.extract_info(link, download=False)
        if 'entries' in result:
            video = result['entries'][0]
        else:
            video = result
        video_title = video['title']
        video_url = video['url']
    return video_title


def main():
    while True:
        check2='Y'
        if check2 == 'Y':
            choice = input("Would you like to download (youtube) link? or soundcloud link and adult video link (other)?: ")
            if choice == 'other':
                link = input("Enter the link: ")
                if check(link):
                    print("Title Video: " + "{}".format(get_info(link)))
                    print("1.Download an Audio playlist")
                    print("2.Download a Video playlist")
                    print("3.Download a Single Audio")
                    print("4.Download a single video file")
                    check2 = int(input("------------Enter your choice------------: "))
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
                        print("Unknown Choice :(")
                check2 = str(input("do you want to continue?(Y/n): "))
                if check2 == 'n':
                    break
                    print("Enjoy Watching Your Video, BYE/BYE")
                    
            elif choice == 'youtube':
                youtube_link = input("Enter a youtube song link to add to songs.txt: ")
                f = open('/Users/samehphopal/jarvis/songs.txt', 'w')
                f.write(youtube_link)
                f.close()
                if not os.path.exists('/Users/samehphopal/jarvis/Songs'):
                    os.mkdir('/Users/samehphopal/jarvis/Songs')
                else:
                    os.chdir('/Users/samehphopal/jarvis/Songs')
                yt()
        else:
            print("No Option selected, closing...")

        
        
if __name__ == '__main__':
    main()
              
