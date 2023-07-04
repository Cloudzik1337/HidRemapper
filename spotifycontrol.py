
import spotipy
import spotipy.util as util
import os
import json
import time 
import requests
import logging
import colorama
import base64



# Spotify API credentials
SPOTIFY_USERNAME = '' # Add your username here
SPOTIFY_CLIENT_ID = '' # Add the client id you get here
SPOTIFY_CLIENT_SECRET = '' # Add the client secret here
SPOTIFY_REDIRECT_URI = 'http://localhost:8080/'

# Spotify scope
SPOTIFY_SCOPE = 'user-modify-playback-state user-read-playback-state'
#if .chache file exists, open it 


def refresh_token(refresh_token_json, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET):
    url= 'https://accounts.spotify.com/api/token'
    tk = base64.b64encode((SPOTIFY_CLIENT_ID+':'+SPOTIFY_CLIENT_SECRET).encode('ascii'))
    headers = { 'Authorization': 'Basic '+ tk.decode('ascii')}
    data = {'grant_type': 'refresh_token', 'refresh_token': refresh_token_json}


    r = requests.post(url, data=data, headers=headers)
    return r.json()







def recash():
    if os.path.exists(".cache"):  
        with open(".cache", "r") as f:
            token = json.load(f)
            timestamp = token["expires_at"]
            refresh_token_json = token["refresh_token"]
            access_token = token["access_token"]
        # if token expired, refresh it
        if time.time() > timestamp:
            refresh_token_json = refresh_token(refresh_token_json, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
            access_token = refresh_token_json["access_token"]
            #formule time now + 3600s
            expires_in = time.time() + refresh_token_json["expires_in"]-100 # -100 to be sure
            with open(".cache", "r") as f:
                # replace old token with new one
                # replace old timestamp with new one
                old_file = f.read()
                old_file = old_file.replace(token["access_token"], access_token)
                old_file = old_file.replace(str(token["expires_at"]), str(expires_in))
                logging.info(f"[SP] {old_file} ")
            with open(".cache", "w") as f:
                f.write(old_file)
            init()

    

spotify = None
def init():
    global spotify
    # Spotify access token

    token = util.prompt_for_user_token(
        SPOTIFY_USERNAME,
        SPOTIFY_SCOPE,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI
    )

    # Create a Spotify object
    spotify = spotipy.Spotify(auth=token)
    

init()
# Function to change the volume
def change_volume(volume_change):
    recash()
        
    try:
        current_volume = spotify.current_playback()['device']['volume_percent']
    except TypeError:
        return False
    new_volume = max(0, min(100, current_volume + volume_change))
    spotify.volume(new_volume)
    return True

global saved_volume
def mute():
    
    global saved_volume
    try:
        current_volume = spotify.current_playback()['device']['volume_percent']
    except TypeError:
        return False
    if current_volume != 0:
        saved_volume = current_volume
        spotify.volume(0)
    else:
        spotify.volume(saved_volume)
    return True