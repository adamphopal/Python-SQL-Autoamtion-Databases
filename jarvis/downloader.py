from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv

# Download data and config



def yt():
        download_options = {
                'format': 'bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'nocheckcertificate': True,
                'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                        }],
                }
        

        
#        if not os.path.exists('Songs'):
#                os.mkdir('Songs')
#        else:
#                os.chdir('Songs')
                
        with youtube_dl.YoutubeDL(download_options) as dl:
                f = open('/Users/samehphopal/jarvis/songs.txt', 'r')
                for song_url in f:
                        dl.download([song_url])
                        
def main():
        youtube_link = input("Enter song link to add to songs.txt: ")
        f = open('/Users/samehphopal/jarvis/songs.txt', 'w')
        f.write(youtube_link)
        f.close()
        if not os.path.exists('/Users/samehphopal/jarvis/Songs'):
                os.mkdir('/Users/samehphopal/jarvis/Songs')
        else:
                os.chdir('/Users/samehphopal/jarvis/Songs')
        yt()



if __name__ == '__main__':
    main()

