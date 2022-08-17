import argparse
import logging
import os
import requests
from bs4 import BeautifulSoup
logger = None
def parse_args():
    parser = argparse.ArgumentParser(description = "Web crawler")
    parser.add_argument("-d", "--debug", help = "Enable debug logging", action="store_true")
    return parser.parse_args()


def configure_logging(level= logging.INFO):
    global logger
    logger = logging.getLogger("crawler")
    logger.setLevel(level)
    screen_handler =logging.StreamHandler()
    screen_handler.setLevel(level)
    formatter = logging.Formatter("[%(levelname)s] : %(filename)s(%(lineno)d) : %(message)s")
    screen_handler.setFormatter(formatter)
    logger.addHandler(screen_handler)



def get_artists(base):
    artists_list = {}
    resp =requests.get(base)
    soup = BeautifulSoup(resp.content,"lxml")
    track_lists = soup.find("table", attrs= {"class": "tracklist"})
    track_link = track_lists.find_all('h3')
    for link in track_link[0:5]:
        artists_list[link.text]  = link.a['href']
    return artists_list



def get_songs(artists_name):
     song_list = {}
     resp = requests.get(artists_name)
     soup = BeautifulSoup(resp.content,'lxml')
     songs = soup.find("table", attrs= {"class": "tracklist"})
     song_link = songs.find_all('a')
     if song_link:
        logger.debug("song list successfully parsed")
        for songs in song_link[0:5]:
            song_list[songs.text]= songs["href"]
     else:
        logger.debug("song list parsing unsuccessfull")
     return song_list



def get_lyrics(song):
     resp = requests.get(song)
     soup = BeautifulSoup(resp.content,'lxml')
     lyrics = soup.find("p",attrs = {"id": "songLyricsDiv"})
     if lyrics:
        logger.debug("lyrics successfully parsed")
     else:
        logger.debug("lyrics parsing unsuccessfull")
     return lyrics.text



def crawl(download_dir):
    for artist_name,artist_link in get_artists("http://www.songlyrics.com/top-artists-lyrics.html").items():
        artist_dir = os.path.join(download_dir,artist_name)
        if not os.path.exists(artist_dir):
            os.makedirs(artist_dir)
        for song ,song_link in get_songs(artist_link).items():
            song_name = song.replace("/","-")
            f = open(f"{artist_dir}/{song_name}.txt",'w')
            lyrics = get_lyrics(song_link)
            f.write(lyrics)
            f.close()


def main():
    args = parse_args()
    if args.debug:
        configure_logging(logging.DEBUG)
    else:
        configure_logging(logging.INFO)
    crawl("artists")
   
if __name__ == "__main__":
    main()
   
