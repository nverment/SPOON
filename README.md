Spoon is a tool to help you seamlessly leave Spotify. It can transfer your existing playlists to YouTube Music, if you are into that sort of thing, download them locally and automatically rename and tag them so they look nice and clean in your new Mp3 player :).  

# Installation
## For tech people
Just clone the directory. Keep in mind that in the current version of the tool, any music you download will be saved in a subdirectory of the current one. You need to have Python installed (of course), so do that first. Then, in the same directory, run the following command:

```powershell
pip install -r requirements.txt
```

## For noobs
(I made this tool for my girlfriend now that we don't live in the same city and I can't download music for her to put on her MP3 player. And she doesn't know shit about computers.)

First, download all the files in here (you can just download as a .zip and extract them).
![[images/image-56.png|348x290]]

Then put them in a folder - keep in mind that whatever music you download will be saved to a subfolder of the current one. 

**For Windows:**
Go to the folder where your files are, right-click and press 'Open in Terminal'.
![[images/image-57.png|347x328]]

**For Mac:**
Open the 'Terminal' app and navigate to your folder (the one where you saved the tool) using the following commands:
- `cd` - go to this folder
- `ls` - look inside this folder

So, you will do something like:
```
>>> ls
	\music
	\pictures
	(^^ this will show you the files and folders in the folder you are currently in)
>>> cd \music
```

Then finally run this command:

```powershell
pip install -r requirements.txt
```

Done!

# Setup
Before running, you need to open YouTube Music and log in. Right click on the page and press Inspect, or just press the F12 key.

![[images/image-36.png]]

Then, on your browser, go to the network tab like so. If you don't see any requests (noob translation: the little cells on the table from the images/image) just reload the page or click on something on it (like a playlist of yours). We are looking for the 'browse' request, it helps if you put the word itself on the 'filter' bar (boxed in red in the images/image below).
![[images/image-52.png]]

Click on it, and you should see something like this:
![[images/image-53.png|606x312]]

We want the **Request Headers**. Just click on the 'Raw' toggle and copy everything underneath.
![[images/image-54.png|412x205]]

Then, on the terminal run the following command:

```powershell
ytmusicapi browser
```

Paste everything, and as instructed, press 'Enter', then 'Ctrl+Z', then 'Enter' again.
![[images/image-55.png|683x165]]

You are good to go!

**Note:** Because these headers reset every now and then, you will also need to do this every now and then. So if you see an error like 'browser.json file does not exist', this is your sign. I usually do it once before each session of using the tool and transfer a lot of playlists without the need to re-do it unless I leave it unattended for an hour or so. 

# Usage
Basic command is as follows:

```powershell
python spoon-transfer.py --url playlist_url --name playlist_name
python spoon-tag.py --dir directory
```

Flags are as follows:
spoon-transfer.py
- `--url playlist_url` the URL of the playlist you want to transfer. Note: if the character '&' is in the URL, delete it and try again - it should work.
- `--name playlist_name` the name of the playlist to be created (doesn't have to be the same as the one you already have, just what you want it to be called).
- `--verb` verbose output - it will show some more information on what is happening.
- `--dow` also download the playlist, after it is created in YouTube Music.

spoon-tag.py
- `--dir directory` where the music you want to tag is located. This only works if your files are named after the format 'Artist - Title.mp3' which is the default for spoon-transfer, which is why those tools are packaged together.

Enjoy, and fuck Spotify!