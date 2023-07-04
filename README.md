
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
  git clone [https://link-to-project](https://github.com/Cloudzik1337/HidRemapper)
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

8. Open VolumeController.py with a text editor, and populate `SPOTIFY_USERNAME`, `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET` with the ID's from above.

9. By default, Spotify volume up and down are bound to Page Up and Page Down. You can find the names of other keys to bind Spotify volume up and down [here](https://github.com/boppreh/keyboard/blob/e277e3f2baf53ee1d7901cbb562f443f8f861b90/keyboard/_canonical_names.py). NOTE: It appears that the options to rebind to are limited, so it could be easier to rebind your desired key (or rotary encoder) to the desired physical keys.

10. Place `VolumeController.py`, `VolumeController.bat`, `VolumeController.vbs` in the same folder somewhere.

11. Double-click `VolumeController.bat`, and a browser should open asking for authorization for your app to run.

12. The script should now be running, and the opened terminal should just have `>>>` as the prompt (meaning you are in a Python instance).

13. A `.cache` file should be automatically created in the same directory with the information needed to run the script

14. If you want to have the python script automatically run at startup, make a shortcut of `VolumeController.vbs` and place it in the folder that appears when you hit `Win + R` and enter `shell:startup`.

15. And you are ready to go :D

