
# Hid Remapper
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

Here Is My Inspiration [
David Zhang
](https://www.youtube.com/watch?v=DTJSREjWH7Y&t=360s)

I bought [pi pico](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) board to use this [hid remapper](https://github.com/jfedor2/hid-remapper)

![App Screenshot](https://github.com/jfedor2/hid-remapper/raw/master/images/remapper1.jpg)



## Features

- Windows Volume up/down
- Current Media Next/Previous
- Pause Media
- Volume Up/Down Spotify Only [My Repo](https://github.com/Cloudzik1337/SpotifyVolumeControler)
- Mute Spotify
- Light Steering (Using tuya sockets and tinytuya library)
- Logging errors
- Able to bind every key from range of f13-f23 and shift_f13-Shift_f23




## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd hidremapper
```

Install dependencies

```bash
  pip install [pkg_name]
```

Start program

```bash
  main.py
```

Spotify WebPage will open 

Create Spotify App.
1. Go to [Spotify Developer](https://developer.spotify.com/dashboard/ "Spotify Developer") and login

2. Create App![CreateApp](https://cdn.upload.systems/uploads/s38kIZMc.png "Create App")        

![](https://cdn.upload.systems/uploads/yMr2p6jY.png)
4. Here is our **Client Id and Client Secret which we will use later**![](https://cdn.upload.systems/uploads/E3L1C3L7.png)

5. Click EDIT SETTINGS \
![](https://cdn.upload.systems/uploads/DKkKlLkz.png)

6. Add `http://localhost:8080/` as Redirect URLs \
![](https://cdn.upload.systems/uploads/ycnQL1mU.png)

7. Grab any dependancies with `python -m pip install keyboard` and `python -m pip install spotipy`



## Configuring the Spotify Volume Controller

1. Install the necessary dependencies with the following commands:
```bash
python -m pip install keyboard
python -m pip install spotipy
```
2.Open VolumeController.py with a text editor and populate the SPOTIFY_USERNAME, SPOTIFY_CLIENT_ID, and SPOTIFY_CLIENT_SECRET variables with the IDs obtained in the previous step.

3. A .cache file should be automatically created in the same directory, containing the necessary information to run the script.

4. You are now ready to go! Enjoy the HID remapper functionalities.
