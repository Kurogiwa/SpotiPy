# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# import os

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
#     client_id=os.getenv("SPOTIFY_APP_CLIENT_ID", "SPOTIFY_APP_CLIENT_ID"),
#     client_secret=os.getenv("SPOTIFY_APP_CLIENT_SECRET", "SPOTIFY_APP_CLIENT_SECRET"),
#     redirect_uri="http://localhost:8000/",
#     scope="playlist-read-private"
# ))

# results = sp.current_user_playlists()
# for idx, item in enumerate(results['items']):
#     print(idx, item['name'], "–", item['public'])

# terminar de implementar o cliente, estudar sobre o rpm no sdk e como fazer um banco dedados sql-server no python
# roubar a animação do mydei

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.current_user_playlists()
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s - %s" % (i + 1 + playlists['offset'], playlist['name'],  playlist['public']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
