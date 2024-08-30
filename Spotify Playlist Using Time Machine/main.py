from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which Year You wanna Travel to (YYYY-MM-DD) ?")
site_url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url=site_url)

site_data = response.text

soup = BeautifulSoup(site_data, "html.parser")

song_title_list = [movie.text.strip() for movie in soup.select(".lrv-a-unstyle-list h3#title-of-a-story")]
song_title_list = song_title_list[2:]

SPOTIFY_CLIENT_ID = "ENTER CLIENT ID"
SPOTIFY_CLIENT_SECRET = "ENTER CLIENT SECRET"
redirect_uri = 'http://localhost:8888/callback' #use any redirect

# Set up the scope
scope =  "playlist-modify-private"

# Authenticat
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=redirect_uri,
                                               scope=scope,
                                               cache_path=r"Spotify Playlist Using Time Machine\.cache"))

user_id = sp.current_user()["id"]
print(user_id)


song_urls = []
for song in song_title_list:
    result = sp.search(q=f"track:{song} year:{date.split("-")[0]}", type="track")
    try:
        url = result["tracks"]["items"][0]["uri"]
        song_urls.append(url)
        print(url)
    except:
        print(f"{song} doesnt exist on spotify :(")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} BillBoard 100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_urls)
