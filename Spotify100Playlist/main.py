from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
scope = "playlist-modify-private"
REDIRECT_URI = "https://example.com/"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="",
        client_secret="",
        redirect_uri=REDIRECT_URI,
        scope=scope,
        cache_path="token.txt"))

user_id = sp.current_user()["id"]
print(user_id)

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0"}

url="https://www.billboard.com/charts/hot-100/"+date

response = requests.get(url=url, headers= header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
