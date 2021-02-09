#!/usr/bin/python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


CLIENT_ID = '81a85361a046433299fb5e441100f4e2'
CLIENT_SECRET = 'da76e7c036f04214a39e4ddaa803afaf'


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri='http://localhost:8888',scope="user-library-read"))
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
