import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import datetime
# Set up your Spotify API credentials
client_id = '797b5af7c6b64882be336f37c8c7e2e5'
client_secret = 'e98df635264843089f9f65d90cf625d4'


# Authenticate with the Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

data = []
def getdata(track,artist,streams):

    track_name = track
    artist_name = artist

    # Search for the track
    results = sp.search(q=f'track:{track_name} artist:{artist_name}', type='track', limit=1)

    # Print the full JSON response
    #print(json.dumps(results, indent=4))
        # Check if any tracks were found
    if results['tracks']['items']:
        track_data = results['tracks']['items'][0]
        track_name = track_data['name']
        artist_name = track_data['artists'][0]['name']
        track_id = track_data['artists'][0]['id']
        image_url = track_data['album']['images'][0]['url']
        
        
        print(f"Track: {track_name}")
        print(f"Artist: {artist_name}")
        print(f"id: {track_id}")
        print(f"Image URL: {image_url}")
        
        data.append({
                "track": track_name,
                "artist": artist_name,
                "id": track_id,
                "image_url": image_url,
                "streams": streams,
        })

            


        json_data = {
        "date": str(datetime.date.today()) ,
        "results": data  
        }


        
        json_output = json.dumps(json_data,indent=4)

        with open("data/processedTopArtist.json", "w") as file:
            json.dump(json_data, file)



        
        
        
    else:
        return {"No results found for the given track and artist."}
    
    

