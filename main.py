import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = "http://example.com"


# Spotify auth

scope = "playlist-modify-private,playlist-modify-public,playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               show_dialog=True,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]


# Scraping

input_time = input("Enter the date (YYYY-MM-DD) of which playlist you want to create: ")
year = input_time[0: 5]

BILLBOARD_ENDPOINT = "https://www.billboard.com/charts/hot-100/"

song_response = requests.get(url=f"{BILLBOARD_ENDPOINT}{input_time}").text

soup = BeautifulSoup(song_response, "html.parser")

songs_html = soup.select(selector="li > #title-of-a-story")

songs = [song.getText().strip() for song in songs_html]


# Searching for tracks & Creating playlist

current_playlists = [playlist["name"] for playlist in sp.user_playlists(user=user_id, limit=50)["items"]]

if f"Best of {input_time}" not in current_playlists:
    playlist = sp.user_playlist_create(user=user_id, name=f"Best of {input_time}", public=True)

    tracks = []
    for track in songs:
        track_link = sp.search(q=f"remaster%20track:{track}%20year:{year}", type="track")
        if track_link["tracks"]["items"]:
            tracks.append(track_link["tracks"]["items"][0]["uri"])

    sp.playlist_add_items(playlist_id=playlist["id"], items=tracks)


else:
    print("Playlist Already Exists")
