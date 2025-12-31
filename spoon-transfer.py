#!/usr/bin/env python3

import argparse
import sys
import spotipy
import subprocess
from ytmusicapi import YTMusic
from spotipy.oauth2 import SpotifyOAuth
from pathlib import Path
from mutagen.easyid3 import EasyID3

ytmusic = YTMusic("browser.json")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="fb082051a03843e0abd792bae573f9cd",
    client_secret="3ca5e605b6094e0ba1a89027baf27dc8",
    redirect_uri="http://127.0.0.1:1234",
    scope="user-library-read"))

namelist = []

def parse_args():
    parser = argparse.ArgumentParser(
        description=
        "SPOON - The ultimate tool to transfer playlists from Spotify to YouTube. Because that subscription is getting a little too expensive."
    )

    # required
    parser.add_argument(
        "--url", 
        required=True,
        help="Spotify playlist URL")

    parser.add_argument(
        "--name",
        required=True,
        help="Playlist name"
    )

    # optional
    parser.add_argument(
        "--dow",
        action="store_true",
        help="Download the playlist."
    )

    parser.add_argument(
        "--desc",
        default='',
        help="Playlist description"
    )

    parser.add_argument(
        "--verb",
        action="store_true",
        help="Enable verbose output"
    )

    return parser.parse_args()

def validate_spotify_url(url):  
    if "spotify.com/playlist/" not in url:
        print("[X] Wrong Spotify URL format.")
        sys.exit(1)

def spotify_to_yt(url, name, desc):
    uri = (url[34:]).split('?', 1)[0]
    uri = f'spotify:playlist:{uri}'

    results = sp.playlist_items(uri)
    tracks = results['items']

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    playlist_id = ytmusic.create_playlist(
        title=name,
        description=desc,
        privacy_status='public'
    )

    print(f'Creating playlist "{name}"...')

    for t in tracks:
        song_name = t["track"]["name"]
        artist_name = t["track"]["artists"][0]["name"]

        query = f"{song_name} - {artist_name}"
        results = ytmusic.search(query, filter="songs")

        if results:
            video_id = results[0]["videoId"]
            ytmusic.add_playlist_items(playlist_id, [video_id])

            print(f"Added song: {query}")

    playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"
    print(f"\nPlaylist {name} transferred to YouTube Music.")
    return playlist_url

def download_playlist(playlist_url):
    currname = "%(playlist_title)s/%(artist)s - %(title)s.%(ext)s"
    namelist.append(currname)
    cmd = [
        "yt-dlp",
        "--no-warnings", "--quiet",
        "-x",
        "--audio-format", "mp3",
        "-o", currname,
        playlist_url,
    ]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print(f"[X] Failed to download: {yt_url}")
        sys.exit(1)
    print(f"Playlist downloaded!")

def main():
    args = parse_args()

    url = args.url
    name = args.name
    desc = args.desc
    verb = args.verb
    dow = args.dow

    if verb:
        print(f"[+] URL: {url}")
        print(f"[+] Name: {name}")
        print(f"[+] Description: {desc}")

    validate_spotify_url(url)
    yt_url = spotify_to_yt(url, name, desc)

    if dow:
        print(f"\nDownloading playlist '{name}' ...")
        download_playlist(yt_url)

if __name__ == "__main__":
    main()
