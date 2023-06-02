import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

# Set up your Spotify API credentials
client_id = '797b5af7c6b64882be336f37c8c7e2e5'
client_secret = 'e98df635264843089f9f65d90cf625d4'

# Authenticate with the Spotify API

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri='http://localhost:8888/callback'))


top_tracks = sp.current_user_top_tracks(time_range='short_term', limit=10)

# Print the details of the top tracks
for track in top_tracks['items']:
    print(f"Track: {track['name']}")
    print(f"Artist: {track['artists'][0]['name']}")
    print(f"Preview URL: {track['preview_url']}")
    print('---')
