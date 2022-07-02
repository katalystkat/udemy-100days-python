#Scrape billboard 100
#API w Spotify
from bs4 import BeautifulSoup
import requests
import spotipy
import pprint
from spotipy.oauth2 import SpotifyOAuth
USER_ID = input own user ID here 


ClIENT_ID =  input own client id here
CLIENT_SECRET = input own client secret here 


## Get input of what week we are building playlist of
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
webpage = ("https://www.billboard.com/charts/hot-100/" + date)

#Get webpage data from billboard.com with specific year input
response = requests.get(webpage)
music_page = response.text

#Parse through with Beautiful Soup
song_arr = []
soup = BeautifulSoup(music_page, "html.parser")
song_name_tag = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
for songs in song_name_tag:
    titles = songs.getText()
    song_arr.append((titles.strip()))
sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope="playlist-modify-public",
        redirect_uri="http://example.com",
        client_id=ClIENT_ID,
        client_secret= CLIENT_SECRET,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in song_arr:
    result = sp.search(q=f"track:{song} year: {year}", type="track")
    song_uri = result["tracks"]["items"][0]["uri"]
    song_uris.append(song_uri)

#Create a playlist
playlist = sp.user_playlist_create(
    user= USER_ID,
    name=f'{date} Billboard 100',
    public=True,
    collaborative=False,
    description="Learning Spopify API"
)

sp.playlist_add_items(
    playlist_id= playlist["id"],
    items = song_uris
)
# print(song_uris)
# user_playlist_create(user, name, public=True, collaborative = False, description = "API practice")
