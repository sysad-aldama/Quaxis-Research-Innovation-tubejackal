# Description: Quick youtube video downloader. Nothing special. I will add features if required.
# Written by: Jp C Aldama
# Date: 3/7/2020 - 4:46 PM
# Usage: without qoutes or angle brackets 'python tubejackal.py <YouTube URL>'
# License: MIT 
# Written by: JP Aldama (Quaxis Corporation 2020)
# Requirements: pip install pytube3

# Usage [enter exact, no quotes or anglebrackets]: 
# python tubejackal.py https://youtubeurl
# Special Thanks to pytube3 author https://twitter.com/hmartin

from pytube import YouTube 
import os, sys
import time

url = sys.argv[1]
def jack_video(url): 
    """ Download video from YouTube in specified format and resolution to your local machine. """
    start = time.time()
    yt = YouTube(url, on_progress_callback=progress_function)
    os.system('clear')
    print(f'\t\t\t[___________TUBEJACKAL___________]\n')
    print(f'\t\t\t[___More features coming soon!___]\n')
    print(f'\t\t\t[____________JP Aldama___________]\n')
    print(f'\t\t\t[___Quaxis Corporation (c)2020___]\n\n\n') 
    global title
    title = yt.title
    video = yt.streams.first()
    global size     
    size = video.filesize
    yt.streams[0].download() 
    print(f"\n[TUBEJACKAL COMPLETE] -> {title} has sucessfully downloaded!")
    end = time.time()
    elapsed_time = end - start
    print(f'[TUBEJACKAL RUNNING TIME] -> {elapsed_time} seconds...')
    print(f'[TUBEJACKAL EXITING]\n')
    sys.exit()

def progress_function(stream,chunk,bytes_remaining): 
    """ Simple download progress displayed indicating how many bytes were received. """ 
    percent = (100*(size-bytes_remaining))/size
    
    progress = ("[TUBEJACKAL downloading] -> {0} -> {1}% complete".format(title,round(percent,2)))
    sys.stdout.write('\r'+progress)
    
if __name__ == '__main__':
    jack_video(url)
    
