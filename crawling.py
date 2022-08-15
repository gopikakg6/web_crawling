import argparse
import logging
import requests
from bs4 import BeautifulSoup

logger = None
def parse_args():
    parser = argparse.ArgumentParser(description = "Web crawler")
    parser.add_argument("-d", "--debug", help = "Enable debug logging", action="store_true")
    return parser.parse_args()

def configure_logging(level=logging.INFO):
    global logger
    logger = logging.getLogger("crawler")
    logger.setLevel(level)
    screen_handler = logging.StreamHandler()
    screen_handler.setLevel(level)
    formatter = logging.Formatter("[%(levelname)s] : %(filename)s(%(lineno)d) : %(message)s")
    screen_handler.setFormatter(formatter)
    logger.addHandler(screen_handler)


def get_artists(base):
    resp = requests.get(base)
    soup = BeautifulSoup(resp.content)
    soup.find_all('a')
    soup.find('title')
    tracklists = soup.find('table',attrs={"class": "tracklist"})
    
    
    headings =tracklists.find_all('h3')
    for heading in headings:
        img = heading.find('img')
        if img not in heading:
            print("Artist name: ",heading.text)



def get_songs(base):
    resp = requests.get(base)
    soup = BeautifulSoup(resp.content,'lxml')
    songs = soup.find("table", attrs= {"class": "tracklist"})
    song_link = songs.find_all('a')
    for songs in song_link:
        if songs.find('img') not in songs:
            print(songs.text)


def get_lyrics(base):
    resp = requests.get(base)
    soup = BeautifulSoup(resp.content,'lxml')
    lyrics = soup.find("p",attrs = {"id": "songLyricsDiv"})
    print(lyrics.text)


def main():
    get_songs("http://www.songlyrics.com/michael-jackson-lyrics/")
    get_lyrics("http://www.songlyrics.com/michael-jackson/you-are-not-alone-lyrics/")



if __name__ == "__main__":
    main()
     

    

